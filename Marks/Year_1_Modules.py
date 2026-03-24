import streamlit as st

st.title("Year 1 Modules")
st.write("Select a page:")

if st.button("Total Mark", use_container_width=True):
    st.switch_page("pages/Total_Mark.py")

if st.button("Algebra 1", use_container_width=True):
    st.switch_page("pages/Algebra_1.py")

if st.button("Algebra 2", use_container_width=True):
    st.switch_page("pages/Algebra_2.py")

if st.button("Analysis 1", use_container_width=True):
    st.switch_page("pages/Analysis_1.py")

if st.button("Analysis 2", use_container_width=True):
    st.switch_page("pages/Analysis_2.py")

if st.button("Foundations", use_container_width=True):
    st.switch_page("pages/Foundations.py")

if st.button("Introduction to Probability", use_container_width=True):
    st.switch_page("pages/Introduction_to_Probability.py")

if st.button("Mathematics By Computer", use_container_width=True):
    st.switch_page("pages/Mathematics_By_Computer.py")

if st.button("Methods of Mathematical Modelling 1", use_container_width=True):
    st.switch_page("pages/Methods_of_Mathematical_Modelling_1.py")

if st.button("Methods of Mathematical Modelling 2", use_container_width=True):
    st.switch_page("pages/Methods_of_Mathematical_Modelling_2.py")

if st.button("Programming for Scientists", use_container_width=True):
    st.switch_page("pages/Programming_for_Scientists.py")

if st.button("Statistical Laboratory", use_container_width=True):
    st.switch_page("pages/Statistical_Laboratory.py")

