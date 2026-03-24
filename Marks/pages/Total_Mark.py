import streamlit as st

st.write("No point calculating this now")

st.divider()

if st.button("Year 1 Modules", use_container_width=True):
    st.switch_page("Year_1_Modules.py")