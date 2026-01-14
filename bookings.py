class Rooms:
    def __init__(self,number,type,price):
        self.number=number
        self.type=type
        self.price=price
        self.bookings=[]  # List of bookings: [(guest_name, checkin, checkout), ...]
        self.isbooked=False
        self.guest_name=None

    def get_room_info(self):
        status = "BOOKED" if self.isbooked else "AVAILABLE"
        guest = self.guest_name if self.guest_name else "None"
        booking_info = ""
        if self.bookings:
            booking_info = f"\n  Upcoming Bookings: {len(self.bookings)}"
        return (
            f"Room {self.number}\n"
            f"  Type:   {self.type}\n"
            f"  Price:  {self.price}\n"
            f"  Status: {status}\n"
            f"  Guest:  {guest}"
            f"{booking_info}"
        )
    
    def is_available(self, checkin_date, checkout_date):
        """Check if room is available for the given date range"""
        for booking in self.bookings:
            guest, existing_checkin, existing_checkout = booking
            # Check for overlap: new booking overlaps if it starts before existing ends 
            # AND ends after existing starts
            if checkin_date < existing_checkout and checkout_date > existing_checkin:
                return False
        return True
    
    def add_booking(self, guest_name, checkin, checkout):
        """Add a booking to the room"""
        self.bookings.append((guest_name, checkin, checkout))
        self.bookings.sort(key=lambda x: x[1])  # Sort by check-in date
        # Update current status if this booking is active
        self.update_current_status()
    
    def remove_booking(self, guest_name, checkin):
        """Remove a specific booking"""
        self.bookings = [b for b in self.bookings if not (b[0] == guest_name and b[1] == checkin)]
        self.update_current_status()
    
    def update_current_status(self):
        """Update the current isbooked status and guest_name based on today's date"""
        from datetime import datetime
        today = datetime.now().date()
        
        # Check if any booking is currently active
        for guest, checkin, checkout in self.bookings:
            if checkin <= today < checkout:
                self.isbooked = True
                self.guest_name = guest
                return
        
        # No active booking
        self.isbooked = False
        self.guest_name = None

class StandardRoom(Rooms):
    def __init__(self, number):
        super().__init__(number,"Standard",300)
        self.hasbalcony='Yes'
        self.haslounge='No'
        self.hasbar='No'

class DeluxeRoom(Rooms):
    def __init__(self, number):
        super().__init__(number, "Deluxe",500)
        self.hasbalcony='Yes'
        self.haslounge='Yes'
        self.hasbar='No'

class SuiteRoom(Rooms):
    def __init__(self,number):
        super().__init__(number,'Suite',700)
        self.hasbalcony='Yes'
        self.haslounge='Yes'
        self.hasbar='Yes'