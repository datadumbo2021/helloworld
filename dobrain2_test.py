import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import time, datetime

file_path = '/Users/prost/Downloads/231016_test.csv'
df = pd.read_csv(file_path)

st.header('DoBrain2 Dashboard')
st.write('Hello, *Prost!* :sunglasses:')

selected_profile = st.selectbox('Select ProfileId', df['ProfileId'].unique())
filtered_df = df[df['ProfileId'] == selected_profile]

pivot_df = pd.pivot_table(
    filtered_df, 
    values='alSessionTypeLv', 
    index='alSessionType', 
    columns='serial', 
    aggfunc=np.max
)

st.write(pivot_df)
