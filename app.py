
import numpy as np
import joblib
import pandas as pd
#from flasgger import Swagger
import streamlit as st 


regressor = joblib.load('Grades.pkl')

def welcome():
    return "Welcome All"

def predict_note_authentication(CAT1,CAT2,DA1,DA2):
   
    prediction=regressor.predict([[CAT1,CAT2,DA1,DA2]])
    print(prediction)
    return prediction



def main():
    st.title("Grade Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Predict your Grades using this App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    CAT1 = st.text_input("CAT1","Type Here")
    CAT2 = st.text_input("CAT2","Type Here")
    DA1 = st.text_input("DA1","Type Here")
    DA2 = st.text_input("DA2","Type Here")
    result=""
    if st.button("Click here to view Prediction"):
        result=predict_note_authentication(CAT1,CAT2,DA1,DA2)
    st.success('The output is {}'.format(result))
    if st.button("Regards"):
        st.text("All the best for FAT")
        st.text("Perform well")

if __name__=='__main__':
    main()