def total_time(t1, t2):
    if t1.minute + t2.minute >= 60:
        return str(t1.hour + t2.hour + 1) + " Hours " + str(t1.minute + t2.minute - 60) + " Minutes"


def total_time_in_minutes(t1, t2):
    if t1.minute + t2.minute >= 60:
        return str(((t1.hour + t2.hour + 1) * 60) + (t1.minute + t2.minute - 60)) + " Minutes"


def time_difference(t1, t2):
    if t1.minute < t2.minute:
        return str(t1.hour + t2.hour - 1) + " Hours " + str((t1.minute + 60) - t2.minute) + " Minutes"
    else:
        return str(t1.hour - t2.hour) + " Hours " + str(t1.minute - t2.minute) + " Minutes"


class Time:

    def __init__(self,hour,minute):
        self.hour = hour
        self.minute = minute

    def display_time(self):
        return self.hour + " Hours " + self.minute + "Minutes"


time_obj1 = Time(5, 50)
time_obj2 = Time(2, 15)
print("The total time is {}".format(total_time(time_obj1, time_obj2)))
print("The total time in minutes is {}".format(total_time_in_minutes(time_obj1, time_obj2)))
print("The time difference is {}".format(time_difference(time_obj1, time_obj2)))

