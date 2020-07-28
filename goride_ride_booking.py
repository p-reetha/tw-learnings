class Ride:
    """Ride class provides the various attributes involved in the ride"""
    def __init__(self, vehicle_category, distance, ac_service):
        self.__vehicle_category = vehicle_category
        self.__distance = distance
        self.__ac_service = ac_service

    def get_vehicle_category(self):
        return self.__vehicle_category

    def set_vehicle_category(self, new_category):
        self.__vehicle_category = new_category

    def get_distance(self):
        return self.__distance

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
    print("Vehicle categories:\nAuto - Can accommodate a maximum 3 people\nMicro - Can accommodate a maximum 4 people\nXL - Can accommodate a maximum 10 people")
    vehicle_category_var = input("Enter the vehicle category you want to book: (example:auto, micro, xl)\n")
    if vehicle_category_var == "auto":
        ac_service_var = "no"
    else:
        ac_service_var = input("If you want AC service enter 'yes' or else enter 'no'\nEnter your choice: ")
    distance_var = int(input("Enter your ride distance in kilometers: (example: 20)\n"))
    ride_object = Ride(vehicle_category_var, distance_var, ac_service_var)
    if vehicle_category_var == "auto":
        ride_object.display_auto_price_menu()
    elif vehicle_category_var == "micro":
        ride_object.display_micro_price_menu()
    else:
        ride_object.display_xl_price_menu()


ride_booking()
'''
Sample Output:
Vehicle categories:
Auto - Can accommodate a maximum 3 people
Micro - Can accommodate a maximum 4 people
XL - Can accommodate a maximum 10 people
Enter the vehicle category you want to book: (example:auto, micro, xl)
micro
If you want AC service enter 'yes' or else enter 'no'
Enter your choice: yes
Enter your ride distance in kilometers: (example: 20)
15

Category	Km range	Price with AC	Price without AC

Micro		Upto 15		Rs.12/km		Rs.14/km
Micro		15 above	Rs.10/km		Rs.12/km

'''