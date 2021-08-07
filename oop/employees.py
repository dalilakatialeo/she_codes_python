class Employee:
    #attr - name, role, pay_level
    #method - work, get_name, get_role

    def __init__(self, name, salary, phone_number, start_date):
        self.name = name
        self.salary = salary
        self.phone_number = phone_number
        self.start_date = start_date

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)

    def get_contact_details(self):
        return (self.name, self.phone_number)

#create an object of this class

employee_1 = Employee("Fran", 78000, "0437845266", "1st June 2020")
print(employee_1.get_employment_details())
