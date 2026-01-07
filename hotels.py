from rooms import Rooms

class Hotel:
    def __init__(self,name):
        self.name=name
        self.rooms={}

    def add_rooms(self,room_number,type,price):
        if room_number in self.rooms:
            print("rooms is already added")
        else:
            self.rooms[room_number]= Rooms(room_number,type,price)
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
            if self.rooms[room_number].booked==True:
                self.rooms[room_number].booked=False
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
                print('/n')
        else:
            print('no room to show')
