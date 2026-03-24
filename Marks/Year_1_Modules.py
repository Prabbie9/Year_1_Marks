import streamlit as st

st.title("Year 1 Modules")
st.write("Select a page:")

if st.button("Total Mark", use_container_width=True):
    st.switch_page("pages/total_mark.py")

if st.button("Algebra 1", use_container_width=True):
    st.switch_page("pages/algebra_1.py")

if st.button("Algebra 2", use_container_width=True):
    st.switch_page("pages/algebra_2.py")

if st.button("Analysis 1", use_container_width=True):
    st.switch_page("pages/analysis_1.py")

if st.button("Analysis 2", use_container_width=True):
    st.switch_page("pages/analysis_2.py")

if st.button("Foundations", use_container_width=True):
    st.switch_page("pages/foundations.py")

if st.button("Introduction to Probability", use_container_width=True):
    st.switch_page("pages/introduction_to_probability.py")

if st.button("Mathematics By Computer", use_container_width=True):
    st.switch_page("pages/mathematics_by_computer.py")

if st.button("Methods of Mathematical Modelling 1", use_container_width=True):
    st.switch_page("pages/methods_of_mathematical_modelling_1.py")

if st.button("Methods of Mathematical Modelling 2", use_container_width=True):
    st.switch_page("pages/methods_of_mathematical_modelling_2.py")

if st.button("Programming for Scientists", use_container_width=True):
    st.switch_page("pages/programming_for_scientists.py")

if st.button("Statistical Laboratory", use_container_width=True):
    st.switch_page("pages/statistical_laboratory.py")

