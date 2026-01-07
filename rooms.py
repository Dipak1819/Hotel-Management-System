class Rooms:
    def __init__(self,number,type,price):
        self.number=number
        self.type=type
        self.price=price
        self.isbooked=False
        self.guest_name=None

    def get_room_info(self):
        status = "BOOKED" if self.isbooked else "AVAILABLE"
        guest = self.guest_name if self.guest_name else "None"
        return (
            f"Room {self.number}\n"
            f"  Type:   {self.type}\n"
            f"  Price:  {self.price}\n"
            f"  Status: {status}\n"
            f"  Guest:  {guest}"
        )

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

    