from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value

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
    "email" : "abc12@hdfc.com",
    "linkedin_url": "https://www.linkedin.com/abc123",
    "weight" : 52.7, 
    "married" : False, 
    "contact_details" : {"mobile" : "90909090"},}

# Unpack the dictionary
patient_1 = Patient(**patient_info)

#Call the function
insert_patient_data(patient_1)
update_patient_data(patient_1)