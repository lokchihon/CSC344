% Lok Chi Hon
% Assignment 4: Prolog

% Cave defined
cave([[0, 0, 2, 3], [2, 0, 1, 2], [3, 0, 3, 1], [6, 0, 1, 2], [7, 0, 1, 3], [8, 0, 4, 4],
 [9, 4, 3, 1], [10, 5, 2, 1], [0, 4, 6, 6], [3, 3, 3, 1], [4, 2, 1, 1], [6, 5, 1, 5],
 [7, 8, 1, 2], [8, 9, 3, 1], [11, 8, 1, 2]]).

% Possible Moves
move([X,SqY],forward,[Y,SqY]) :- Y is X+1.
% move([X,SqY],back,[Y,SqY]) :- Y is X-1.
move([SqX,X],up,[SqX,Y]) :- Y is X+1.
move([SqX,X],down,[SqX,Y]) :- Y is X-1.

% Contains function from Microproject
contains([RectX,RectY,Width,Height],[SqX,SqY]) :-
    RectX<SqX,
    RectY<SqY,
    RectX+Width>=SqX,
    RectY+Height>=SqY.

% Recursive Contains function
doesItContain([],[_,_]) :- false.
doesItContain([H|_],[SqX2,SqY2]) :-
    H =[A,B,C,D],
    contains([A,B,C,D],[SqX2,SqY2]).
doesItContain([_|T],[SqX2,SqY2]) :-
    doesItContain(T,[SqX2,SqY2]).


% Checking membership for retaking steps
not_member(_,[]):-!.
not_member(X,[Head|Tail]) :-
    X \== Head,
    not_member(X,Tail).

% Base Case
fly(Cave,[CaveWidth,CaveHeight],CurrState,[CurrState|Path]) :-
    fly2(Cave, [CaveWidth,CaveHeight],CurrState,[],[CurrState|Path]).

% Final Case
fly2(_,[CaveWidth,_],CurrState,_, CurrState) :-
    CurrState=[CurrX,_],
    CurrX=CaveWidth,
    !.

% Recursive Case
fly2(Cave,[CaveWidth,CaveHeight],CurrState, Visited, [CurrState|Path]) :-
    move(CurrState,_,NextState),
    \+doesItContain(Cave,NextState),
    not_member(NextState, Visited),
    New_Visited = [NextState|Visited],
    fly2(Cave,[CaveWidth, CaveHeight],NextState,New_Visited,Path).