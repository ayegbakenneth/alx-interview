#!/usr/bin/env python3
""" File executable path """
import sys
""" Module import path """

def first(chess_b, row, column):
    """ This method uses different solutions
    started with left side"""
    for i in range(column):
        if chess_b[row][i] == 1:
            return False

    """ look up upper diagonal on left side """
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if chess_b[i][j] == 1:
            return False

    """ look up lower diagonal on left side """
    for i, j in zip(range(row, len(chess_b), 1), range(column, -1, -1)):
        if chess_b[i][j] == 1:
            return False

    return True

def nqueens_first(chess_b, column, idea):
    """ A method for the nqueens solutions """
    if column >= len(chess_b):
        ideas = []
        for i in range(len(chess_b)):
            for j in range(len(chess_b)):
                if chess_b[i][j] == 1:
                    ideas.append([i, j])
        idea.append(ideas)
        return

    for i in range(len(chess_b)):
        if first(chess_b, i, column):
            chess_b[i][column] = 1
            nqueens_first(chess_b, column + 1, idea)
            chess_b[i][column] = 0

def nqueens(N):
    """ A method for the nqueens solutions """
    chess_b = [[0 for _ in range(N)] for _ in range(N)]
    idea = []
    nqueens_first(chess_b, 0, idea)
    return idea

def main():
    """ The main program function """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    idea = nqueens(N)
    for ken in idea:
        print(ken)

if __name__ == "__main__":
    main()
