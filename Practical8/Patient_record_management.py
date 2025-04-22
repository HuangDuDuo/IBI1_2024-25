name=input('Input name here: ')
age=input('Input age here: ')
date_of_latest_admission=input('Input date of latest admission here: ')
medical_history=input('Input medical history here: ')
class Patients:
    def __init__(self,name,age,date_of_latest_admission,medical_history):
        self.name=name
        self.age=age
        self.date_of_latest_admission=date_of_latest_admission
        self.medical_history=medical_history
    def print_details(self):
        print(f'Name: {self.name}, Age: {self.age}, Date of latest admission: {self.date_of_latest_admission}, Medical history: {self.medical_history}')
patient01=Patients(name,age,date_of_latest_admission,medical_history)
print ("Patient Record:")
patient01.print_details()
