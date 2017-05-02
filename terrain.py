import random

class Terrain:
    icon = ""
    movement = 0
    trees=0
    miningquality=0
    def __init__(self, icon, movement, trees,miningquality):
        self.icon=icon
        self.movement=movement
        self.trees=trees
        self.miningquality=miningquality
class Map:
    terrains=[[]]

    def getTerrainAtPoint(self,x,y):
        return self.terrains[x][y]

    def setTerrainAtPoint(self,x,y,newterrain):
        self.terrains[x][y] = newterrain

    def getMap(self):
        final = ""
        for terrainy in self.terrains:
            for terrainx in self.terrains:
                final += terrainx.icon
            final+="\n"
        return final

terrainTemplates = {}

terrainTemplates["corruption"] = Terrain("XX",3,40)
terrainTemplates["forest"] = Terrain("||",2,40)
terrainTemplates["plains"] = Terrain("__", 1, 2)


def generateRandomMap(mapobject):
    MAPSIZE = 10
    generationMap = [[]]
    #Set "seeds"
    for key, value in terrainTemplates:
        x = random.randint(0,MAPSIZE-1)
        y = random.randint(0,MAPSIZE-1)
        mapobject.setTerrainAtPoint(x,y,value)
    print(mapobject.getMap())