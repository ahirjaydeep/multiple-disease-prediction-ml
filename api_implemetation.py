#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 12:00:28 2025

@author: jaydeepahir
"""
'''
import json
import requests

url = 'https://bae7-35-243-143-16.ngrok-free.app/diabetes_prediction'

input_data_for_model = {
    
    'pregnancies' : 5,
    'Glucose' : 166,
    'BloodPressure' : 72,
    'SkinThikness' : 19,
    'Insulin' : 175,
    'BMI' : 25.8,
    'DiabetesPedigreeFunction' : 0.587,
    'Age' : 51
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, json=input_data_for_model)
print(response.json())
'''


# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 19:06:30 2022

@author: siddhardhan
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 12:16:26 2022

@author: siddhardhan

"""

import json
import requests


url = 'https://bae7-35-243-143-16.ngrok-free.app/diabetes_prediction'


input_data_for_model = {
    
    'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)