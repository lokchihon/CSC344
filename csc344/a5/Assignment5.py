# Lok Chi Hon
# Assignment 5
import subprocess
import os
import re
import json
import zipfile
import shutil


def createAndEditJSon(currDir):
    for name in os.listdir(currDir):
        if os.path.isdir(os.path.join(currDir, name)):
            if name == 'a1':
                path = os.path.join(currDir + "a1", "summary_a1.json")
                with open(path, "r+") as f:
                    data = json.load(f)
                    data ['name'] = "Assignment1"
                    data['relAddress'] = "a1/Assignment1.c"
                    data['lineCount'] = doWC(currDir + "a1/Assignment1.c")
                    data['identifiers'] = getIds(currDir+"a1/Assignment1.c")
                    f.seek(0)
                    json.dump(data, f)
                    f.truncate()
            if name == 'a2':
                path = os.path.join(currDir + "a2", "summary_a2.json")
                with open(path, "r+") as f:
                    data = json.load(f)
                    data['name'] = "Assignment2"
                    data['relAddress'] = "a2/Assignment2.clj"
                    data['lineCount'] = doWC(currDir + "a2/Assignment2.clj")
                    data['identifiers'] = getIds(currDir+"a2/Assignment2.clj")
                    f.seek(0)
                    json.dump(data, f)
                    f.truncate()
            if name == 'a3':
                path = os.path.join(currDir + "a3", "summary_a3.json")
                with open(path, "r+") as f:
                    data = json.load(f)
                    data['name'] = "Assignment3"
                    data['relAddress'] = "a3/Assignment3.scala"
                    data['lineCount'] = doWC(currDir + "a3/Assignment3.scala")
                    data['identifiers'] = getIds(currDir+"a3/Assignment3.scala")
                    f.seek(0)
                    json.dump(data, f)
                    f.truncate()
            if name == 'a4':
                path = os.path.join(currDir + "a4", "summary_a4.json")
                with open(path, "r+") as f:
                    data = json.load(f)
                    data['name'] = "Assignment4"
                    data['relAddress'] = "a4/Assignment4.pl"
                    data['lineCount'] = doWC(currDir + "a4/Assignment4.pl")
                    data['identifiers'] = getIds(currDir+"a4/Assignment4.pl")
                    f.seek(0)
                    json.dump(data, f)
                    f.truncate()
            if name == 'a5':
                path = os.path.join(currDir + "a5", "summary_a5.json")
                with open(path, "r+") as f:
                    data = json.load(f)
                    data['name'] = "Assignment5"
                    data['relAddress'] = "a5/Assignment5.py"
                    data['lineCount'] = doWC(currDir + "a5/Assignment5.py")
                    data['identifiers'] = getIds(currDir+"a5/Assignment5.py")
                    f.seek(0)
                    json.dump(data, f)
                    f.truncate()

def createHTML(currDir):
    for name in os.listdir(currDir):
        if os.path.isdir(os.path.join(currDir, name)):
            if name == 'a1':
                with open(os.path.join(currDir + "a1", "summary_a1.html"), "w") as write_file:
                    message="""
                    """+"""
                    """
            if name == 'a2':
                with open(os.path.join(currDir + "a2", "summary_a2.html"), "w") as write_file:
                    message="""
                    """+"""
                    """
            if name == 'a3':
                with open(os.path.join(currDir + "a3", "summary_a3.html"), "w") as write_file:
                    message="""
                    """+"""
                    """
            if name == 'a4':
                with open(os.path.join(currDir + "a4", "summary_a4.html"), "w") as write_file:
                    message="""
                    """+"""
                    """
            if name == 'a4':
                with open(os.path.join(currDir + "a5", "summary_a5.html"), "w") as write_file:
                    message="""
                    """+"""
                    """

