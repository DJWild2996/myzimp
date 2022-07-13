from abstract_product_A import TileProduct
from directions import Direction as myD


# ConcreteProductA1
class IndoorTile(TileProduct):
    def __init__(self, name, effect=None, doors=None, x=16, y=16, entrance=None):
        if doors is None:
            doors = []
        self.type = "Indoor"
        self.name = name
        self.x = x
        self.y = y
        self.effect = effect
        self.doors = doors
        self.entrance = entrance

    def __repr__(self):
        return f'{self.name}, {self.doors}, {self.type},' \
               f' {self.x}, {self.y}, {self.effect} \n'

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def change_door_position(self, idx, direction):
        self.doors[idx] = direction

    def set_entrance(self, direction):
        self.entrance = direction

    def rotate_entrance(self):
        if self.entrance == myD.NORTH:
            self.set_entrance(myD.EAST)
            return
        if self.entrance == myD.SOUTH:
            self.set_entrance(myD.WEST)
            return
        if self.entrance == myD.EAST:
            self.set_entrance(myD.SOUTH)
            return
        if self.entrance == myD.WEST:
            self.set_entrance(myD.NORTH)
            return

    def rotate_tile(self):
        for door in self.doors:
            if door == myD.NORTH:
                self.change_door_position(self.doors.index(door), myD.EAST)
            if door == myD.EAST:
                self.change_door_position(self.doors.index(door), myD.SOUTH)
            if door == myD.SOUTH:
                self.change_door_position(self.doors.index(door), myD.WEST)
            if door == myD.WEST:
                self.change_door_position(self.doors.index(door), myD.NORTH)
