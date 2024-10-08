import streamlit as st
import pandas as pd
st.set_page_config(
    page_title='Palmer Penguins Predictor',
    page_icon='🐧',
)

st.title('🐧 Palmer Penguins Predictor')
with st.expander('data'):
    st.write('**RAW DATA**')
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/palmer-penguins/4dbd79d6ae9f5f97ec9682e79e8ce73c150aca1f/data/penguins_cleaned.csv') 
    df

    st.write('**X**')
    x = df.drop('species',axis=1)
    x
    st.write('**Y**')
    y = df.species
    y
    
 with st.expander('data visualization'):
    
    st.scatter_chart( data =df,x= 'bill_lenght_mm',y='body_mass_g',color='species')
       
       
