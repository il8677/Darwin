import random
from time import time

ms=9

class Terrain:
    icon = ""
    movement = 0
    trees=0
    miningquality=0
    def __init__(self, icon, movement, trees,miningquality,foodDensity):
        self.icon=icon
        self.movement=movement
        self.trees=trees
        self.miningquality=miningquality

class Map:
    terrains=[]

    def __init__(self, MAPSIZE):
        self.MAPSIZE = MAPSIZE
        for i in range(0, MAPSIZE):
            self.terrains.append([])
            for n in range(0, MAPSIZE):
                self.terrains[i].append(terrainTemplates["empty"])
        pass
    def getTerrainAtPoint(self,x,y):
        return self.terrains[x][y]

    def setTerrainAtPoint(self,x,y,newterrain):
        self.terrains[x][y] = newterrain

    def getMap(self):
        final = ""
        for terrainy in range(0,self.MAPSIZE):
            for terrainx in range(0,self.MAPSIZE):
                final += self.terrains[terrainy][terrainx].icon
            final+="\n"
        return final
    def getMapWithPlayer(self,px,py):
        final = ""
        for terrainy in range(0,self.MAPSIZE):
            for terrainx in range(0,self.MAPSIZE):
                if not px == terrainx and py == terrainy:
                    final += self.terrains[terrainy][terrainx].icon
                else:
                    final += "PP"
            final+="\n"
        return final

terrainTemplates = {}

terrainTemplates["empty"] = Terrain("  ",0,0,0,0)
terrainTemplates["corruption"] = Terrain("XX",3,40,1,0)
terrainTemplates["forest"] = Terrain("||",2,40, 20,10)
terrainTemplates["plains"] = Terrain("__", 1, 2, 15,2)
terrainTemplates["mountains"] = Terrain("^^",2,5,45,5)

def translateKeyIntoInt(key):
    it = 0
    for i in terrainTemplates.keys():
        if i  == key:
            return it
        it+=1

def up(y):
    if y+1 < 10:
        return y+1
    else:
        return 0
def down(y):
    if(y - 1 >= 0):
        return y-1
    else:
        return ms
def left(x):
    if x-1 >= 0:
        return x-1
    else:
        return ms
def right(x):
    if(x + 1 < 10):
        return x+1
    else:
        return ms
def printgenmap(generationMap):
    for yy in range(0,ms):
        for xx in range(0,ms):
            print(generationMap[xx][yy],end="")
            print(" ",end="")
        print(end="\n")

def generateRandomMap(mapobject, MAPSIZE):
    generationMap = []
    for y in range(0, MAPSIZE):
        generationMap.append([])
        for x in range(0,MAPSIZE):
            generationMap[y].append(1000)
    random.seed=time()
    #Set "seeds"
    for value in terrainTemplates.values():
        x = random.randint(0,MAPSIZE-1)
        y = random.randint(0,MAPSIZE-1)
        mapobject.setTerrainAtPoint(x,y,value)
        generationMap[x][y] = 0
    print(mapobject.getMap())
    #Spread
    for i in range(0, 1000):
        for y in range(0, MAPSIZE):
            for x in range(0, MAPSIZE):
                if mapobject.getTerrainAtPoint(x,y).icon != "  ":
                    if generationMap[x][up(y)] > generationMap[x][y]:
                        generationMap[x][up(y)] = generationMap[x][y] + 1
                        mapobject.setTerrainAtPoint(x,up(y), mapobject.getTerrainAtPoint(x,y))

                    if generationMap[x][down(y)] > generationMap[x][y]:
                        generationMap[x][down(y)] = generationMap[x][y] + 1
                        mapobject.setTerrainAtPoint(x, down(y), mapobject.getTerrainAtPoint(x, y))

                    if generationMap[left(x)][y] > generationMap[x][y]:
                        generationMap[left(x)][y] = generationMap[x][y] + 1
                        mapobject.setTerrainAtPoint(left(x), y, mapobject.getTerrainAtPoint(x, y))


                    if generationMap[right(x)][y] > generationMap[x][y]:
                        generationMap[right(x)][y] = generationMap[x][y] + 1
                        mapobject.setTerrainAtPoint(right(x), y, mapobject.getTerrainAtPoint(x, y))
    for y in range(0, MAPSIZE):
        for x in range(0, MAPSIZE):
            if mapobject.getTerrainAtPoint(x,y).icon == "  ":
                mapobject.setTerrainAtPoint(x,y, mapobject.getTerrainAtPoint(random.randrange(0,MAPSIZE),random.randrange(0,MAPSIZE)))

    print(mapobject.getMap())