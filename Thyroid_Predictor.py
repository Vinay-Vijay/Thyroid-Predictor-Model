# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 
import streamlit as st

#loading the saved model 
loaded_model=pickle.load(open('./Thyroid_Prediction.ipynb','rb'))

def Thyroid_Prediction(input_data):
    
    input_data_as_numpy_array = np.array(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0]==0):
        return 'The person does not have Thyroid'
    else:
        return 'The person has Thyroid'
    
def main():
    
    st.title('Thyroid Predictor')
    
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    onThyroxine = st.text_input('On Thyroxin')
    queryOnThyroxine = st.text_input('Query on Thyroxin')
    onAntithyroidMedication = st.text_input('On Anti Thyroid Medication')
    sick = st.text_input('Are you sick')
    pregnant = st.text_input('Are you pregnant')
    thyroidSurgery = st.text_input('Undergone Thyroid surgery')
    I131Treatment = st.text_input('Undergone I131 treatment')
    queryHypothyroid = st.text_input('Query on Hypothyroid')
    queryHyperthyroid = st.text_input('Query on Hyperthyroid')
    lithium = st.text_input('Lithium level')
    goitre = st.text_input('Goitre')
    tumor = st.text_input('Tumor')
    hypopituitary = st.text_input('Hypopitutary')
    psych = st.text_input('Pysch')
    TSHmeasured = st.text_input('TSHmeasured')
    TSH = st.text_input('TSH Level')
    T3measured = st.text_input('T3 measured')
    T3 = st.text_input('T3 level')
    TT4measured = st.text_input('TT4 measured')
    TT4 = st.text_input('TT4 Level')
    T4Umeasured = st.text_input("t$U measured")
    T4U = st.text_input('T4U Level')
    FTImeasured = st.text_input('FTI measured')
    FTI = st.text_input('FTI Level')
    TBGmeasured = st.text_input('TBG measured')
    TBG = st.text_input('TBG Level')
    
    diagnosis = ''
    
    if st.button('Thyroid Test Results'):
        diagnosis = Thyroid_Prediction([age, sex, onThyroxine, queryOnThyroxine, onAntithyroidMedication, sick, pregnant, thyroidSurgery, I131Treatment, queryHypothyroid, queryHyperthyroid, lithium, goitre, tumor, hypopituitary, psych, TSHmeasured, TSH, T3measured, T3, TT4measured, TT4, T4Umeasured, T4U, FTImeasured, FTI, TBGmeasured, TBG])
        
    st.success(diagnosis)



if __name__ == '__main__':
    main()
    
        
        