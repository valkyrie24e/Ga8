import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.header('Divide Two Numbers')
def user_input_features():
name1 = st.munber_input("Enter the first number", "Type Here ...")
name2 = st.number_input("Enter the second number", "Type Here ...")
getanswer = st.selectbox("Get answer in:",['whole', 'Float'])

if(status == 'Whole'):
    # take height input in centimeters
  try:
        answer = round(name1/name2)
  except:
        st.text("Enter the numbers")
 
else:
    # take height input in meters
  try:
        answer = float(name1/name2)
  except:
        st.text("Enter the numbers")
if(st.button("submit")):
   st.text("The answer is {}.".format(answer))
else:
    st.error("not valid")
data = {'Enter the first number': name1,
            'Enter the second number': name2,
            'Get answer in': getanswer,
            }
features = pd.DataFrame(data, index=[0])
return features
  
