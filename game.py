"""Implements classes for the game"""
class Room:
    """Class Room"""
    def __init__(self,name) -> None:
        """Constructs an object of a room
        """
        self.__name = name
        self.__description =''
        self.__lst = [None,None,None,None]
        self.__character = None
        self.__item = None
    
    def set_description(self,description):
        """Sets the description of the room"""
        self.__description = description
    
    def link_room(self,room,vector):
        """Links the rooms between themselves"""
        if vector == 'west':
            self.__lst[0] = room
        if vector == 'north':
            self.__lst[1] = room
        if vector == 'east':
            self.__lst[2] = room
        if vector == 'south':
            self.__lst[3] = room
    
    def set_character(self,character):
        """Places character into the room"""
        self.__character = character
    
    def set_item(self,item):
        """Places the item in the room"""
        self.__item = item
    
    def get_details(self):
        """Gets details about the room"""
        print(self.__name)
        print('--------------------')
        print(self.__description)
        i = 0
        for room in self.__lst:
            if room is not None:
                if i == 0:
                    print(self.__lst[i].__name, ' is west')
                if i == 1:
                    print(self.__lst[i].__name, ' is north')
                if i == 2:
                    print(self.__lst[i].__name, ' is east')
                if i == 3:
                    print(self.__lst[i].__name, ' is south')
            i +=1
        if self.__item is not None:
            print('The [',self.__item.get_name(),'] is here - ',self.__item.describe())
        print()
    def get_character(self):
        """Gets the character, whcih is in the room"""
        return self.__character

    def move(self,command):
        """Moves the user from one place to another"""
        if command == 'west':
            return self.__lst[0]
        if command == 'north':
            return self.__lst[1]
        if command == 'east':
            return self.__lst[2]
        if command == 'south':
            return self.__lst[3]
        return None

    def character(self,value):
        """Sets the value to the character"""
        self.__character = value
    
    def get_item(self):
        """Returns the item"""
        return self.__item

class Enemy:
    """Class enemy - bad characters"""
    def __init__(self,name,description) -> None:
        """Constructs an object of type Enemy"""
        self.__name = name
        self.__description = description
        self.__conversation = ''
        self.__weakness = None
        self.__defeated = 0

    def set_conversation(self,conversation):
        """Sets conversation to the character"""
        self.__conversation = conversation
    
    def set_weakness(self,weakness):
        """Sets the weakness of the enemy"""
        self.__weakness = weakness

    def describe(self):
        """Describes an enemy"""
        print(self.__name, ' is here')
        print(self.__description)
    
    def talk(self):
        """Returns the conversation of the character"""
        print('[',self.__name,' says]:', self.__conversation)

    def fight(self,fight_with):
        """Fight between user and enemy"""
        if self.__weakness == fight_with:
            self.__defeated +=1
            return True
        return False
    
    def get_defeated(self):
        """The condition of defeat"""
        return self.__defeated


class Item:
    """Class of an item"""
    def __init__(self,name) -> None:
        """Constructs an item"""
        self.__name = name
        self.__description = ''
    
    def set_description(self,description):
        """Describes an item"""
        self.__description = description
    
    def get_name(self):
        """Returns the name of the item"""
        return self.__name
    
    def describe(self):
        """Returns the description of an item"""
        return self.__description