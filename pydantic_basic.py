from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    #Type validation
    name : Annotated[str, Field(max_length = 50, 
                                title= "Name of the patient", description="The name of the patient for our record", 
                                examples = ["Ron", "Weasley"])]
    age : int = Field(gt = 0, lt = 60)
    email : EmailStr
    linkedin_url : AnyUrl
    weight : Annotated[float, Field(gt = 0, strict = True)]
    married : Annotated[bool, Field(default = None)]
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {
    "name" : "Anita", 
    "age" : 30, 
    "email" : "abc12@gmail.com",
    "linkedin_url": "https://www.linkedin.com/abc123",
    "weight" : 52.7, 
    "married" : False, 
    "contact_details" : {"mobile" : "90909090"},}

# Unpack the dictionary
patient_1 = Patient(**patient_info)

#Call the function
insert_patient_data(patient_1)
update_patient_data(patient_1)