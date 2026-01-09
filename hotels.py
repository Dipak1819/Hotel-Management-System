from rooms import StandardRoom,DeluxeRoom,SuiteRoom
from payment import Payment
import json

def decorator_function(func1):
    def wrapper_function(self,type1):
        found=func1(self,type1)
        if found:
            for v in self.rooms.values():
                if v.type==type1:
                    print(f"  Balcony: {v.hasbalcony}")
                    print(f"  Lounge:  {v.haslounge}")
                    print(f"  Bar:     {v.hasbar}")
        return found
    return wrapper_function
        

class Hotel:
    def __init__(self,name):
        self.name=name
        self.filename='database.json'
        self.rooms={}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename,'r') as file:
                content=json.load(file)
        
            for j, v in content.items():
                i=int(j)
                if v['room_type']=='Standard':
                    self.rooms[i]=StandardRoom(
                        v['room_number']
                    )
                elif v['room_type']=='Deluxe':
                    self.rooms[i]=DeluxeRoom(
                        v['room_number']
                    )
                elif v['room_type']=='Suite':
                    self.rooms[i]=SuiteRoom(
                        v['room_number']
                    )
                self.rooms[i].isbooked=v['book status']
                self.rooms[i].guest_name=v['guest']
        
        except json.JSONDecodeError:  # ← Add this!
            print("Empty or corrupted file, starting fresh")
            self.rooms = {}

        except Exception as e:
            print(f"cant load file error: {e}")
            self.rooms={}

               

    def save_file(self):
        try:
            data={}
            for i, v in self.rooms.items():
                if isinstance(v,StandardRoom):
                    room_type="Standard"
                elif isinstance(v,DeluxeRoom):
                    room_type="Deluxe"
                else:
                    room_type="Suite"

                data[i]={
                    "room_number":i,
                    "room_type":room_type,
                    "room_price":v.price,
                    "book status":v.isbooked,
                    "guest":v.guest_name,
                    "has_lounge":v.haslounge,
                    "type":v.type
                }
                
            with open(self.filename,'w') as file:
                json.dump(data,file,indent=4)

        except Exception as e:
                print(f'the exception generated: {e}')

    
    def add_rooms(self,room_number,type):
        room_number=int(room_number)
        if room_number in self.rooms:
            print("rooms is already added")
        else:
            if type.lower()=='standard':
                self.rooms[room_number]=StandardRoom(room_number)
            elif type.lower()=='deluxe':
                self.rooms[room_number]=DeluxeRoom(room_number)
            else:
                self.rooms[room_number]=SuiteRoom(room_number)

        self.save_file()
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
                    self.save_file()
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
                self.save_file()
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

    def delete_rooms(self,num):
        if num in self.rooms:
            del self.rooms[num]
            print('room deleted successfully')
            self.save_file()
        else:
            print('room doesnt exist in the database')
            return

    @decorator_function  
    def search_room_by_type(self, type1):
        flag= False
        for v in self.rooms.values():
            if v.type==type1:
                print(v.get_room_info())
                flag=True
        
        if not flag:
            print("no room of given type found")
        return flag
        

            