import streamlit as st
import numpy as np
import pandas as pd
from streamlit import column_config


def space():
    st.write("")
    st.write("")
def style(df: pd.DataFrame):
    return (
        df.style.set_properties(**{
            "text-align": "center",
            "font-size": "18px",
            "font-weight": "bold"
        })
    )
def dataframe(df: pd.DataFrame):
    return (st.dataframe(data=style(df), width="stretch", height="content", hide_index=True, column_order=["Type","Weighting","Percentage","Actual Mark?"],column_config={"Percentage": st.column_config.NumberColumn("Percentage",format="percent"),"Weighting": st.column_config.NumberColumn("Weighting",format="%.2f"),"Weighting": st.column_config.NumberColumn("Weighting",format="percent")}))

marks_df = pd.DataFrame(
    [
        {"Type": "Moodle Quizzes","Weighting":0.15, "Percentage": 1, "Actual Mark?": "Yes", "Colour":"#0000ff"},
        {"Type": "Final Exam","Weighting":0.85, "Percentage": 0.85, "Actual Mark?": "No", "Colour":"#0000ff"},
    ]
)
final_mark = (marks_df["Weighting"] * marks_df["Percentage"]).sum()
final_mark_df = pd.DataFrame([{"Type":"Final Mark","Weighting":1.00, "Percentage":final_mark, "Actual Mark?":"No", "Colour":"#ff0000"}])
final_df = pd.concat([marks_df, final_mark_df], ignore_index=True)


st.title("Foundations Marks")


dataframe(final_mark_df)

st.markdown("CATS: 10")

st.divider()

dataframe(marks_df)

space()

st.bar_chart(final_df,x = "Type",y="Percentage",width = "stretch", height = "content", color = "Colour",sort = False)
st.divider()

if st.button("Year 1 Modules", use_container_width=True):
    st.switch_page("Year_1_Modules.py")
if st.button("Total Mark", use_container_width=True):
    st.switch_page("pages/total_mark.py")
