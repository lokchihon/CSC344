// Lok Chi Hon
// Assignment 3
import scala.util.parsing.combinator._

// E := T '||' E | T
// T := F '&&' T | F
// F := '!' A | A
// A := '(' E ')' | C
// C := 'true' | 'false' | c
// c := any alphabetic character

// all need extends tree
abstract class Tree
  case class E(l: Tree) extends Tree
  case class And(l: Tree, r: Tree) extends Tree
  case class Or(l: Tree, r: Tree) extends Tree
  case class Not(l:Tree) extends Tree
  case class Var(str: String) extends Tree
  case class Bool(b: Boolean) extends Tree

object Assignment3 extends Combinators{
  def eval(t: Tree): Tree = t match {

    case E(l) =>
      val evalE = eval(l)
      evalE match{
        case E(l:Tree) => eval(evalE)
        case And(l:Tree, r:Tree) => And(eval(l), eval(r))
        case Or(l:Tree, r: Tree) => Or(eval(l), eval(r))
        case Not(l:Tree) => Not(eval(l))
      }

    case And(l,r) =>
      val evalAndl = eval(l)
      val evalAndr = eval(r)
      (evalAndl, evalAndr) match{
        case (Bool(true),Bool(true)) => Bool(true)
        case (_,Bool(false)) => Bool(false)
        case (Bool(false),_) => Bool(false)
        case (Var(a), Bool(true)) => Var(a)
        case (Bool(true), Var(a)) => Var(a)
        case (Var(a), Var(b)) => And(Var(a),Var(b))
        case (l:Tree, Bool(true)) => eval(l)
        case (Bool(true), r:Tree) => eval(r)
        case (l:Tree, r:Tree) => And(eval(l), eval(r))
    }

    case Or(l,r) =>
      val evalOrl = eval(l)
      val evalOrr = eval(r)
      (evalOrl, evalOrr) match {
        case (Bool(false), Bool(false)) => Bool(false)
        case (_, Bool(true)) => Bool(true)
        case (Bool(true), _) => Bool(true)
        case (Var(a), Bool(false)) => Var(a)
        case (Bool(false),Var(a)) => Var(a)
        case (Var(a),Var(b)) => Or(Var(a), Var(b))
        case (l: Tree, Bool(false)) => eval(l)
        case (Bool(false), r:Tree) => eval(r)
        case (l:Tree, r:Tree) => Or(eval(l), eval(r))
      }

    case Not(a) =>
      val evalNota = eval(a)
      evalNota match {
        case Bool(false) => Bool(true)
        case Bool(true) => Bool(false)
        case _ => Not(evalNota)
      }

    case Var(a) => Var(a)

    case Bool(b) => Bool(b)
  }

  def evalStr(t: Tree): String = t match {

    case E(l) =>
      val evalStrE = evalStr(l)
      evalStrE match {
        case _ => "(" + evalStrE + ")"
      }

    case And(l, r) =>
      val evalStrl = evalStr(l)
      val evalStrr = evalStr(r)
      (evalStrl, evalStrr) match{
        case _ => evalStr(l) + " && " + evalStr(r)
      }

    case Or(l, r) =>
      val evalStrl = evalStr(l)
      val evalStrr = evalStr(r)
      (evalStrl, evalStrr) match {
        case _ => evalStr(l) + " || " + evalStr(r)
      }

    case Not(l) =>
      val evalStrl = evalStr(l)
      evalStrl match{
        case _ => "!" + evalStr(l)
      }

    case Var(a) => a

    case Bool(b) => b.toString()


  }
  def main(args: Array[String]){
    val line = ""
    while( line != "quit"){
      print("expression? ")
      val line = scala.io.StdIn.readLine()
      if (line == "quit"){
        System.exit(0)
      }
      val exp:Tree = parseAll(Ep, line).get
      print("result: ")
      println(evalStr(eval(exp)))
    }
  }
}

// E := T '||' E | T
// T := F '&&' T | F
// F := '!' A | A
// A := '(' E ')' | C
// C := 'true' | 'false' | c
// c := any alphabetic character
class Combinators extends JavaTokenParsers{
  def Ep: Parser[Tree] = T ~ orc ~ Ep ^^ { case l ~ p ~ r => Or(l, r) } | T
  def T: Parser[Tree] = F ~ andc ~ T ^^ { case l ~ p ~ r => And(l, r) }| F
  def F: Parser[Tree] = notc ~ A ^^ { case p ~ r => Not(r) }| A
  def A: Parser[Tree] = leftP ~ Ep ~ rightP ^^ { case p ~ l ~ m => l}| C
  def C: Parser[Tree] = trueB ^^{str =>Bool(true)}| falseB ^^{str =>Bool(false)}| c
  def c: Parser[Tree] = varname

  def varname: Parser[Var] = "[A-Za-z]".r ^^ { str => Var(str) }
  def andc[Tree] = "&&"
  def orc[Tree] = "||"
  def notc[Tree] = "!"
  def leftP[Tree] = "("
  def rightP[Tree] = ")"
  def trueB[Tree] = "true"
  def falseB[Tree] = "false"
}