import turtle
import time
import sys
import util

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(1300, 700)

class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Visited(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.goto(1000, 1000)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

class Expand(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.goto(1000, 1000)
        self.shape("square")
        self.color("purple")
        self.penup()
        self.speed(0)


class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        # self.goto(1000, 1000)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

grid = open(sys.argv[1], 'r')
grid = grid.read()
grid = grid.split('\n')


def setupMaze(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -230 + (x * 24)
            screen_y = 286 - (y * 24)
            if character == "%":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == "G":
                end.goto(screen_x, screen_y)
                end.stamp()
                finish.append((screen_x, screen_y))

            if character == "S":
                sprite.goto(screen_x, screen_y)


class sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)
    def search(self, s, heuristic=None):
        m = 0
        act = []
        visitedNode = []
        x = round(sprite.xcor(), 0)
        y = round(sprite.ycor(), 0)
        currentState = (x, y)
        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
            s.push((currentState, act, self.heading()))
        elif isinstance(s, util.PriorityQueue):
            s.push((currentState, act, self.heading(), 0), heuristic(currentState, finish[0]))
        while s:
            if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                currentState, action, heading = s.pop()
            elif isinstance(s, util.PriorityQueue):
                currentState, action, heading, oldCost = s.pop()
            x = currentState[0]
            y = currentState[1]
            if not currentState in visitedNode:
                visitedNode.append(currentState)
                if (currentState in finish):
                    sprite.path(action)
                if (heading == 0):
                    if (x + 24, y) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x + 24, y), action + [0] + [0] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x + 24, y), finish[0]) + newCost
                            s.push(((x + 24, y), action + [0] + [0] + [2], 180, newCost), cost)
                    elif (x + 24, y) not in walls and x + 24 < -230 + (24 * len(grid)):
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x + 24, y), action + [0] + [0] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x + 24, y), finish[0]) + newCost
                            s.push(((x + 24, y), action + [0] + [0] + [2], 180, newCost), cost)
                        expand.goto(x + 24, y)
                        expand.stamp()
                    if (x - 24, y) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x - 24, y), action + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x - 24, y), finish[0]) + newCost
                            s.push(((x - 24, y), action + [2], 0, newCost), cost)
                    elif (x - 24, y) not in walls and x - 24 > - 230: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x - 24, y), action + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x - 24, y), finish[0]) + newCost
                            s.push(((x - 24, y), action + [2], 0, newCost), cost)
                        expand.goto(x - 24, y)
                        expand.stamp()
                    if (x, y + 24) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y + 24),action + [1] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y + 24), finish[0]) + newCost
                            s.push(((x, y + 24), action + [1] + [2], 90, newCost), cost)
                    elif (x, y + 24) not in walls and y + 24 < 286: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y + 24),action + [1] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y + 24), finish[0]) + newCost
                            s.push(((x, y + 24), action + [1] + [2], 90, newCost), cost)
                        expand.goto(x, y + 24)
                        expand.stamp()
                    if (x, y - 24) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y - 24), action + [0] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y - 24), finish[0]) + newCost
                            s.push(((x, y - 24), action + [0] + [2], 270, newCost), cost)
                    elif (x, y - 24) not in walls and y - 24 > 286 - (24 * len(grid)): 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y - 24), action + [0] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y - 24), finish[0]) + newCost
                            s.push(((x, y - 24), action + [0] + [2], 270, newCost), cost)
                        expand.goto(x, y - 24)
                        expand.stamp()
                elif (heading == 180):
                    if (x + 24, y) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x + 24, y), action + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x + 24, y), finish[0]) + newCost
                            s.push(((x + 24, y), action + [2], 180, newCost), cost)
                    elif (x + 24, y) not in walls and x + 24 < -230 + (24 * len(grid)):
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x + 24, y), action + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x + 24, y), finish[0]) + newCost
                            s.push(((x + 24, y), action + [2], 180, newCost), cost)
                        expand.goto(x + 24, y)
                        expand.stamp()
                    if (x - 24, y) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x - 24, y),action + [0] + [0] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x - 24, y), finish[0]) + newCost
                            s.push(((x - 24, y), action + [0] + [0] + [2], 0, newCost), cost)
                    elif (x - 24, y) not in walls and x - 24 > - 230: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x - 24, y),action + [0] + [0] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x - 24, y), finish[0]) + newCost
                            s.push(((x - 24, y), action + [0] + [0] + [2], 0, newCost), cost)
                        expand.goto(x - 24, y)
                        expand.stamp()
                    if (x, y + 24) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y + 24), action + [0] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y + 24), finish[0]) + newCost
                            s.push(((x, y + 24), action + [0] + [2], 90, newCost), cost)
                    elif (x, y + 24) not in walls and y + 24 < 286: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y + 24), action + [0] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y + 24), finish[0]) + newCost
                            s.push(((x, y + 24), action + [0] + [2], 90, newCost), cost)
                        expand.goto(x, y + 24)
                        expand.stamp()
                    if (x, y- 24) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y - 24), action + [1] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y - 24), finish[0]) + newCost
                            s.push(((x, y - 24), action + [1] + [2], 270, newCost), cost)
                    elif (x, y - 24) not in walls and y - 24 > 286 - (24 * len(grid)): 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y - 24), action + [1] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y - 24), finish[0]) + newCost
                            s.push(((x, y - 24), action + [1] + [2], 270, newCost), cost)
                        expand.goto(x, y - 24)
                        expand.stamp()
                elif (heading == 90):
                    if (x + 24, y) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x + 24, y), action + [1] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x + 24, y), finish[0]) + newCost
                            s.push(((x + 24, y), action + [1] + [2], 180, newCost), cost)
                    elif (x + 24, y) not in walls and x + 24 < -230 + (24 * len(grid)):
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x + 24, y), action + [1] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x + 24, y), finish[0]) + newCost
                            s.push(((x + 24, y), action + [1] + [2], 180, newCost), cost)
                        expand.goto(x + 24, y)
                        expand.stamp()
                    if (x - 24, y) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x - 24, y), action + [0] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x - 24, y), finish[0]) + newCost
                            s.push(((x - 24, y), action + [0] + [2], 0, newCost), cost)
                    elif (x - 24, y) not in walls and x - 24 > - 230: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x - 24, y), action + [0] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x - 24, y), finish[0]) + newCost
                            s.push(((x - 24, y), action + [0] + [2], 0, newCost), cost)
                        expand.goto(x - 24, y)
                        expand.stamp()
                    if (x, y + 24) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y + 24), action + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y + 24), finish[0]) + newCost
                            s.push(((x, y + 24), action + [2], 90, newCost), cost)
                    elif (x, y + 24) not in walls and y + 24 < 286: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y + 24), action + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y + 24), finish[0]) + newCost
                            s.push(((x, y + 24), action + [2], 90, newCost), cost)
                        expand.goto(x, y + 24)
                        expand.stamp()
                    if (x, y - 24) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y - 24), action + [0] + [0] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y - 24), finish[0]) + newCost
                            s.push(((x, y - 24), action + [0] + [0] + [2], 270, newCost), cost)
                    elif (x, y - 24) not in walls and y - 24 > 286 - (24 * len(grid)): 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y - 24), action + [0] + [0] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y - 24), finish[0]) + newCost
                            s.push(((x, y - 24), action + [0] + [0] + [2], 270, newCost), cost)
                        expand.goto(x, y - 24)
                        expand.stamp()
                else:
                    if (x + 24, y) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x + 24, y), action + [0] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x + 24, y), finish[0]) + newCost
                            s.push(((x + 24, y), action + [0] + [2], 180, newCost), cost)
                    elif (x + 24, y) not in walls and x + 24 < -230 + (24 * len(grid)):
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x + 24, y), action + [0] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x + 24, y), finish[0]) + newCost
                            s.push(((x + 24, y), action + [0] + [2], 180, newCost), cost)
                        expand.goto(x + 24, y)
                        expand.stamp()
                    if (x - 24, y) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x - 24, y), action + [1] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x - 24, y), finish[0]) + newCost
                            s.push(((x - 24, y), action + [1] + [2], 0, newCost), cost)
                    elif (x - 24, y) not in walls and x - 24 > - 230: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x - 24, y), action + [1] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x - 24, y), finish[0]) + newCost
                            s.push(((x - 24, y), action + [1] + [2], 0, newCost), cost)
                        expand.goto(x - 24, y)
                        expand.stamp()
                    if (x, y + 24) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y + 24), action + [0] + [0] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y + 24), finish[0]) + newCost
                            s.push(((x, y + 24), action + [0] + [0] + [2], 90, newCost), cost)
                    elif (x, y + 24) not in walls and y + 24 < 286: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y + 24), action + [0] + [0] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y + 24), finish[0]) + newCost
                            s.push(((x, y + 24), action + [0] + [0] + [2], 90, newCost), cost)
                        if m != 0:
                            expand.goto(x, y + 24)
                            expand.stamp()
                        else: m = 1
                    if (x, y - 24) in finish:
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y - 24), action + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y - 24), finish[0]) + newCost
                            s.push(((x, y - 24), action + [2], 270, newCost), cost)
                    if (x, y - 24) not in walls and y - 24 > 286 - (24 * len(grid)): 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
                            s.push(((x, y - 24), action + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x, y - 24), finish[0]) + newCost
                            s.push(((x, y - 24), action + [2], 270, newCost), cost)
                        expand.goto(x, y - 24)
                        expand.stamp()

    def path(self, action):
        timeRun = wn.textinput("Time", None)
        direction = 3
        x = round(sprite.xcor(), 0)
        y = round(sprite.ycor(), 0)
        for i in action:
            if i == 0:
                self.left(90)
                direction -= 1
                if direction < 0: direction = 3
            elif i == 1:
                self.right(90)
                direction += 1
                if direction > 3: direction = 0
            elif i == 2:
                visited.goto(x, y)
                visited.stamp()
                if (direction == 0): x -= 24
                elif (direction == 1): y += 24
                elif (direction == 2): x += 24
                else: y -= 24
                self.forward(24)
            time.sleep(float(timeRun))
        print("Finished")
        time.sleep(1)
        sys.exit()

    def DFS(self):
        sprite.search(util.Stack())

    def BFS(self):
        sprite.search(util.Queue())

    def nullHeuristic(self, state):
        return 0

    def UCS(self, heuristic=nullHeuristic):
        sprite.search(util.PriorityQueue(), heuristic)

    def manhattanHeuristic(self, state):
        return abs(state[0] - finish[0][0]) + abs(state[1] - finish[0][1])

    def AStar(self, heuristic=manhattanHeuristic):
        sprite.search(util.PriorityQueue(), heuristic)

    def BestFS(self, heuristic=manhattanHeuristic):
        s = util.PriorityQueue()
        m = 0
        act = []
        visitedNode = []
        x = round(sprite.xcor(), 0)
        y = round(sprite.ycor(), 0)
        currentState = (x, y)
        s.push((currentState, act, self.heading()), heuristic(currentState, finish[0]))
        while s:
            currentState, action, heading = s.pop()
            x = currentState[0]
            y = currentState[1]
            if not currentState in visitedNode:
                visitedNode.append(currentState)
                if (currentState in finish):
                    sprite.path(action)
                if (heading == 0):
                    if (x + 24, y) in finish:
                        s.push(((x + 24, y), action + [0] + [0] + [2], 180), heuristic((x + 24, y), finish[0]))
                    elif (x + 24, y) not in walls and x + 24 < -230 + (24 * len(grid)):
                        s.push(((x + 24, y), action + [0] + [0] + [2], 180), heuristic((x + 24, y), finish[0]))
                        expand.goto(x + 24, y)
                        expand.stamp()
                    if (x - 24, y) in finish:
                        s.push(((x - 24, y), action + [2], 0), heuristic((x - 24, y), finish[0]))
                    elif (x - 24, y) not in walls and x - 24 > - 230: 
                        s.push(((x - 24, y), action + [2], 0), heuristic((x - 24, y), finish[0]))
                        expand.goto(x - 24, y)
                        expand.stamp()
                    if (x, y + 24) in finish:
                        s.push(((x, y + 24),action + [1] + [2], 90), heuristic((x, y + 24), finish[0]))
                    elif (x, y + 24) not in walls and y + 24 < 286: 
                        s.push(((x, y + 24),action + [1] + [2], 90), heuristic((x, y + 24), finish[0]))
                        expand.goto(x, y + 24)
                        expand.stamp()
                    if (x, y - 24) in finish:
                        s.push(((x, y - 24), action + [0] + [2], 270), heuristic((x, y - 24), finish[0]))
                    elif (x, y - 24) not in walls and y - 24 > 286 - (24 * len(grid)):
                        s.push(((x, y - 24), action + [0] + [2], 270), heuristic((x, y - 24), finish[0]))
                        expand.goto(x, y - 24)
                        expand.stamp()
                elif (heading == 180):
                    if (x + 24, y) in finish:
                        s.push(((x + 24, y), action + [2], 180), heuristic((x + 24, y), finish[0]))
                    elif (x + 24, y) not in walls and x + 24 < -230 + (24 * len(grid)):
                        s.push(((x + 24, y), action + [2], 180), heuristic((x + 24, y), finish[0]))
                        expand.goto(x + 24, y)
                        expand.stamp()
                    if (x - 24, y) in finish:
                        s.push(((x - 24, y),action + [0] + [0] + [2], 0), heuristic((x - 24, y), finish[0]))
                    elif (x - 24, y) not in walls and x - 24 > - 230: 
                        s.push(((x - 24, y),action + [0] + [0] + [2], 0), heuristic((x - 24, y), finish[0]))
                        expand.goto(x - 24, y)
                        expand.stamp()
                    if (x, y + 24) in finish:
                        s.push(((x, y + 24), action + [0] + [2], 90), heuristic((x, y + 24), finish[0]))
                    elif (x, y + 24) not in walls and y + 24 < 286:  
                        s.push(((x, y + 24), action + [0] + [2], 90), heuristic((x, y + 24), finish[0]))
                        expand.goto(x, y + 24)
                        expand.stamp()
                    if (x, y - 24) in finish:
                        s.push(((x, y - 24), action + [1] + [2], 270), heuristic((x, y - 24), finish[0]))
                    elif (x, y - 24) not in walls and y - 24 > 286 - (24 * len(grid)):
                        s.push(((x, y - 24), action + [1] + [2], 270), heuristic((x, y - 24), finish[0]))
                        expand.goto(x, y - 24)
                        expand.stamp()
                elif (heading == 90):
                    if (x + 24, y) in finish:
                        s.push(((x + 24, y), action + [1] + [2], 180), heuristic((x + 24, y), finish[0]))
                    elif (x + 24, y) not in walls and x + 24 < -230 + (24 * len(grid)):
                        s.push(((x + 24, y), action + [1] + [2], 180), heuristic((x + 24, y), finish[0]))
                        expand.goto(x + 24, y)
                        expand.stamp()
                    if (x - 24, y) in finish:
                        s.push(((x - 24, y), action + [0] + [2], 0), heuristic((x - 24, y), finish[0]))
                    elif (x - 24, y) not in walls and x - 24 > - 230: 
                        s.push(((x - 24, y), action + [0] + [2], 0), heuristic((x - 24, y), finish[0]))
                        expand.goto(x - 24, y)
                        expand.stamp()
                    if (x, y + 24) in finish:
                        s.push(((x, y + 24), action + [2], 90), heuristic((x, y + 24), finish[0]))
                    elif (x, y + 24) not in walls and y + 24 < 286: 
                        s.push(((x, y + 24), action + [2], 90), heuristic((x, y + 24), finish[0]))
                        expand.goto(x, y + 24)
                        expand.stamp()
                    if (x, y - 24) in finish:
                        s.push(((x, y - 24), action + [0] + [0] + [2], 270), heuristic((x, y - 24), finish[0]))
                    elif (x, y - 24) not in walls and y - 24 > 286 - (24 * len(grid)):
                        s.push(((x, y - 24), action + [0] + [0] + [2], 270), heuristic((x, y - 24), finish[0]))
                        expand.goto(x, y - 24)
                        expand.stamp()
                else:
                    if (x + 24, y) in finish:
                        s.push(((x + 24, y), action + [0] + [2], 180), heuristic((x + 24, y), finish[0]))
                    elif (x + 24, y) not in walls and x + 24 < -230 + (24 * len(grid)):
                        s.push(((x + 24, y), action + [0] + [2], 180), heuristic((x + 24, y), finish[0]))
                        expand.goto(x + 24, y)
                        expand.stamp()
                    if (x - 24, y) in finish:
                        s.push(((x - 24, y), action + [1] + [2], 0), heuristic((x - 24, y), finish[0]))
                    elif (x - 24, y) not in walls and x - 24 > - 230: 
                        s.push(((x - 24, y), action + [1] + [2], 0), heuristic((x - 24, y), finish[0]))
                        expand.goto(x - 24, y)
                        expand.stamp()
                    if (x, y + 24) in finish:
                        s.push(((x, y + 24), action + [0] + [0] + [2], 90), heuristic((x, y + 24), finish[0]))
                    elif (x, y + 24) not in walls and y + 24 < 286: 
                        s.push(((x, y + 24), action + [0] + [0] + [2], 90), heuristic((x, y + 24), finish[0]))
                        if m != 0:
                            expand.goto(x, y + 24)
                            expand.stamp()
                        else: m = 1
                    if (x, y - 24) in finish:
                        s.push(((x, y - 24), action + [2], 270), heuristic((x, y - 24), finish[0]))
                    elif (x, y - 24) not in walls and y - 24 > 286 - (24 * len(grid)): 
                        s.push(((x, y - 24), action + [2], 270), heuristic((x, y - 24), finish[0]))
                        expand.goto(x, y - 24)
                        expand.stamp()

# ############ main program starts here  ######################


maze = Maze()
sprite = sprite()
end = End()
walls = []
finish = []
visited = Visited()
expand = Expand()
corner = []

setupMaze(grid)

algorithm = wn.textinput("Algorithm", "Chon 1 trong nhung thuat toan sau:\n DFS \n BFS \n AStar \n UCS \n BestFS ")

if (algorithm == 'DFS'):
    wn.title("Depth - First Search")
    sprite.DFS()
elif (algorithm == 'BFS'):
    wn.title("Breadth - First Search")
    sprite.BFS()
elif (algorithm == 'AStar'):
    wn.title("A Star")
    sprite.AStar()
elif (algorithm == 'UCS'):
    wn.title("Uniform - Cost Search")
    sprite.UCS()
elif (algorithm == 'BestFS'):
    wn.title("Best-First Search")
    sprite.BestFS()


