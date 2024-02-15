import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title(" Survey of Lung Cancer")
st.write("Please fill out the folloeing survey to help us gather information about lung cancer")
#survey questions
age=st.slider("What is your age?",18,100,50)
gender=st.radio("What is your gender?",["Male","Female"])
smoking_status=st.radio("Do you currently smoke cigarettes?",["Yes","No"])
years_somked=st.slider("How many years have you smoked?",0,100,20)
family_history=st.radio("Do you have a family history of lung cancer?",["Yes","No"])
symptom_duration=st.slider("How long have you experienced symptoms?",0,60,30)
#submit button
if st.button("submit"):
    # store survey responses in a dataFrame
    survey_data=pd.DataFrame({"Age":[age],"Gender":[gender],"Smoking Status":[smoking_status],"Years Smoked":[years_somked],
                              "symptom Duration":[symptom_duration]}) 
    
    import streamlit as st
    st.divider()
    import pandas as pd
    df=pd.read_csv("C:\\Users\\Admin\\Desktop\\Dashboard\\survey lung cancer.csv")
    df
    st.write("Graphs of survey lung cancer")
    import matplotlib.pyplot as plt
    st.bar_chart(df)
    st.line_chart(df)
    st.scatter_chart(df)
    
     