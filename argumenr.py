def bank_transfer(sender,receiver, amount):
    print(f'Transferring {amount} from {sender} to {receiver}')

bank_transfer('ram', 'sita', 500)

def book_flight(from_city, to_city):
    print(f'Booking a flight from {from_city} to {to_city}')
book_flight(to_city= 'Nepalgunj', from_city= 'Kathmandu')

def area_of_rec(l,b):
    a= l*b
    print(a)
area_of_rec(10,20)

if __name__ == '__main__':
    area_of_rec(10.20)
    print('Hello')
    print('Python')
