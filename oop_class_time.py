class Time:

    def __init__(self,t1hour,t1min,t2hour,t2min):
        self.t1hour = t1hour
        self.t1min = t1min
        self.t2hour = t2hour
        self.t2min = t2min
        self.minutes = self.t1min + self.t2min
        self.hours = self.t1hour + self.t2hour
        if self.minutes >= 60:
            self.hours = 1 + self.hours
            self.minutes = self.minutes - 60

    def total_time(self):
        return str(self.hours)+" Hours", str(self.minutes)+" Minutes"

    def time_diff(self):
        return str(self.t1hour - self.t2hour)+" Hours", str(self.t1min - self.t2min)+" Minutes"

    def total_time_in_minutes(self):
        return str((self.hours * 60) + self.minutes)+" Minutes"


while True:
    try:
        first_time_hour = int(input("Enter the first time\'s hours: "))
        first_time_minute = int(input("Enter the first time\'s minutes: "))
        second_time_hour = int(input("Enter second time\'s hours: "))
        second_time_minute = int(input("Enter second time\'s minute: "))

    except:
        print("You have not entered a number\nEnter carefully!")
        continue

    t1 = Time(first_time_hour,first_time_minute,second_time_hour,second_time_minute)
    print("Total time is ",Time.total_time(t1))
    print("Time difference is ",Time.time_diff(t1))
    print("Total time in minutes: ",Time.total_time_in_minutes(t1))
    break




