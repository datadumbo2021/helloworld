import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

file_path = '/Users/prost/Downloads/231016_test.csv'
df = pd.read_csv(file_path)

st.header('DoBrain2 Dashboard with datetime')
st.write('Hello, *Prost!* :sunglasses:')

selected_profile = st.selectbox('Select ProfileId', df['ProfileId'].unique())
filtered_df = df[df['ProfileId'] == selected_profile]

# alSessionTypeLv 피벗 테이블
pivot_lv = pd.pivot_table(
    filtered_df, 
    values='alSessionTypeLv', 
    index='alSessionType', 
    columns='serial', 
    aggfunc=np.max
)

# createdAt 피벗 테이블
pivot_created_at = pd.pivot_table(
    filtered_df, 
    values='createdAt', 
    index='alSessionType', 
    columns='serial', 
    aggfunc='first'
)

# 결과를 저장할 빈 데이터프레임 생성
final_df = pd.DataFrame(index=pivot_lv.index)

# 두 피벗 테이블의 각 열을 번갈아 가며 최종 데이터프레임에 추가
for col in pivot_lv.columns:
    final_df[f'lv_{col}'] = pivot_lv[col]
    final_df[f'createdAt_{col}'] = pivot_created_at[col]

st.write(final_df)
