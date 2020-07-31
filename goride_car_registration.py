import re


class Car:
    """Car class provides various details of a car"""
    def __init__(self, category, number, colour, company, model):
        self.__category = category
        self.__number = number
        self.__colour = colour
        self.__company = company
        self.__model = model

    def get_car_category(self):
        return self.__category

    def get_car_number(self):
        return self.__number

    def get_car_colour(self):
        return self.__colour

    def set_car_colour(self, new_colour):
        self.__colour = new_colour

    def get_car_company(self):
        return self.__company

    def get_car_model(self):
        return self.__model


class Driver:
    """Driver class provides the details of the car, driver/owner"""
    def __init__(self, name, age, license_number, license_validity, car_object):
        self.__name = name
        self.__age = age
        self.__license_number = license_number
        self.__license_validity = license_validity
        self.car_object = car_object

    def get_driver_name(self):
        return self.__name

    def get_driver_age(self):
        return self.__age

    def set_driver_age(self, current_age):
        self.__age = current_age

    def get_license_number(self):
        return self.__license_number

    def get_license_validity(self):
        return self.__license_validity

    def set_license_validity(self, updated_validity):
        self.__license_validity = updated_validity


def car_registration():
    driver_name_var = input("Enter the car driver/owner name: ")
    while True:
        driver_age_var = input("Enter driver age: ")
        if re.match(r"[2-9][0-9]", driver_age_var):
            break
        else:
            print("Enter age correctly")
    while True:
        license_number_var = input("Enter driving license number: ")
        if re.match(r"([A-Z]{2}[0-9]{2}(19|20)[0-9][0-9])([0-9]{7})", license_number_var):
            break
        else:
            print("Entered license number is not valid")
    while True:
        license_validity_var = input("Enter driving license validity number: ")
        if re.match(r"(0?[1-9]|[12][0-9]|3[01])[-](0?[1-9]|1[012])[-]((19|20)[0-9]{2})$", license_validity_var):
            break
        else:
            print("Entered license validity number is not valid")
    print("Car categories:\nMicro - All cars that can accommodate a maximum 4 people\nXL - All cars that can accommodate a maximum 10 people")
    while True:
        car_category_var = input("Enter your car category: (example:micro, xl)")
        if car_category_var in ['micro', 'xl']:
            break
        else:
            print("You have entered a wrong category of car")
            continue
    while True:
        car_number_var = input("Enter car number: ")
        if re.match(r"^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$", car_number_var):
            break
        else:
            print("Entered car number is not valid")
    car_colour_var = input("Enter car colour: ")
    car_company_var = input("Enter car company name: ")
    car_model_var = input("Enter car model name: ")
    car_object = Car(car_category_var, car_number_var, car_colour_var, car_company_var, car_model_var)
    driver_object = Driver(driver_name_var, driver_age_var, license_number_var, license_validity_var, car_object)
    print("\nRegistration successful !")


car_registration()
'''
Sample output:
Enter the car driver/owner name: A.Preetha
Enter driver age: 21
Enter driving license number: MH1420110062821
Enter driving license validity number: 04-12-2022
Car categories:
Micro - All cars that can accommodate a maximum 4 people
XL - All cars that can accommodate a maximum 10 people
Enter your car category: (example:micro, xl)micro
Enter car number: TN 01 PA 4554
Enter car colour: Red
Enter car company name: ford
Enter car model name: figo

Registration successful !
'''
