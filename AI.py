import turtle                   
import time
import sys
import util

wn = turtle.Screen()              
wn.bgcolor("black")               
# wn.setup(600,610)                 
wn.setup(1300, 700)

class Maze(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")           
        self.color("yellow")          
        self.penup()               
        self.speed(0)                

class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
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
        act = []
        visitedNode = []
        x_walls = round(sprite.xcor(),0)         
        y_walls = round(sprite.ycor(),0)
        currentState = (x_walls, y_walls)
        if isinstance(s, util.Stack) or isinstance(s, util.Queue):
            s.push((currentState, act, self.heading()))
        elif isinstance(s, util.PriorityQueue):
            s.push((currentState, act, self.heading(), 0), heuristic(currentState, finish[0]))
        while s:
            if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                currentState, action, heading = s.pop()
            elif isinstance(s, util.PriorityQueue):
                currentState, action, heading, oldCost = s.pop()
            x_walls = currentState[0]
            y_walls = currentState[1]
            if not currentState in visitedNode:
                visitedNode.append(currentState)
                if (currentState in finish):
                    sprite.path(action)
                if (heading == 0):  
                    if (x_walls + 24, y_walls) not in walls:     
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls + 24, y_walls),action + [0] + [0] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls + 24, y_walls),action + [0] + [0] + [2], 180, newCost), cost)
                    if (x_walls - 24, y_walls) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls - 24, y_walls),action + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls - 24, y_walls),action + [2], 0, newCost), cost)
                    if (x_walls, y_walls + 24) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls, y_walls + 24),action + [1] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls, y_walls + 24),action + [1] + [2], 90, newCost), cost)
                    if (x_walls, y_walls - 24) not in walls: 
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls, y_walls - 24),action + [0] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls, y_walls - 24),action + [0] + [2], 270, newCost), cost)         
                elif (heading == 180):  
                    if (x_walls + 24, y_walls) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls + 24, y_walls),action + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls + 24, y_walls),action + [2], 180, newCost), cost)      
                    if (x_walls - 24, y_walls) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls - 24, y_walls),action + [0] + [0] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls - 24, y_walls),action + [0] + [0] + [2], 0, newCost), cost) 
                    if (x_walls, y_walls + 24) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls, y_walls + 24),action + [0] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls, y_walls + 24),action + [0] + [2], 90, newCost), cost) 
                    if (x_walls, y_walls - 24) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls, y_walls - 24),action + [1] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls, y_walls - 24),action + [1] + [2], 270, newCost), cost) 
                elif (heading == 90):  
                    if (x_walls + 24, y_walls) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls + 24, y_walls),action + [1] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls + 24, y_walls),action + [1] + [2], 180, newCost), cost) 
                    if (x_walls - 24, y_walls) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls - 24, y_walls),action + [0] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls - 24, y_walls),action + [0] + [2], 0, newCost), cost) 
                    if (x_walls, y_walls + 24) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls, y_walls + 24),action + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls, y_walls + 24),action + [2], 90, newCost), cost) 
                    if (x_walls, y_walls - 24) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls, y_walls - 24),action + [0] + [0] + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls, y_walls - 24),action + [0] + [0] + [2], 270, newCost), cost) 
                else:
                    if (x_walls + 24, y_walls) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls + 24, y_walls),action + [0] + [2], 180))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls + 24, y_walls),action + [0] + [2], 180, newCost), cost) 
                    if (x_walls - 24, y_walls) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls - 24, y_walls),action + [1] + [2], 0))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls - 24, y_walls),action + [1] + [2], 0, newCost), cost) 
                    if (x_walls, y_walls + 24) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls, y_walls + 24),action + [0] + [0] + [2], 90))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls, y_walls + 24),action + [0] + [0] + [2], 90, newCost), cost) 
                    if (x_walls, y_walls - 24) not in walls:          
                        if isinstance(s, util.Stack) or isinstance(s, util.Queue):     
                            s.push(((x_walls, y_walls - 24),action + [2], 270))
                        elif isinstance(s, util.PriorityQueue):
                            newCost = oldCost + 1
                            cost = heuristic((x_walls + 24, y_walls), finish[0]) + newCost
                            s.push(((x_walls, y_walls - 24),action + [2], 270, newCost), cost) 
    def path(self, action):
        for i in action:
            if i == 0:
                self.left(90)
            elif i == 1:
                self.right(90)
            elif i == 2:
                self.forward(24)
            time.sleep(float(sys.argv[3]))
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
        act = []
        visitedNode = []
        x_walls = round(sprite.xcor(),0)         
        y_walls = round(sprite.ycor(),0)
        currentState = (x_walls, y_walls)
        s.push((currentState, act, self.heading()), heuristic(currentState, finish[0]))
        while s:
            currentState, action, heading = s.pop()
            x_walls = currentState[0]
            y_walls = currentState[1]
            if not currentState in visitedNode:
                visitedNode.append(currentState)
                if (currentState in finish):
                    sprite.path(action)
                if (heading == 0):  
                    if (x_walls + 24, y_walls) not in walls:     
                        s.push(((x_walls + 24, y_walls),action + [0] + [0] + [2], 180), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls - 24, y_walls) not in walls:           
                        s.push(((x_walls - 24, y_walls),action + [2], 0), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls, y_walls + 24) not in walls:              
                        s.push(((x_walls, y_walls + 24),action + [1] + [2], 90), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls, y_walls - 24) not in walls:    
                        s.push(((x_walls, y_walls - 24),action + [0] + [2], 270), heuristic((x_walls + 24, y_walls), finish[0]))    
                elif (heading == 180):  
                    if (x_walls + 24, y_walls) not in walls:            
                        s.push(((x_walls + 24, y_walls),action + [2], 180), heuristic((x_walls + 24, y_walls), finish[0]))   
                    if (x_walls - 24, y_walls) not in walls:            
                        s.push(((x_walls - 24, y_walls),action + [0] + [0] + [2], 0), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls, y_walls + 24) not in walls:             
                        s.push(((x_walls, y_walls + 24),action + [0] + [2], 90), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls, y_walls - 24) not in walls:          
                        s.push(((x_walls, y_walls - 24),action + [1] + [2], 270), heuristic((x_walls + 24, y_walls), finish[0]))
                elif (heading == 90):  
                    if (x_walls + 24, y_walls) not in walls:          
                        s.push(((x_walls + 24, y_walls),action + [1] + [2], 180), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls - 24, y_walls) not in walls:          
                        s.push(((x_walls - 24, y_walls),action + [0] + [2], 0), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls, y_walls + 24) not in walls:          
                        s.push(((x_walls, y_walls + 24),action + [2], 90), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls, y_walls - 24) not in walls:          
                        s.push(((x_walls, y_walls - 24),action + [0] + [0] + [2], 270), heuristic((x_walls + 24, y_walls), finish[0]))
                else:
                    if (x_walls + 24, y_walls) not in walls:          
                        s.push(((x_walls + 24, y_walls),action + [0] + [2], 180), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls - 24, y_walls) not in walls:          
                        s.push(((x_walls - 24, y_walls),action + [1] + [2], 0), heuristic((x_walls + 24, y_walls), finish[0])) 
                    if (x_walls, y_walls + 24) not in walls:          
                        s.push(((x_walls, y_walls + 24),action + [0] + [0] + [2], 90), heuristic((x_walls + 24, y_walls), finish[0]))
                    if (x_walls, y_walls - 24) not in walls:          
                        s.push(((x_walls, y_walls - 24),action + [2], 270), heuristic((x_walls + 24, y_walls), finish[0]))
# ############ main program starts here  ######################

maze = Maze()               
sprite = sprite()           
end = End()              
walls =[]                 
finish = []             

setupMaze(grid)        

if (sys.argv[2] == 'DFS'):
    sprite.DFS()
elif (sys.argv[2] == 'BFS'):
    sprite.BFS()
elif (sys.argv[2] == 'AStar'):
    sprite.AStar()
elif (sys.argv[2] == 'UCS'):
    sprite.UCS()
elif (sys.argv[2] == 'BestFS'):
    sprite.BestFS()