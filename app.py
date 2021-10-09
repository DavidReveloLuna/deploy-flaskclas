# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:15:14 2021

@author: dreve
"""

from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return 'Deploy ML'

@app.route("/predecir", methods=['POST'])
def prediccion():
    json = request.get_json(force=True)
    xin = json['Datos']
    print(xin)
    yout = model.predict(xin)
    print(yout)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'El paciente corresponde a la clase {}\n'.format(labels[y_out])
        
    return mensaje

pkl_filename = 'diabetes_model.pkl'
with open(pkl_filename,'rb') as file:
    model = pickle.load(file)

labels = ['Sano','Diabetes']

if __name__ == '__main__':
    app.run()
