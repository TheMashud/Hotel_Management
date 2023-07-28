import datetime
class Common:
    def __init__(self,Name, Address, Phone):
        self.Name = Name
        self.Address = Address
        self.Phone = Phone

class Guest(Common):
    def __init__(self, Name, Address, Phone, Guest_id, Amount_due):
        self.Guest_id = Guest_id
       
        self.amount_due = Amount_due
        super().__init__(Name, Address, Phone)
        
    def disply_guest(self):
        print(f'Name: {self.Name} Adreess: {self.Address} Phone: {self.Phone} Id: {self.Guest_id} ')


class Room:
    def __init__(self, Room_number, Room_type, Room_rate):
        self.Room_number = Room_number
        self.Room_type = Room_type
        self.Room_rate = Room_rate
        self.is_booking = False
        self.guest_assigned = None

class Reservation:
    def __init__(self,reservation_id, guest, room, ck_in_date, ck_out_date) -> None:
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.ck_in_date = ck_in_date
        self.ck_out_date = ck_out_date


class Billing:
    def __init__(self, bill_id, guest, room, total_amount) -> None:
        self.bill_id = bill_id
        self.guest = guest
        self.room = room
        self.total_amont = total_amount
        self.is_paid = False

class Hotel(Common):
    def __init__(self, Name, Address, Phone):
        self.available_rooms = []
        self.guests = []
        self.reservation = []
        self.bills = []
        super().__init__(Name, Address, Phone)

    def check_room_availability(self, room_number):
        for room in self.available_rooms:
            if room.room_number == room_number:
                return room.is_booking
            return False
        
    def create_reservation(self, reservation_id, guest, room, ck_in_date, ck_in_out):
        reservation = Reservation(reservation_id, guest, room, ck_in_date, ck_in_out)
        room.is_booking = True
        room.guest_assigned = guest
        self.reservation.append(reservation)

    def Cheak_out_guest(self, guest):
        for room in self.available_rooms:
            if room.guest_assigned == guest:
                room.is_booking = False
                room.guest_assigned = None
                break

    def generate_bill(self, guest, room):
        total_amount = room.Room_rate * (guest.ck_out_date - guest.ck_in_date).days
        guest.amount_due += total_amount
        bill = Billing(len(self.bills) + 1, guest, room, total_amount)
        self.bills.append(bill)

    def update_guest_information(self, guest, name, address, number):
        guest.name = name
        guest.address = address
        guest.number = number

class Staff:
    pass
        
