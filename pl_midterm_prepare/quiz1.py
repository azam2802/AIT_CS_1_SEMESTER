seats = [i for i in range(100)]
reserved_seats = []

def reserv(seat):
    if seat in seats:
        if seat in reserved_seats:
            return f"Seat {seat} has been already reserved"
        else:
            reserved_seats.append(seat)
            return f"Seat {seat} was reserved successfully"
    return f"Seat {seat} is not found"

def delete_reserv(seat):
    if seat in seats:
        if seat in reserved_seats:
            reserved_seats.remove(seat)
            return f"Reservstion for {seat} was successfully cancelled"
        else:
            return f"Seat {seat} is not reserved"
    return f"Seat {seat} is not found"
    
def show_reserved():
    return reserved_seats

