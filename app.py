import streamlit as st

# Page Config
st.set_page_config(
    page_title="Grade Calculator",
    page_icon="📚",
    layout="centered"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-title">
    🎓 Grade Calculator
</div>
<div class="subtitle">
    Calculate Percentage & Grade Instantly
</div>
""", unsafe_allow_html=True)

# Input Section
st.markdown("<br>", unsafe_allow_html=True)

name = st.text_input("Student Name")

m1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100)
m2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100)
m3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100)
m4 = st.number_input("Subject 4 Marks", min_value=0, max_value=100)
m5 = st.number_input("Subject 5 Marks", min_value=0, max_value=100)

if st.button("Calculate Grade"):

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    st.markdown(f"""
    <div class="result-card">
        <h2>{name}</h2>
        <h3>Total Marks: {total}/500</h3>
        <h3>Percentage: {percentage:.2f}%</h3>
        <h1>Grade: {grade}</h1>
    </div>
    """, unsafe_allow_html=True)