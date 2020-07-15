def large_planet(*planet_list):
    diameter_list = []
    for planet in planet_list:
        diameter_list.append(planet.diameter)
    large = max(diameter_list)
    for planet in planet_list:
        if planet.diameter == large:
            return planet.name


class Planet:

    def __init__(self,name,diameter,moons,days):
        self.name = name
        self.diameter = diameter
        self.moons = moons
        self.days = days

    def calc_radius(self):
        return self.diameter // 2

    def days_count(self):
        days_list = list(self.days.split(" "))
        if days_list[1] == "days":
            self.days = days_list[0]
        else:
            self.days = int(int(days_list[0])*365.25)
        return self.days


planet1_obj = Planet("Mercury", 4879, 0, "88 days")
planet2_obj = Planet("Venus", 12100, 0, "225 days")
planet3_obj = Planet("Earth", 12755, 1, "365 days")
planet4_obj = Planet("Mars", 6786, 2, "687 days")
planet5_obj = Planet("Jupiter", 142800, 79, "12 earth years")
planet6_obj = Planet("Saturn", 120537, 82, "29.5 earth years")
planet7_obj = Planet("Uranus", 51819, 27, "84 earth years")
planet8_obj = Planet("Neptune", 49529, 14, "165 earth years")
print("The radius of {} is {}".format(planet8_obj.name, Planet.calc_radius(planet8_obj)))
print("The number of days in {} is {}".format(planet5_obj.name, Planet.days_count(planet5_obj)))
print("The largest planet is {}".format(large_planet(planet1_obj, planet2_obj, planet3_obj, planet4_obj, planet5_obj, planet6_obj, planet7_obj, planet8_obj)))


