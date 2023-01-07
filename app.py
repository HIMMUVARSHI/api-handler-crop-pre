import streamlit as st
import pickle


st.title('Crop Prodicition System')
model=pickle.load(open('model.pkl','rb'))
col1,col2=st.columns(2)
n=col1.number_input('Enter Nitrogen:')
p=col2.number_input('Enter Phosphorous:')
k=col1.number_input('Enter potassium:')
t=col2.number_input('Enter temp:')
h=col1.number_input('Enter humid:')
ph=col2.number_input('Enter PH:')
r=col1.number_input('Enter rainfall:')


if st.button('Predict'):
    data=[[n,p,k,t,h,ph,r]]
    result=model.predict(data)[0]
    st.success(result)