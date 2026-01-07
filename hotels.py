from rooms import StandardRoom,DeluxeRoom,SuiteRoom
from payment import Payment
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
                num_nights=int(input('How many nights you want to book the room for: \n'))
                ibill=num_nights*(self.rooms[room_number].price)
                x=input('do you want to proceed with the payment {Y/N):  \n')
                if x.lower()=='y':
                    r=Payment(ibill,username)
                    r.get_final_bill()
                    print('Your room is booked successfully !!')
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
