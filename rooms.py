class Rooms:
    def __init__(self,number,type,price):
        self.number=number
        self.type=type
        self.price=price
        self.isbooked=False
        self.guest_name=None

    def get_room_info(self):
        return f'Room {self.number} if of type {self.type} and its price is {self.price}'
    