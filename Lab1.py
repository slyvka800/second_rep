class Park:
    location = 'Earth'

    def __init__(self, ticket_price = 0, address = 'Park Avenue', lane_length = 0):
        self.ticket_price = ticket_price
        self.address = address
        self.lane_length = lane_length

    def __del__(self):
        pass
    def __str__(self):
        return f'Park is located on the {self.address}, has total length of lanes — {self.lane_length}m' \
              f' and You can visit it by ticket — {self.ticket_price} UAH'
    @staticmethod
    def get_location():
        return Park.location

def main():
    parks_list = [Park(250, 'Golovna Street', 4950),
                  Park(300, 'Sadova Street'),
                  Park(1400, lane_length = 300)]

    for park in parks_list:
        print(park)

    print(Park.get_location())

if __name__ == "__main__":
    main()