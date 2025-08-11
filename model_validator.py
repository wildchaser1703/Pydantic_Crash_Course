from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    #Type validation
    name : str
    age : int 
    email : EmailStr
    linkedin_url : AnyUrl
    weight : float
    married : bool
    contact_details : Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients over 60 must have an emergency contact in contact_details.")
        return model


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {
    "name" : "Anita", 
    "age" : 30, 
    # if age is 65
    "email" : "abc12@hdfc.com",
    "linkedin_url": "https://www.linkedin.com/abc123",
    "weight" : 52.7, 
    "married" : False, 
    "contact_details" : {"mobile" : "90909090"},}
    # then contact details
    # "contact_details" : {"emergency" : "90909090"},}

# Unpack the dictionary
patient_1 = Patient(**patient_info)

#Call the function
insert_patient_data(patient_1)
update_patient_data(patient_1)