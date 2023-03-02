
class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []
    room: Room = Room("There's a 'creepy-looking' hospital down the road, next to a river that almost has no water running down it.", 1, None, None, None )
    room_list.append(room)
    room = Room("You're in the entrance of the abandoned hospital, it's much more creepier inside! There's a key on floor next to some broken glass.", 5, 0, 2, None)
    room_list.append(room)
    room = Room("This looks like a waiting room, but the chairs are barely holding it's form and you can see some rats here and there. Also, there's a door at the north of the room below a sign that reads 'Surgery Room'.", 3, None, None, 1)
    room_list.append(room)
    room = Room("After opening the door you're shocked by the smell of death. There's a body or what remains of it in the center of the room. It smells so bad in here!", None, 2, 4, 5)
    room_list.append(room)
    room = Room("You arrived at a bathroom, you'll pretty lucky if anything works in here. There's a flashlight near a corner.", None, None, None, 3)
    room_list.append(room)
    room = Room("It's pitch black in the room. You can't see a thing but you hear a cracking sound coming from this room.", None, 1, 3, None)
    room_list.append(room)
    print(room_list[0])
    current_room = 0
    current_room = room_list[0].description
    done = False
    while not done:
        print()
        print(current_room)
        action = input("Where will you go? ")
        next_action = action
        if next_action.lower() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                print(next_room.description)


main()
