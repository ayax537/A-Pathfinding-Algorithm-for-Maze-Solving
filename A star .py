# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:27:23 2023

@author: HP
"""

import turtle
import time
import heapq

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Solving Program")
wn.setup(1300, 700)

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        
grid4 = [
    "+++++++++++++++",
    "              e",
    "               ",
    "               ",
    "               ",
    "               ",
    "               ",
    "               ",
    "s              ",
    "+++++++++++++++",
]

grid2 = [
"+++++++++++++++",
"+s+       + +e+",
"+ +++++ +++ + +",
"+ + +       + +",
"+ +   +++ + + +",
"+ + + +   + + +",
"+   + + + + + +",
"+++++ + + + + +",
"+     + + +   +",
"+++++++++++++++",
 ]

grid3 = [
"+++++++++",
"+ ++ ++++",
"+ ++ ++++",
"+ ++ ++++",
"+s   ++++",
"++++ ++++",
"++++ ++++",
"+      e+",
"+++++++++",
 ]

grid1 = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s             +                            +",
"+ +++++++++++ +++++++++++++++ ++++++++ +++++ +",
"+           +                 +        +     +",
"++ +++++++ ++++++++++++++ ++++++++++++++++++++",
"++ ++    + ++           + ++                 +",
"++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
"++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
"++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
"++ ++   ++ ++             ++          +++ ++ +",
"++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
"++    + ++                   ++              +",
"+++++ + +++++++++++++++++++++++ ++++++++++++ +",
"++ ++ +                   ++          +++ ++ +",
"++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
"++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
"++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
"++                     ++ ++ ++              +",
"+++++ ++ + +++++++++++ ++ ++ ++ ++++++++++++e+",
"++++++++++++++++++++++++++++++++++++++++++++++",
 ]

start_x = 0
start_y = 0
end_x = 0
end_y = 0

def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
            if character == " ":
                path.append((screen_x, screen_y))
            if character == "e":
                yellow.goto(screen_x, screen_y)
                yellow.stamp()
                end_x, end_y = screen_x, screen_y
                path.append((screen_x, screen_y))
            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)

def heuristic(cell, goal):
    x1, y1 = cell
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def search(x, y):
    priority_queue = [(heuristic((x, y), (end_x, end_y)), 0, (x, y))]  # Use a priority queue with heuristic
    solution[x, y] = x, y
    while priority_queue:
        time.sleep(0)
        _, cost, current = heapq.heappop(priority_queue)

        x, y = current
        if (x, y) == (end_x, end_y):
            yellow.stamp()
            break

        for dx, dy in [(-24, 0), (24, 0), (0, -24), (0, 24)]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in path and (new_x, new_y) not in visited:
                cell = (new_x, new_y)
                solution[cell] = x, y
                heapq.heappush(priority_queue, (cost + 1 + heuristic(cell, (end_x, end_y)), cost + 1, cell))
                blue.goto(cell)
                blue.stamp()

        visited.append(current)
        green.goto(x, y)
        green.stamp()
        if (x, y) != (start_x, start_y):
            red.goto(solution[x, y])
            red.stamp()

def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]

maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = []
solution = {}

setup_maze(grid1)
search(start_x, start_y)
backRoute(end_x, end_y)

wn.exitonclick()
