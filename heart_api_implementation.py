#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 21:44:23 2025

@author: jaydeepahir
"""


import json
import requests

url = 'https://75ba-35-185-9-50.ngrok-free.app/heart_prediction'

input_data_for_model = {
    
    'age' : 63, 
    'sex' : 1, 
    'cp' : 3, 
    'trestbps' : 145,
    'chol' : 233,
    'fbs' : 1,
    'restecg' : 0,
    'thalach' : 150,
    'exang' : 0,
    'oldpeak' : 2.3,
    'slope' : 0,
    'ca' : 0,
    'thal' : 1
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, json=input_data_for_model)
print(response.json())