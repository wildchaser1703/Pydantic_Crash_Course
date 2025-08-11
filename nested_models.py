from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    age  : int
    gender : str
    address : Address

address_dict = {
    "city" : "Gurgaon", 
    "state" : "Haryana", 
    "pin" : "120120"}

address1 = Address(**address_dict)

patient_dict = {
    "name" : "Anita", 
    "age" : 30, 
    "gender" : "female", 
    "address" : address1}

patient1 = Patient(**patient_dict) 

print(patient1.name)
print(patient1.address.city)