def defHTML(currDir):
    for name in os.listdir(currDir):
        if os.path.isdir(os.path.join(currDir, name)):
            if name == 'a1':
                path = os.path.join(currDir + "a1", "summary_a1.html")
                with open(currDir + "a1/summary_a1.json","r+") as jd:
                    data = json.dumps(json.load(jd))
                    with open(path, "r+") as f:
                        message = """
                        <html>
                        <body>

                            <h2>Assignment 1 Summary</h2>

                        <p id = "demo"></p>
                        <p id = "demo2"></p>
                        <p id = "demo3"></p>

                        <script>
                        var text = '""" + data + """';
                        obj = JSON.parse(text);
                        document.getElementById("demo").innerHTML =
                        "Name: " + obj.name;
                        document.getElementById("demo2").innerHTML =
                        "Line Count: " + obj.lineCount;

                        var i;
                        var x = "";
                        for (i in obj.identifiers){
                            x+= "<br>"+ obj.identifiers[i] ;
                        }

                        document.getElementById("demo3").innerHTML = 
                        "Identifiers: " + x ;

                        </script>

                        </body>
                        </html>
                        """
                        f.write(message)
                        f.close()

            if name == 'a2':
                path = os.path.join(currDir + "a2", "summary_a2.html")
                with open(currDir + "a2/summary_a2.json","r+") as jd:
                    data = json.dumps(json.load(jd))
                    with open(path, "r+") as f:
                        message = """
                        <html>
                        <body>

                            <h2>Assignment 2 Summary</h2>

                        <p id = "demo"></p>
                        <p id = "demo2"></p>
                        <p id = "demo3"></p>

                        <script>
                        var text = '""" + data + """';
                        obj = JSON.parse(text);
                        document.getElementById("demo").innerHTML =
                        "Name: " + obj.name;
                        document.getElementById("demo2").innerHTML =
                        "Line Count: " + obj.lineCount;

                        var i;
                        var x = "";
                        for (i in obj.identifiers){
                            x+= "<br>"+ obj.identifiers[i] ;
                        }

                        document.getElementById("demo3").innerHTML = 
                        "Identifiers: " + x ;

                        </script>

                        </body>
                        </html>
                        """
                        f.write(message)
                        f.close()

            if name == 'a3':
                path = os.path.join(currDir + "a3", "summary_a3.html")
                with open(currDir + "a3/summary_a3.json","r+") as jd:
                    data = json.dumps(json.load(jd))
                    with open(path, "r+") as f:
                        message = """
                        <html>
                        <body>

                            <h2>Assignment 3 Summary</h2>

                        <p id = "demo"></p>
                        <p id = "demo2"></p>
                        <p id = "demo3"></p>

                        <script>
                        var text = '""" + data + """';
                        obj = JSON.parse(text);
                        document.getElementById("demo").innerHTML =
                        "Name: " + obj.name;
                        document.getElementById("demo2").innerHTML =
                        "Line Count: " + obj.lineCount;

                        var i;
                        var x = "";
                        for (i in obj.identifiers){
                            x+= "<br>"+ obj.identifiers[i] ;
                        }

                        document.getElementById("demo3").innerHTML = 
                        "Identifiers: " + x ;

                        </script>

                        </body>
                        </html>
                        """
                        f.write(message)
                        f.close()

            if name == 'a4':
                path = os.path.join(currDir + "a4", "summary_a4.html")
                with open(currDir + "a4/summary_a4.json","r+") as jd:
                    data = json.dumps(json.load(jd))
                    with open(path, "r+") as f:
                        message = """
                        <html>
                        <body>

                            <h2>Assignment 4 Summary</h2>

                        <p id = "demo"></p>
                        <p id = "demo2"></p>
                        <p id = "demo3"></p>

                        <script>
                        var text = '""" + data + """';
                        obj = JSON.parse(text);
                        document.getElementById("demo").innerHTML =
                        "Name: " + obj.name;
                        document.getElementById("demo2").innerHTML =
                        "Line Count: " + obj.lineCount;

                        var i;
                        var x = "";
                        for (i in obj.identifiers){
                            x+= "<br>"+ obj.identifiers[i] ;
                        }

                        document.getElementById("demo3").innerHTML = 
                        "Identifiers: " + x ;

                        </script>

                        </body>
                        </html>
                        """
                        f.write(message)
                        f.close()

            if name == 'a5':
                path = os.path.join(currDir + "a5", "summary_a5.html")
                with open(currDir + "a5/summary_a5.json","r+") as jd:
                    data = json.dumps(json.load(jd))
                    with open(path, "r+") as f:
                        message = """
                        <html>
                        <body>

                            <h2>Assignment 5 Summary</h2>

                        <p id = "demo"></p>
                        <p id = "demo2"></p>
                        <p id = "demo3"></p>

                        <script>
                        var text = '""" + data + """';
                        obj = JSON.parse(text);
                        document.getElementById("demo").innerHTML =
                        "Name: " + obj.name;
                        document.getElementById("demo2").innerHTML =
                        "Line Count: " + obj.lineCount;

                        var i;
                        var x = "";
                        for (i in obj.identifiers){
                            x+= "<br>"+ obj.identifiers[i] ;
                        }

                        document.getElementById("demo3").innerHTML = 
                        "Identifiers: " + x ;

                        </script>

                        </body>
                        </html>
                        """
                        f.write(message)
                        f.close()


def doWC(filePath):
    numLines = 1
    with open(filePath, 'r') as f:
        for line in f:
            numLines += 1
    return numLines


