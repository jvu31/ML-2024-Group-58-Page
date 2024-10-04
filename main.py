import streamlit as st
import pandas as pd


contributions = pd.DataFrame (
    [
        {"Name": "Jimmy", "Contributions": "gfnkjlgdf"},
    ]
)

# Display text
st.title('Star Classification Model')
st.header('CS 4641 - Fall 2024')
st.subheader('Introduction/Background')
st.text("*insert intro*")
st.subheader('Problem Definition')
st.text("*insert problem*")
st.subheader('Methods')
st.text("*insert method*")
st.subheader('(Potential) Results and Discussion')
st.text("*insert results*")
st.subheader('References')
st.text("*insert references*")
st.subheader('Gantt Chart')
st.subheader('Contribution Table')
st.data_editor(contributions, hide_index=True)


