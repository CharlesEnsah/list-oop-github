class Patient:
    def __init__(self, name, patient_id, age, gender, diagnosis):
        self.name = name 
        self.patients_id =patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        
    def display_info(self):
        print("********** Patients Info**********")
        print(f"Name: {self.name}")
        print(f"Name: {self.patient_id}")
        print(f"Name: {self.age}")
        print(f"Name: {self.gender}")
        print(f"Name: {self.diagnosis}")

        