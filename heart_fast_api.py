#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 21:16:07 2025

@author: jaydeepahir
"""


from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import json

app = FastAPI()

class model_input(BaseModel):
    
    age : int 
    sex : int 
    cp : int 
    trestbps : int
    chol : int 
    fbs : int
    restecg : int
    thalach : int 
    exang : int 
    oldpeak : float 
    slope : int 
    ca : int 
    thal : int 
    
    
diabetes_model = pickle.load(open('heart_model.sav', 'rb'))

@app.post('/heart_prediction')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age = input_dictionary['age']
    sex = input_dictionary['sex']
    cp = input_dictionary['cp']
    trestbps = input_dictionary['trestbps']
    chol = input_dictionary['chol']
    fbs = input_dictionary['fbs']
    restecg = input_dictionary['restecg']
    thalach = input_dictionary['thalach']
    exang = input_dictionary['exang']
    oldpeak = input_dictionary['oldpeak']
    slope = input_dictionary['slope']
    ca = input_dictionary['ca']
    thal = input_dictionary['thal']
    
    input_list = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    prediciton = diabetes_model.predict([input_list])
    
    if (prediciton[0] == 0):
        return 'The person does not have heart disease'
    else :
        return 'The person has heart disease'