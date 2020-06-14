# AttainU (Woodpecker): Python Project
```
Project Name : Maze Solver 
Created By   : Divya Jyoti Sen
email Id     : sendivyajyoti@gmail.com

```

## Maze Solver

This program will take input as an MxN matrix of 0s and 1s(0 denoting walls and 1 denoting clear path) and give a matrix of same MxN size in output file. Where 1s will show the shortest path between the start and the destination, and 0s will be the blocked or useless path.

**Read me file content:**
- Whats inside the folder **mazesolver**. 
- How to run MazeSolver In Windows Operating System.
- Approach to tackle the problem.
- Code Explanation.
- Modules used.
- Conclusion.

## Whats inside **mazesolver?**

Github mazesolver folder consists of 4 contents.

1. README.md

2. mazesolver.py

3. input.txt

3. output.txt

### README.md 
User Manual with contents, instructions and information about the project mazesolver.

### mazeSolver.py
Contains the main script/coding of the mazesolver project.

### input.txt
This is an input file which will be used to provide the initial condition of the maze, this will be edited/provided by the user.

### output.txt
This will be the output file in which the mazesolver.py will save the output of the result of given input from input file.

## How to run MazeSolver In Windows OS.

Open the input.txt file and type the desired input in prescribed format and then save it and close.

`Format for typing the input condition.`

Input should be string of space separated integers, numbers of integers denote N of the matrix and number of lines denote M of the matrix.
>space between each integer is a must.

after you are finished typing your input, save the file and close it. Now open command prompt, change your current directory to this mazesolver project folder, and then type the command provided below to execute the mazesolver.py script. 
In case any help needed, type 'python mazesolver.py -h or -help' without quotes for command help menu.


## Command line

This program has 1 command with 3 arguments(1 optional).

- python mazesolver.py --i input.txt --o output.txt --d 3,4

### Arguments
1. --i inputfile.txt
    Use this argument to provide the input file which will contain the input typed by you. By default there exist an input.txt file, if you want to give your own input file then give the name of your inputfile after --i.

2. --o outputfile.txt
    Use this argument to provide the output file which will store the output produced by mazesolver.py. By default there exist an output.txt file, if you want output in your own output file then give the name of your outputfile after --o.

3. --d 3,4 (Optional)
    This argument is optional and will take the value of the provided matrix size in the inputfile by default. This defines the destination in the maze. If you want to give your own destiantion type 2 integers separated by a comma(the coordinates of your destination) after --d. In this example 3,4 means destination is at [3,4] of the matrix with 0 indexing.

    **Important: Dont use any spaces in between integers, only comma and integers allowed.**

## Approach to tackle the problem.

Backtracking method is used in order to find the smallest path in lesser time. BFS algo's time complexity was higher for the shortest path, hence backtracking method is perfect for this scenario. 

### Code Explanation

**main() function--**

This is the main function which initialises the input and output conditions by asking the user from command prompt and then pass them as arguments in the function smazesolvr().

**mazesolvr() function**

First of, input and output files are opened and stored in the variables, then a sol[] is defined to store the solution(this matrix will get modified according to the solution in further functions). After that the next function mazesolvrUtil() is called to update the sol[] and get the result. In the end of this function we wrtie the output file with sol[] and close the files.

**mazesolvrUtil() function**

This is the main fucntion which checks and finds the shortest path with the help of a smaller function nxtMve() which checks whether the next move is valid or not. And this function updates the sol[] recursively accordingly and returns it by assigning the values in it as the shortest path.

**nxtMve() function**

This function is used to check the validity of next move. Returns true if next move exists else returns false.

## Modules Used

In creation of this python program, following module(s) is/are used:

`argparse` - To get user input in command line

## Conclusion

The project was interesting and a bit simpler, so i have decided to optimize it further in future, by adding visualiser to it so that it can show how exactly it is finding the shortest path. And further more I was thinking of making it bidirectional path finder, by doing the same thing from the destiantion side in reverse order simultaneously, which will result in even more reduced time.

`---THANK YOU---`
