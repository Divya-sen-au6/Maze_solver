import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', default='input.txt', type=str, help='Use this command to provide input file, input.txt by default.')
    parser.add_argument('--o', default='output.txt', type=str, help='Use this command to provide output file, output.txt by default.')
    parser.add_argument('--d', default=0, type=str, help='Use this command to give manual destination a,b by default.')
    args = parser.parse_args()
    sys.stdout.write(str(mazesolvr(args)))

M = 0
N = 0
D = [0,0]


def nxtMve(maze, x, y):

    if x >= 0 and x < M and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False


def mazesolvr(args):
    output_file = args.o
    ofile = open(output_file, 'w')
    ofile.write("")
    input_file = args.i
    ifile = open(input_file, 'r')
    lines = ifile.readlines()
    maze = []
    for i in lines:
        maze.append(list(map(int, i.strip().split(' '))))
    
    dest = args.d
    global N
    global M
    global D
    M = len(maze)
    N = len(maze[0])
    if dest == 0:
        D = [M-1,N-1]
    else:
        dest = dest.split(',')
        D = [int(dest[0]), int(dest[1])]
    
    ifile.close()
    sol = [[0 for j in range(N)] for i in range(M)]
    
    if mazesolvrUtil(maze, 0, 0, sol) == False:
        output_file = args.o
        ofile = open(output_file, 'w')
        ofile.write('-1')
        ofile.close()
        print("Solution doesn't exist")
        return False

    output_file = args.o
    ofile = open(output_file, 'a')
    for i in sol:
        b = list(map(str, i))
        b.append('\n')
        ofile.write(' '.join(b))
    ofile.close()

    return True


def mazesolvrUtil(maze, x, y, sol):

    if x == D[0] and y == D[1] and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if nxtMve(maze, x, y) == True:
        sol[x][y] = 1
        if mazesolvrUtil(maze, x + 1, y, sol) == True:
            return True
        if mazesolvrUtil(maze, x, y + 1, sol) == True:
            return True
        sol[x][y] = 0
        return False


if __name__ == "__main__":
    main()
