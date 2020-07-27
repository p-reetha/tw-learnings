class Ride:
    """Ride class provides the different attributes of the ride"""
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

    def display_auto_price_menu(self):
        print("\nCategory\tKm range\tPrice with AC\tPrice without AC\n")
        print("Auto\t\tUpto 15\t\tRs.10/km\t\tNA")
        print("Auto\t\t15 - 30\t\tRs.8/km\t\t\tNA")
        print("Auto\t\t30 above\tRs.15/km\t\tNA")

    def display_micro_price_menu(self):
        print("\nCategory\tKm range\tPrice with AC\tPrice without AC\n")
        print("Micro\t\tUpto 15\t\tRs.12/km\t\tRs.14/km")
        print("Micro\t\t15 above\tRs.10/km\t\tRs.12/km")

    def display_xl_price_menu(self):
        print("\nCategory\tKm range\tPrice with AC\tPrice without AC\n")
        print("XL\t\t\tUpto 15\t\tRs.14/km\t\tRs.15/km")
        print("XL\t\t\t15 above\tRs.14/km\t\tRs.15/km")


def ride_booking():
    print("Car categories:\nAuto - All cars that can accommodate a maximum 3 people\nMicro - All cars that can accommodate a maximum 4 people\nXL - All cars that can accommodate a maximum 10 people")
    car_category_var = input("Enter the car category you want to book: (example:auto, micro, xl)\n")
    if car_category_var == "auto":
        ac_service_var = "no"
    else:
        ac_service_var = input("If you want AC service enter 'yes' or else enter 'no'\nEnter your choice: ")
    km_var = int(input("Enter your ride distance in kilometers: (example: 20)\n"))
    ride_object = Ride(car_category_var, km_var, ac_service_var)
    if car_category_var == "auto":
        ride_object.display_auto_price_menu()
    elif car_category_var == "micro":
        ride_object.display_micro_price_menu()
    else:
        ride_object.display_xl_price_menu()


ride_booking()
'''
Sample Output:
Car categories:
Auto - All cars that can accommodate a maximum 3 people
Micro - All cars that can accommodate a maximum 4 people
XL - All cars that can accommodate a maximum 10 people
Enter the car category you want to book: (example:auto, micro, xl)
micro
If you want AC service enter 'yes' or else enter 'no'
Enter your choice: yes
Enter your ride distance in kilometers: (example: 20)
15

Category	Km range	Price with AC	Price without AC

Micro		Upto 15		Rs.12/km		Rs.14/km
Micro		15 above	Rs.10/km		Rs.12/km

'''