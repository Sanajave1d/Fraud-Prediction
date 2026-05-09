import streamlit as st
import pandas as pd
import joblib

model= joblib.load('fraud_detection.pkl')

st.title('Fraud Detection')
st.markdown('Enter the transaction details to predict if it is fraudulent or not.')

st.divider()

# Input fields
transcation_type = st.selectbox('Transaction Type', ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])

amount = st.number_input('Amount', min_value=0.0, value = 1000.0, step=0.01)
oldbalanceOrg = st.number_input('Old Balance Origin', min_value=0.0, value = 0.0, step=0.01)
newbalanceOrig = st.number_input('New Balance Origin', min_value=0.0, value = 0.0, step=0.01)
oldbalanceDest = st.number_input('Old Balance Destination', min_value=0.0, value = 0.0, step=0.01)
newbalanceDest = st.number_input('New Balance Destination', min_value=0.0, value = 0.0, step=0.01)

if st.button('Predict'):
    input_data = pd.DataFrame({
        'type': [transcation_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    prediction = model.predict(input_data)[0]

    st.subheader(f'Prediction Result: {int(prediction)}')

    if prediction == 1:
        st.error('The transaction is predicted to be fraudulent.')
    else:
        st.success('The transaction is predicted to be legitimate.')   
