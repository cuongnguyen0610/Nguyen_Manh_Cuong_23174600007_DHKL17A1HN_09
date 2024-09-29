class Date:
    def __init__(self, day=1, month=1, year=1900):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next(self):
        days_in_month = [31, 28 + (1 if self.is_leap_year() else 0), 31, 30, 31, 30, 
                         31, 31, 30, 31, 30, 31]
        
        self.day += 1
        
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            
            if self.month > 12:
                self.month = 1
                self.year += 1

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)


class Employee:
    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date  
        self.start_date = start_date  

    def display_info(self):
        print(f"Name: {self.name}")
        print("Birth Date: ", end="")
        self.birth_date.display()
        print("Start Date: ", end="")
        self.start_date.display()


birth_date = Date(15, 5, 1990)
start_date = Date(1, 1, 2020)

employee = Employee("Nguyen Van A", birth_date, start_date)
employee.display_info()
