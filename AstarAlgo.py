import pygame 
import sys
import math

pygame.init()

width=height=500
screen=pygame.display.set_mode((width,height))

class spot:
    def __init__(self, i,j):
        self.x=i
        self.y=j
        self.f=0
        self.g=0
        self.h=0
        self.closed=False
        self.previous= None
        self.neighbors= []

    def show(self,color,st):
        if self.closed == False :
            pygame.draw.rect(screen, color, (self.x * w, self.y * h, w, h), st)
            pygame.display.update()

    def addNeighbors(self,grid):
        x =self.x
        y=self.y
        if x < cols-1:
            self.neighbors.append(grid[x+1][y])
        if y < rows-1:
            self.neighbors.append(grid[x][y+1])
        if x> 0:
            self.neighbors.append(grid[x-1][y])
        if y >0:
            self.neighbors.append(grid[x][y-1])

rows = 50
cols = 50

w= width/rows
h= height/rows

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
path =[]
openset = []
closedset = []    
flag=0
grid = [0 for i in range(cols)]

for i in range(cols):
    grid[i]= [0 for j in range(rows)] 

for i in range (cols):
    for j in range (rows):
        grid[i][j]= spot(i,j)

for i in range(cols):
    for j in range(rows):
        grid[i][j].show((255,255,255),1)        

for i in range (cols):
    for j in range (rows):
        grid[i][j].addNeighbors(grid)


#start node
start = grid[2][2]
end = grid[49][49]



def heuristic(a,b):
    d= math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
    return d       

openset.append(start)

def main():
    start.show(green,0)
    end.show(grey,0)
    
    if len(openset) > 0:
        lowestindex=0
        for i in range(len(openset)):
            if openset[i].f < openset[lowestindex].f:
                lowestindex=i

        current = openset[lowestindex]

        if current == end:
            flag=1
            print("done")
            path =[]
            temp = current.previous
            while temp!=start:
                print(temp.x,end=" ")
                path.append(temp)
                temp=temp.previous
            for i in range(len(path)):
                path[i].show(blue,0) 
        

        openset.pop(lowestindex)
        closedset.append(current) 
        current.show(red, 0)       # Show closed sets

        for i in range(len(current.neighbors)):
            neighbor=current.neighbors[i]
            if neighbor not in closedset:
                tempG= current.g + 1
                if neighbor in openset:
                    if neighbor.g >tempG:
                        neighbor.g= tempG
                else:
                    neighbor.g = tempG
                    openset.append(neighbor)
                    neighbor.show(green, 0)  # Show opensets

            neighbor.h = heuristic(neighbor,end)
            neighbor.f = neighbor.g + neighbor.h
            if  neighbor.previous == None:
                neighbor.previous = current

        # if flag==2:
        #     for i in range(len(openset)):
        #         openset[i].show(green, 0)

        #     for i in range(len(closedset)):
        #         if closedset[i] != start:
        #             closedset[i].show(red, 0)


pygame.display.flip()


while True:
    ev1 = pygame.event.poll()
    if ev1.type == pygame.QUIT:
        #pygame.display.quit()
        pygame.quit()
        sys.exit()
    main()