from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name : str
    age : int
    height : float  #m
    weight : float  #kg
    married : bool

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height ** 2),2)
        return bmi

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("BMI is", patient.bmi)
    print("Inserted")

patient_info = {
    "name" : "Anita", 
    "age" : 30, 
    # if age is 65
    "height" : 1.72,
    "weight" : 52.7, 
    "married" : False, 
    "contact_details" : {"mobile" : "90909090"},}
    # then contact details
    # "contact_details" : {"emergency" : "90909090"},}

# Unpack the dictionary
patient_1 = Patient(**patient_info)

#Call the function
insert_patient_data(patient_1)
