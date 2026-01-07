from rooms import StandardRoom,DeluxeRoom,SuiteRoom

class Hotel:
    def __init__(self,name):
        self.name=name
        self.rooms={}

    def add_rooms(self,room_number,type):
        if room_number in self.rooms:
            print("rooms is already added")
        else:
            if type.lower()=='standard':
                self.rooms[room_number]=StandardRoom(room_number)
            elif type.lower()=='deluxe':
                self.rooms[room_number]=DeluxeRoom(room_number)
            else:
                self.rooms[room_number]=SuiteRoom(room_number)
            
        print("room added successfully")

    def book_rooms(self,room_number,username):
        if room_number in self.rooms:
            if self.rooms[room_number].isbooked==False: 
                self.rooms[room_number].number=room_number
                self.rooms[room_number].isbooked=True
                self.rooms[room_number].guest_name=username
            else:
                print(f'room {room_number} is already booked')
        else:
            print("please enter a valid room number")

    def check_out(self,room_number):
        if room_number in self.rooms:
            if self.rooms[room_number].isbooked==True:
                self.rooms[room_number].isbooked=False
                self.rooms[room_number].guest_name=None
                print("room checked out successfully")
            else:
                print("the room is not booked to check out")
        else:
            print(f'Please enter a valid room number')

    def list_rooms(self):
        if self.rooms:
            for i in self.rooms:
                print(self.rooms[i].get_room_info())
        else:
            print('no room to show')
