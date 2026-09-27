import streamlit as st

st.title("Age Calculator App")

name = st.text_input("Please enter your name :_ ").title()

birth_year = st.number_input("Please enter your birth year :- ", step=1, format="%d", value=None)

current_year = 2026

if name and birth_year:

    if birth_year > current_year:
        st.error("Birth year cannot be in the future!")
    elif birth_year < 1900:
        st.error("Please enter a valid birth year!")
    else:
        birth_year = int(birth_year)
        age = current_year - birth_year
        st.write(f"Hello, {name}! You are {age} years old.")