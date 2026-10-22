import streamlit as st
import joblib
import pandas as pd

# set the tab title
st.set_page_config("Deployment Project")

# Set the page title
st.title("Machine Failure Prediction Project")

# Set header
st.subheader("By Radhika Nirmalkar")

# Load the pipeline (data cleaning, preprocessing) and model
pre = joblib.load("pipeline.joblib")
model = joblib.load("model.joblib")

# Create Input boxes that takes input from the user 
ID = st.number_input("ID")
Product_ID = st.number_input("Product ID")
Type = st.selectbox("Type",options=['L','M'])
Air Temperature[K] = st.number_input("Ait Temperature")
Process Temperature[K] = st.number_input("Process Temperature")
Rotational Speed[RPM] = st.number_input("Rotaional Speed")
Torque[NM] = st.number_input("Torque")
Tool Wear = st.number_input("Tool Wear")
TWF = st.number_input("TWF")
HDF = st.number_input("HDF")
PWF = st.number_input("PWF")
OSF = st.number_input("OSF")
RNF = st.number_input("RNF")

# Include a button. After providing all the inputs, user will click on the button. The button should provide the necessary predictions
submit = st.button("Predict Machine Failure  Status")

if submit:
    data = {
        'id':[ID],
        'Product ID':[Product_ID],
        'Type':[Type],
        'Air Temperature[K]':[Air Temperature[K]],
        'Process Temperature[K]':[Process Temperature[K]],
        'Rotational speed[rpm]':[Rotatioanl Speed[RPM]],
        'Torque[Nm]':[Torque[NM]],
        'Tool wear[min]':[Tool Wear],
        'TWF':[TWF],
        'HDF':[HDF],
        'PWF':[PWF],
        'OSF':[OSF],
        'RNF':[RNF]
    }
    # Convert above dictionary into dataframe first
    xnew = pd.DataFrame(data)
    # Apply data cleaning and preprocessing on new data using pre pipeline
    
    xnew_pre = pre.transform(xnew)
    xnew_pre.columns = [re.sub(r'[\[\]<]', '_', str(col)) for col in xnew_pre.columns]
    test_col2=xnew_pre['Product ID'].fillna('L53257').astype(str)
    xnew_pre['Product ID'] = test_col2.map(mapping).fillna(-1).astype(int)
    # predictions
    preds = model.predict(xnew_pre)
    if preds[0]==1:
        op = 'Machine is Failed'
        # st.subheader('Machine is Failed')
    else:
        op = 'Machine is Not Failed'
        # st.subheader('Machine is Not Failed')
    
    st.subheader(op)