def getIds(filePath):
    listOfIds = []
    if filePath.endswith(".c"):
        with open(filePath, 'r') as fil:
            for line in fil:
                line = line.lstrip()
                if line.split(' ')[0] != '//':
                    if '"' in line:
                        indexOf = line.find('"')
                        newLine = line[0:indexOf]
                        while indexOf < len(line):
                            indexOf = indexOf + 1
                            if line[indexOf] == '"':
                                newLine = newLine + line[indexOf+1:len(line)]
                                break
                        lineList = re.findall(r'\w+',newLine)
                        for w in lineList:
                            if bool(re.search(r'\d',w)) == False:
                                if w != '_':
                                    listOfIds.append(w)
                    else: 
                        lineList = re.findall(r'\w+', line)
                        for w in lineList:
                            if bool(re.search(r'\d',w)) == False:
                                if w != '_':
                                    listOfIds.append(w)

    if filePath.endswith(".clj"):
        with open(filePath, 'r') as fil:
            for line in fil:
                line = line.lstrip()
                if line.split(' ')[0] != ';;':
                    line = re.findall(r'\w+',line)
                    for w in line:
                        if w not in '0123456789':
                            listOfIds.append(w)

    if filePath.endswith(".scala"):
        with open(filePath, 'r') as fil:
            for line in fil:
                line = line.lstrip()
                if line.split(' ')[0] != '//':
                    if '"' in line:
                        indexOf = line.find('"')
                        newLine = line[0:indexOf]
                        while indexOf < len(line):
                            indexOf = indexOf + 1
                            if line[indexOf] == '"':
                                newLine = newLine + line[indexOf+1:len(line)]
                                break
                        lineList = re.findall(r'\w+',newLine)
                        for w in lineList:
                            if bool(re.search(r'\d',w)) == False:
                                if w != '_':
                                    listOfIds.append(w)
                    else: 
                        lineList = re.findall(r'\w+', line)
                        for w in lineList:
                            if bool(re.search(r'\d',w)) == False:
                                if w != '_':
                                    listOfIds.append(w)

    if filePath.endswith(".pl"):
        with open(filePath, 'r') as fil:
            for line in fil:
                line = line.lstrip()
                if line.split(' ')[0] != '%':
                    line = re.findall(r'\w+',line)
                    for w in line:
                        if bool(re.search(r'\d',w)) == False:
                            if w != '_':
                                listOfIds.append(w)

    if filePath.endswith(".py"):
        with open(filePath, 'r') as fil:
            for line in fil:
                if '#' not in line:
                    if '"""' in line:
                        count = 1
                        line = fil.next()
                        while '"""' not in line:
                            line = fil.next()
                            if '"""' in line:
                                if count == 2:
                                    break
                                count = count + 1
                                line = fil.next()
                        line = fil.next()
                    elif '"' in line:
                        indexOf = line.find('"')
                        newLine = line[0:indexOf]
                        lineList = re.findall(r'\w+',newLine)
                        for w in lineList:
                            if bool(re.search(r'\d',w)) == False:
                                if w != '_':
                                    listOfIds.append(w)
                    elif "'" in line:
                        indexOf = line.find("'")
                        newLine = line[0:indexOf]
                        lineList = re.findall(r'\w+',newLine)
                        for w in lineList:
                            if bool(re.search(r'\d',w)) == False:
                                if w != '_':
                                    listOfIds.append(w)
                    else: 
                        line = line.lstrip()
                        lineList = re.findall(r'\w+', line)
                        for w in lineList:
                            if bool(re.search(r'\d',w)) == False:
                                if w != '_':
                                    listOfIds.append(w)
    
    return (removeDuplicates(removeEmptyIds(listOfIds)))

def removeDuplicates(listOfStuff):
    output = []
    seen = set()
    for stuff in listOfStuff:
        if stuff not in seen:
            output.append(stuff)
            seen.add(stuff)
    return output

def removeEmptyIds(listOfStuff):
    output = []
    for stuff in listOfStuff:
        if stuff != "" and stuff != "!":
                output.append(stuff)
    return output

if __name__ == "__main__":
    # getting directory
    currDir = input("Directory: ")

    # creating json file for each subdirectory
    createAndEditJSon(currDir)
    createHTML(currDir)
    defHTML(currDir)

    # creating valid HTML page called index.html in csc344 directory
    f = open(currDir + 'index.html', 'w')

    message = """
    <html>
    <head>
        <title> CSC344 </title>
    </head>

    <body>
    <h1> Lok Chi Hon's CSC344 Work </h1>
    <ol>Assignment 1 
        <a href="a1/Assignment1.c">source</a>&nbsp;&&nbsp;
        <a href="a1/summary_a1.html">summary</a>
        <br>Assignment 2
        <a href="a2/Assignment2.clj">source</a>&nbsp;&&nbsp;
        <a href="a2/summary_a2.html">summary</a>
        <br>Assignment 3"""+"""
        <a href="a3/Assignment3.scala">source</a>&nbsp;&&nbsp;
        <a href="a3/summary_a3.html">summary</a>
        <br>Assignment 4
        <a href="a4/Assignment4.pl">source</a>&nbsp;&&nbsp;
        <a href="a4/summary_a4.html">summary</a>
        <br>Assignment 5
        <a href="a5/Assignment5.py">source</a>&nbsp;&&nbsp;
        <a href="a5/summary_a5.html">summary</a>
    </body>
    </html>
    """
    f.write(message)
    f.close()

    # making zip file
    shutil.make_archive('CSC344Assignments', 'zip', currDir)

    # prompt user for email address and sends the zip file
    email = input("Email: ")
    command = ('./uuencode CSC344Assignments.zip "CSC344Assignments.zip" | mailx -s "Assignment5" ') + email
    os.system(command)