import streamlit as st
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Load the model and the scaler
model = joblib.load('prediction.pkl')
scaler = joblib.load('scaler.pkl')


# Streamlit UI
st.title('Titanic Survival Prediction')

# User input
Pclass = st.selectbox('Ticket Class', [1, 2, 3])
Sex = st.selectbox('Sex', ['Male', 'Female'])
Age = st.number_input('Age', min_value=0.42, max_value=80.0, value=22.0)
SibSp = st.number_input('Number of Siblings/Spouses Aboard', min_value=0, max_value=8, value=1)
Parch = st.number_input('Number of Parents/Children Aboard', min_value=0, max_value=6, value=0)
Fare = st.number_input('Passenger Fare', min_value=0.0, max_value=512.3292, value=7.25)
Embarked = st.selectbox('Port of Embarkation', ['Southampton', 'Cherbourg', 'Queenstown'])

# Convert user input to numerical values
Sex = 0 if Sex == 'Male' else 1
Embarked = {'Southampton': 0, 'Cherbourg': 1, 'Queenstown': 2}[Embarked]

# Prepare input data for prediction
input_data = np.array([Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]).reshape(1, -1)
input_data_scaled = scaler.transform(input_data)


# Prediction button
if st.button('Predict'):
    # Prediction
    prediction = model.predict(input_data_scaled)
    prediction_proba = model.predict_proba(input_data_scaled)

    # Display the result
    st.write(f'Survival Prediction: {"Survived" if prediction[0] == 1 else "Not Survived"}')
    #st.write(f'Prediction Probability: {prediction_proba[0][1]:.4f} for Survived')
