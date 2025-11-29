#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 11:16:26 2025

@author: jaydeepahir
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import json

app = FastAPI()

class model_input(BaseModel):
    
    pregnancies : int 
    Glucose : int 
    BloodPressure : int 
    SkinThikness : int
    Insulin : int 
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int 
    
    
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

@app.post('/2zDFSUnkjCVXHIl4X5zGCr9m4hL_caoxoHmvrN5wvzzgYJzs')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThikness']
    ins = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    input_list = [preg, glu, bp, skin, ins, bmi, dpf, age]
    
    prediciton = diabetes_model.predict([input_list])
    
    if (prediciton[0] == 0):
        return 'The person is not diabetic'
    else :
        return 'The person is diabetic'
    