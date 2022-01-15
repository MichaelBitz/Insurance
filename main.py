'''
data accessible @ https://www.kaggle.com/mirichoi0218/insurance/version/1?select=insurance.csv
Michael Bitz
In scope of Codecademy: Data Scientist Path
Portfolio Project 1
'''

import csv
import numpy as np
from matplotlib import pyplot as plt

class Patient:   
    id_tick = 0

    def __init__(self, age,sex,bmi,children,smoker,region,charges):
        self.id = Patient.id_tick
        self.age = int(age)
        self.sex = sex
        self.bmi = float(bmi)
        self.children = int(children)
        self.smoker = smoker
        self.region = region
        self.charges = float(charges)
        Patient.id_tick += 1

    def __repr__(self):
        return (f''' 
        Id:  {self.id}
        Age:  {self.age}
        Sex:  {self.sex}
        BMI:  {self.bmi}
        Children:  {self.children}
        Smoker:  {self.smoker}
        Region: {self.region}
        Charges: {self.charges}
        ''')

class Registry: 

    def __init__(self):
        self.patients = {}
        
    def load_patient_data(self):     
        with open("insurance.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for line in reader:
                patient = Patient(*line)
                self.add_patient(patient)
            
    def add_patient(self, patient):
        self.patients[patient.id] = patient
    
    def display_patient_info(self):
        for patient_id in self.patients:
            patient = self.patients[patient_id]
            print(patient)

    def get_age_data(self):
        age_arr = self.get_age_array()
        print(f"Mean age: {np.mean(age_arr)}")
        print(f"Median age: {np.median(age_arr)}")
        print(f"STD in age: {np.std(age_arr)}")
        plt.hist(age_arr)
        plt.show()
        return None

    def get_age_array(self):
        return np.array([self.patients[patient_id].age for patient_id in self.patients])
        

    def get_charges_data(self):
        charges_arr = self.get_charges_array()
        print(f"Mean charges: {np.mean(charges_arr)}")
        print(f"Median charges: {np.median(charges_arr)}")
        print(f"STD in charges: {np.std(charges_arr)}")
        plt.hist(charges_arr)
        #plt.show()
        return None
    
    def get_charges_array(self):
        return np.array([self.patients[patient_id].charges for patient_id in self.patients])

    def get_sex_array(self):
        return np.array([self.patients[patient_id].sex for patient_id in self.patients])

    def get_sex_data(self):
        sex_arr = self.get_sex_array()
        print(f"% Men: {np.mean(sex_arr == 'male')*100}")

registry = Registry()
registry.load_patient_data()
registry.display_patient_info()
registry.get_age_data()
registry.get_charges_data()
registry.get_sex_data()




