class Employee:
    def __init__(self, name, emp_id): # Konstruktør som tar name og emp_id som argumenter.
        self._name = name # En privat variabel for å lagre navnet til en ansatt.
        self._emp_id = emp_id # En privat variabel for å lagre id til en ansatt.
        self._salaries = [] # En privat liste for å holde oversikt over månedlig lønn for hver ansatt.

    @property
    def name(self): # En getter for å hente navnet til en ansatt.
        return self._name
    
    @name.setter
    def name(self, new_name): # En setter for å endre navnet til en ansatt.
        self._name = new_name

    @property
    def emp_id(self): # En getter for å hente id til en ansatt.
        return self._emp_id
    
    @property
    def salaries(self): # En getter for å hente lønn til en ansatt.
        return self._salaries
    
    def add_salary(self, salary_amount): # En metode for å legge til lønn til en ansatt.
        self._salaries.append(salary_amount) # Legger til lønn til en ansatt i listen _salaries.

    def print_salaries(self):
        print(f"{self.name}\nID: {self.emp_id}\nSalary per month: {self.salaries}\n") # Printer ut navn, id og lønn til en ansatt.

class SalaryEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary): # Konstruktør som tar name, emp_id og monthly_salary som argumenter.
        super().__init__(name, emp_id) # Kaller konstruktøren til superklassen.
        self._monthly_salary = monthly_salary # En privat variabel for å lagre månedlig lønn til en ansatt.

    @property
    def monthly_salary(self): # En getter for å hente månedlig lønn til en ansatt.
        return self._monthly_salary 
    
    def calculate_payroll(self): # En metode for å beregne lønn til en ansatt.
        payroll = self._monthly_salary # Setter lønn til en ansatt lik månedlig lønn.
        self.add_salary(payroll) # Legger til lønn til en ansatt i listen _salaries.
        return payroll
    
class HourlyEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate): # Konstruktør som tar name, emp_id og hourly_rate som argumenter.
        super().__init__(name, emp_id) # Kaller konstruktøren til superklassen.
        self._hourly_rate = hourly_rate # En privat variabel for å lagre timelønn til en ansatt.
        self._hours_worked = 0

    @property
    def hourly_rate(self): # En getter for å hente timelønn til en ansatt.
        return self._hourly_rate
    
    @property
    def hours_worked(self): # En getter for å hente antall timer en ansatt har jobbet.
        return self._hours_worked
    
    def add_hours(self, hours):
        self._hours_worked = hours

    def calculate_payroll(self): # En metode for å beregne lønn til en ansatt.
        payroll = self._hourly_rate * self._hours_worked # Beregner lønn til en ansatt.
        self.add_salary(payroll)
        return payroll
    
class CommissionEmployee(SalaryEmployee): 
    def __init__(self, name, emp_id, monthly_salary, commission): # Konstruktør som tar name, emp_id, monthly_salary og commission som argumenter.
        super().__init__(name, emp_id, monthly_salary) # Kaller konstruktøren til superklassen.
        self._commission = commission # En privat variabel for å lagre provisjon til en ansatt.

    @property
    def commission_rate(self): # En getter for å hente provisjon til en ansatt.
        return self._commission
    
    def calculate_payroll(self):
        payroll = self._monthly_salary + self._commission # Beregner lønn til en ansatt.
        self.add_salary(payroll) # Legger til lønn til en ansatt i listen _salaries.
        return payroll
    
    
# Hovedprogram

# Create one employee per type
salary_employee = SalaryEmployee("Alice", 1, 3000)
hourly_employee = HourlyEmployee("Bob", 2, 20)
commission_employee = CommissionEmployee("Charlie", 3, 2700, 500)

# Simulate payroll calculation for three months
for month in range(1, 4):
    print(f"Month {month}:")
   
    # For hourly employee, assume they worked 160 hours each month
    hourly_employee.add_hours(160)
   
    # Calculate payroll for each employee
    for employee in [salary_employee, hourly_employee, commission_employee]:
        payroll = employee.calculate_payroll()
        print(f"{employee.name} (ID: {employee.emp_id}) - Payroll: {payroll:.2f} NOK")

    print()

# Display the salaries for each employee
for employee in [salary_employee, hourly_employee, commission_employee]:
    employee.print_salaries()

    

