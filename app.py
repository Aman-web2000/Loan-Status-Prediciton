import streamlit as st
import numpy as np
import pandas as pd 
import seaborn as sns 
import pickle
from PIL import Image

## Background Image
st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.unsplash.com/photo-1583574928052-9a2563277468?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


pickle_in=open('LoanPrediction.pkl','rb')
clf=pickle.load(pickle_in)

def predictor(l):
    prediction=clf.predict([l])
    return prediction[0]


def main():
    html_title="""
    <div style="background-color: darkslategrey; padding:10 px; border:double">
    <h1 style="color: white; font: bolder; text-align: center">Loan Status Predictor</h1>
    </div>
    """
    st.markdown(html_title,unsafe_allow_html=True)
    
    ApplicantIncome=st.number_input('Enter your Income',min_value=10000,max_value=10000000,step=5000)
    CoApplicantIncome=st.number_input('Enter CoApplicant Income',min_value=5000,max_value=1000000,step=2000)
    LoanAmount=st.slider('Loan Amount',min_value=50000,max_value=1000000,step=5000)
    LoanAmountTerm=st.number_input('Loan Amount Term',min_value=2,max_value=12,step=1)
    CreditHistory=st.radio('Do You Own Credit Card :',['0','1'])
    Dependents=st.radio('No of Dependents :',['0','1','2','3+'])
    propertyType=st.selectbox('Property Type',['Rural','Semi Urban','Urban'])
    Education=st.selectbox('Education Qualification',['Graduate','Non Graduate'])
    Employed=st.radio('Are you Self Employed:',['Yes','No'])

    l=[ApplicantIncome,CoApplicantIncome,LoanAmount,LoanAmountTerm,CreditHistory,Dependents,propertyType]
    l1=[]

    l1.append(l[0])
    l1.append(l[1])
    l1.append(l[2])
    l1.append(l[3])

    if l[4]=='0':
        l1.append(0)
    elif l[4]=='1':
        l1.append(1)

    if l[5]=='0':
        l1.append(0)
        l1.append(0)
        l1.append(0)
    elif l[5]=='1':
        l1.append(1)
        l1.append(0)
        l1.append(0)
    elif l[5]=='2':
        l1.append(0)
        l1.append(1)
        l1.append(0)
    elif l[5]=='3+':
        l1.append(0)
        l1.append(0)
        l1.append(1)
        
    if l[-1]=='Rural':
        l1.append(0)
        l1.append(0)
    elif l[-1]=='Semi Urban':
        l1.append(1)
        l1.append(0)
    elif l[-1]=='Urban':
        l1.append(0)
        l1.append(1)


    if st.button('Predict'):

        ans=predictor(l1)
        if ans==1:
            win="""
            <div style="background-color:#FFC300 ; padding:10px">
            <h2 style="color:black,font:bolder;">"Congratulations , Your Loan Application has been Approved!"</h2>
            </div>
            """
            st.markdown(win,unsafe_allow_html=True)
        else:
            lose="""
            <div style="background-color:#C70039 ; padding:10px">
            <h2 style="color:aliceblue ;font:bolder;">Sorry , Your Loan Application has been Rejected !</h2>
            </div>
            """
            st.markdown(lose,unsafe_allow_html=True)

if __name__=='__main__':
    main()
