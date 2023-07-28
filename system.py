
class Common:
    def __init__(self,Name, Address, Phone):
        self.Name = Name
        self.Address = Address
        self.Phone = Phone

class Guest(Common):
    def __init__(self, Name, Address, Phone, Guest_id, Amount_due):
        self.Guest_id = Guest_id
       
        self.__due = Amount_due
        super().__init__(Name, Address, Phone)
        
    def disply_guest(self):
        print(f'Name: {self.Name} Adreess: {self.Address} Phone: {self.Phone} Id: {self.Guest_id} ')


class Room:
    def __init__(self, Room_number, Room_type, Room_rate):
        self.Room_number = Room_number
        self.Room_type = Room_type
        self.Room_rate = Room_rate
        self.occupied = False
        self.guest_assignt = None

class Reservation:
    def __init__(self,reservation_id, guest, room, ck_in_date, ck_in_out) -> None:
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.ck_in_date = ck_in_date
        self.ck_in_out = ck_in_out


class Billing:
    