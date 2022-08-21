class message:
    def __init__(self, Company='', Location='', Qualification='', Experience='', Batch='', Salary='', Apply=''):
        self.Company = Company.strip()
        self.Location = Location.strip()
        self.Qualification = Qualification.strip()
        self.Experience = Experience.strip()
        self.Batch = Batch.strip()
        self.Salary = Salary.strip()
        self.Apply = Apply.strip()

    def display(self):
        print(self.Company)
        print(self.Location)
        print(self.Qualification)
        print(self.Experience)
        print(self.Batch)
        print(self.Salary)
        print(self.Apply)
        print("-----------------------------------------------------------")
