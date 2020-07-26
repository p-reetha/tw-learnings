class Customer:
    """Customer class provides the details of the ride"""
    def __init__(self, category, km_range, ac_service):
        self.__category = category
        self.__km_range = km_range
        self.__ac_service = ac_service

    def get_category(self):
        return self.__category

    def set_category(self, new_category):
        self.__category = new_category

    def get_km_range(self):
        return self.__km_range

    def get_ac_service(self):
        return self.__ac_service


def calc_auto_ride_cost(km):
    if km <= 15:
        return km * 10
    elif km < 30:
        return km * 8
    else:
        return km * 15


def calc_micro_ride_cost(km, ac):
    if ac == "yes":
        if km <= 15:
            return km * 12
        else:
            return km * 10
    else:
        if km <= 15:
            return km * 14
        else:
            return km * 12


def calc_xl_ride_cost(km, ac):
    if ac == "yes":
        if km <= 15:
            return km * 14
        else:
            return km * 14
    else:
        if km <= 15:
            return km * 15
        else:
            return km * 15


def menu():
    print("\nCategory\tKm range\tPrice with AC\tPrice without AC\n")
    print("Auto\t\tUpto 15\t\tRs.10/km\t\tNA")
    print("Auto\t\t15 - 30\t\tRs.8/km\t\t\tNA")
    print("Auto\t\t30 above\tRs.15/km\t\tNA")
    print("Micro\t\tUpto 15\t\tRs.12/km\t\tRs.14/km")
    print("Micro\t\t15 above\tRs.10/km\t\tRs.12/km")
    print("XL\t\t\tUpto 15\t\tRs.14/km\t\tRs.15/km")
    print("XL\t\t\t15 above\tRs.14/km\t\tRs.15/km")


def ride_booking():
    print("Car categories:\nAuto - All cars that can accommodate a maximum 3 people\nMicro - All cars that can accommodate a maximum 4 people\nXL - All cars that can accommodate a maximum 10 people")
    car_category_var = input("Enter the car category you want to book: (example:auto, micro, xl)\n")
    km_var = int(input("Enter your ride distance in kilometers: (example: 20)\n"))
    if car_category_var == "auto":
        ac_service_var = "no"
    else:
        ac_service_var = input("If you want AC service enter 'yes' or else enter 'no'\nEnter your choice: ")
    menu()
    if car_category_var == "auto":
        ride_cost = calc_auto_ride_cost(km_var)
    elif car_category_var == "micro":
        ride_cost = calc_micro_ride_cost(km_var, ac_service_var)
    else:
        ride_cost = calc_xl_ride_cost(km_var, ac_service_var)
    print("\n\nRide cost: {}\n".format(ride_cost))
    booking_confirm = input("If you want to book this ride enter 'yes' or else enter 'no': ")
    if booking_confirm == "yes":
        customer_object = Customer(car_category_var, km_var, ac_service_var)
        print("\nRide successfully booked !")
    else:
        pass


ride_booking()
'''
Sample Output:
Car categories:
Auto - All cars that can accommodate a maximum 3 people
Micro - All cars that can accommodate a maximum 4 people
XL - All cars that can accommodate a maximum 10 people
Enter the car category you want to book: (example:auto, micro, xl)
micro
Enter your ride distance in kilometers: (example: 20)
16
If you want AC service enter 'yes' or else enter 'no'
Enter your choice: yes

Category	Km range	Price with AC	Price without AC

Auto		Upto 15		Rs.10/km		NA
Auto		15 - 30		Rs.8/km			NA
Auto		30 above	Rs.15/km		NA
Micro		Upto 15		Rs.12/km		Rs.14/km
Micro		15 above	Rs.10/km		Rs.12/km
XL          Upto 15		Rs.14/km		Rs.15/km
XL			15 above	Rs.14/km		Rs.15/km


Ride cost: 160

If you want to book this ride enter 'yes' or else enter 'no': yes

Ride successfully booked !
'''