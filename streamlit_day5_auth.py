import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


# --- USER AUTHENTICATION ---
names = ["Christine", "Prost"]
usernames = ["christine", "prost"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("rb") as file:
    hashed_passwords =  pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "dobrain_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")
    
if authentication_status ==  None:
    st.warning("Please enter your username and password")
    
if authentication_status:

    st.header('Do!Brain!')

    st.write('Hello, *Prost!* :sunglasses:')

    st.write(1234)

    df = pd.DataFrame({'first column': [1,2,3,4],
        'second column': [10,20,30,40]})
        
    st.write(df)

    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
    
    df2 = pd.DataFrame(
        np.random.randn(200,3),
        columns=['a','b','c']
    )

    c = alt.Chart(df2).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a','b','c']
    )

    st.write(c)
    
    # --- SIDEBAR ---
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
