class Ride:
    """Ride class provides the various attributes involved in the ride"""
    def __init__(self, vehicle_category, ac_service):
        self.__vehicle_category = vehicle_category
        self.__ac_service = ac_service

    def get_vehicle_category(self):
        return self.__vehicle_category

    def set_vehicle_category(self, new_category):
        self.__vehicle_category = new_category

    def get_ac_service(self):
        return self.__ac_service

    def display_price_menu(self, vehicle_list):
        print("\nCategory\tKm Range\t\tPrice\n")
        for vehicle in vehicle_list:
            if self.__vehicle_category == vehicle.vehicle_category:
                if self.__ac_service == vehicle.ac_service:
                    print(vehicle.vehicle_category, "\t\t", vehicle.km_range, "\t\t", vehicle.price, "/km")


class GoRide:

    def __init__(self, vehicle_category, km_range, price, ac_service, max_people):
        self.vehicle_category = vehicle_category
        self.km_range = km_range
        self.price = price
        self.ac_service = ac_service
        self.max_people = max_people


auto_obj1 = GoRide("auto", "upto 15km", 10, "no", 3)
auto_obj2 = GoRide("auto", "15 - 30km", 8, "no", 3)
auto_obj3 = GoRide("auto", "30 above", 15, "no", 3)
micro_obj1 = GoRide("micro", "upto 15km", 12, "yes", 4)
micro_obj2 = GoRide("micro", "upto 15km", 14, "no", 4)
micro_obj3 = GoRide("micro", "15 above", 10, "yes", 4)
micro_obj4 = GoRide("micro", "15 above", 12, "no", 4)
xl_obj1 = GoRide("xl", "upto 15km", 14, "yes", 10)
xl_obj2 = GoRide("xl", "upto 15km", 15, "no", 10)
xl_obj3 = GoRide("xl", "15 above", 14, "yes", 10)
xl_obj4 = GoRide("xl", "15 above", 15, "no", 10)
goride_objects_list = [auto_obj1, auto_obj2, auto_obj3, micro_obj1, micro_obj2, micro_obj3, micro_obj4, xl_obj1, xl_obj2, xl_obj3, xl_obj4]


def ride_booking():
    print("Vehicle categories:\nAuto - Can accommodate a maximum 3 people\nMicro - Can accommodate a maximum 4 people\nXL - Can accommodate a maximum 10 people")
    while True:
        vehicle_category_var = input("Enter the vehicle category you want to book: (example:auto, micro, xl)\n")
        if vehicle_category_var in ['auto', 'micro', 'xl']:
            break
        else:
            print("You have entered a wrong category of vehicle")
            continue
    if vehicle_category_var == "auto":
        print("AC service is not applicable for auto")
        ac_service_var = "no"
    else:
        while True:
            ac_service_var = input("If you want AC service enter 'yes' or else enter 'no'\nEnter your choice: ")
            if ac_service_var in ['yes', 'no']:
                break
            else:
                print("You have entered wrong AC service choice")
                continue
    ride_object = Ride(vehicle_category_var, ac_service_var)
    Ride.display_price_menu(ride_object, goride_objects_list)
    while True:
        confirm_booking = input("\nIf you want to book this ride enter 'yes' or else enter 'no'\nEnter your choice: ")
        if confirm_booking in ['yes', 'no']:
            break
        else:
            print("Enter your choice correctly")
            continue
    if confirm_booking == 'yes':
        print("\nRide booked successfully!")
    else:
        pass


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

Category	Km Range		Price

micro 		 upto 15km 		 12 /km
micro 		 15 above 		 10 /km

If you want to book this ride enter 'yes' or else enter 'no'
Your choice: yes

Ride booked successfully!

'''