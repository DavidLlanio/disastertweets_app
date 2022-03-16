from helper import *

import streamlit as st

# Markdown with description of app
st.write("""
# Disaster Tweet Classification App
### Based on the Kaggle comptetition: https://www.kaggle.com/c/nlp-getting-started
Type in a sentence and the model will predict whether you are talking about a disaster or not
""")
st.write('---')

# Textbox for user to write their sentence
input_string = st.text_input("Type in your tweet", max_chars=280)

# Predict once button is pressed
prediction = -1
if st.button("Predict"):
    prediction = get_prediction(input_string)

if prediction == 1:
    st.write("""
    ### Model Predicts: Your text IS about a disaster
    """)
else:
    st.write("""
    ### Model Predicts: Your text IS NOT about a disaster
    """)
