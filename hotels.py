from rooms import StandardRoom,DeluxeRoom,SuiteRoom
from payment import Payment
from datetime import datetime
import json

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
                
                # Load bookings if they exist
                if 'bookings' in v:
                    for booking in v['bookings']:
                        guest = booking['guest']
                        checkin = datetime.strptime(booking['checkin'], '%Y-%m-%d').date()
                        checkout = datetime.strptime(booking['checkout'], '%Y-%m-%d').date()
                        self.rooms[i].bookings.append((guest, checkin, checkout))
                
                # Update current status
                self.rooms[i].update_current_status()
        
        except FileNotFoundError:
            print("No existing database found, starting fresh")
            self.rooms = {}
        
        except json.JSONDecodeError:
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

                # Convert bookings to JSON-serializable format
                bookings_list = []
                for guest, checkin, checkout in v.bookings:
                    bookings_list.append({
                        'guest': guest,
                        'checkin': checkin.strftime('%Y-%m-%d'),
                        'checkout': checkout.strftime('%Y-%m-%d')
                    })

                data[i]={
                    "room_number":i,
                    "room_type":room_type,
                    "room_price":v.price,
                    "bookings": bookings_list,
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

    def book_rooms(self, room_number, username, indate, outdate):
        """Book a room for specific dates"""
        if room_number not in self.rooms:
            print("No room exists for given room number")
            return False
        
        try:
            # Convert string dates to date objects
            checkin_date = datetime.strptime(indate, '%Y-%m-%d').date()
            checkout_date = datetime.strptime(outdate, '%Y-%m-%d').date()
            
            # Validate dates
            if checkin_date >= checkout_date:
                print("Check-out date must be after check-in date")
                return False
            
            if checkin_date < datetime.now().date():
                print("Cannot book for past dates")
                return False
            
            # Check if room is available for these dates
            if not self.rooms[room_number].is_available(checkin_date, checkout_date):
                print(f"Room {room_number} is not available for the dates {indate} to {outdate}")
                print("Conflicting bookings exist.")
                return False
            
            # Add the booking
            self.rooms[room_number].add_booking(username, checkin_date, checkout_date)
            self.save_file()
            print(f"Room {room_number} successfully booked for {username} from {indate} to {outdate}")
            return True
            
        except ValueError as e:
            print(f"Invalid date format. Please use YYYY-MM-DD format. Error: {e}")
            return False

    def check_out(self, room_number, guest_name=None):
        """Check out from a room - removes current or specific booking"""
        if room_number not in self.rooms:
            print(f'Please enter a valid room number')
            return False
        
        room = self.rooms[room_number]
        
        if not room.bookings:
            print("The room has no bookings to check out")
            return False
        
        # If guest name provided, find and remove that specific booking
        if guest_name:
            today = datetime.now().date()
            removed = False
            for booking in room.bookings[:]:  # Create a copy to iterate
                if booking[0] == guest_name and booking[1] <= today <= booking[2]:
                    room.remove_booking(guest_name, booking[1])
                    removed = True
                    break
            
            if removed:
                print(f"Checked out {guest_name} from room {room_number} successfully")
                self.save_file()
                return True
            else:
                print(f"No active booking found for {guest_name} in room {room_number}")
                return False
        
        # If no guest name, remove the current active booking
        today = datetime.now().date()
        for booking in room.bookings[:]:
            guest, checkin, checkout = booking
            if checkin <= today < checkout:
                room.remove_booking(guest, checkin)
                print(f"Checked out {guest} from room {room_number} successfully")
                self.save_file()
                return True
        
        print("No active booking found for check-out")
        return False

    def view_room_bookings(self, room_number):
        """View all bookings for a specific room"""
        if room_number not in self.rooms:
            print(f'Room {room_number} does not exist')
            return
        
        room = self.rooms[room_number]
        print(f"\n--- Bookings for Room {room_number} ({room.type}) ---")
        
        if not room.bookings:
            print("No bookings for this room")
            return
        
        today = datetime.now().date()
        for i, (guest, checkin, checkout) in enumerate(room.bookings, 1):
            status = "ACTIVE" if checkin <= today < checkout else "UPCOMING" if checkin > today else "PAST"
            print(f"{i}. Guest: {guest}")
            print(f"   Check-in:  {checkin}")
            print(f"   Check-out: {checkout}")
            print(f"   Status: {status}")
            print()

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

    def search_room_by_type(self, type1):
        flag= False
        for v in self.rooms.values():
            x='  '
            if v.type==type1:
                print(v.get_room_info())
                print(f"{x}Has Balcony: {v.hasbalcony}")
                print(f"{x}Has Lounge: {v.haslounge}")
                print(f"{x}Has Bar: {v.hasbar}")
                flag=True
        
        if not flag:
            print("no room of given type found")
        return flag
    
    def search_by_price_range(self, min, max):
        flag=False
        for v in self.rooms.values():
            if v.price>=min and v.price<=max:
                print(v.get_room_info())
                print(f"  Has Balcony: {v.hasbalcony}")
                print(f"  Has Lounge: {v.haslounge}")
                print(f" Has Bar: {v.hasbar}")
                flag=True

        if not flag:
            print('room not found in the given price range')
            return

