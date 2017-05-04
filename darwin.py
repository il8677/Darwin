import terrain
import finch

class player:
    hunger = 0
    def update(self):
        if self.hunger > 10:
            return True
        self.hunger += 1


mainMap = terrain.Map(10)
terrain.generateRandomMap(mainMap, 10)