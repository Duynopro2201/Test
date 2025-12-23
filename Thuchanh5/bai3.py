class Employee:
    def __init__(self, name, base_salary=0):
        self.name = name
        self.base_salary = base_salary

    def calc_salary(self):
        return self.base_salary

class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, allowance):
        super().__init__(name, base_salary)
        self.allowance = allowance

    def calc_salary(self):
        return super().calc_salary() + self.allowance

class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calc_salary(self):
        return self.hours * self.rate

employees = [
    FullTimeEmployee("Tú", 10_000_000, 2_000_000),
    FullTimeEmployee("Hiếu", 12_000_000, 1_500_000),
    PartTimeEmployee("Lộc", 120, 80_000),
    PartTimeEmployee("Dũng", 100, 100_000),
    FullTimeEmployee("Duy", 15_000_000, 3_000_000),
]

total_salary = sum(emp.calc_salary() for emp in employees)
print("Tổng quỹ lương:", total_salary)

top_3 = sorted(
    employees,
    key=lambda e: e.calc_salary(),
    reverse=True
)[:3]

print("\nTop 3 lương cao nhất:")
for emp in top_3:
    print(f"{emp.name}: {emp.calc_salary():,}")
