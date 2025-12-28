from optparse import Option
import streamlit as st

st.title("Movie Recommendation System")

Option=st.selectbox(
    'Select an option:',
    ('Home', 'Recommend Movies', 'About')
) 