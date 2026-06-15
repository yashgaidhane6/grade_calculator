import streamlit as st

st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800&display=swap');

html, body, [class*="css"]{
    font-family:'Orbitron',sans-serif;
}

.stApp{
    background: linear-gradient(135deg,#050816,#081c3a,#001d3d);
    color:white;
}

/* Title */
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    color:#00e5ff;
    text-shadow:0 0 10px #00e5ff,
                0 0 20px #00e5ff,
                0 0 40px #00e5ff;
    margin-bottom:20px;
}

/* Labels */
label, p{
    color:#00e5ff !important;
    font-size:18px !important;
    font-weight:600 !important;
}

/* Input Boxes */
.stTextInput input,
.stNumberInput input{
    background:#0f172a !important;
    color:white !important;
    border:2px solid #00e5ff !important;
    border-radius:12px !important;
    padding:10px !important;
    font-size:18px !important;
}

/* Number Input Buttons */
.stNumberInput button{
    background:#00e5ff !important;
    color:black !important;
}

/* Button */
.stButton button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    font-size:20px;
    font-weight:bold;
    color:white;
    background:linear-gradient(90deg,#00e5ff,#0077ff);
    box-shadow:0 0 15px #00e5ff;
    transition:0.3s;
}

.stButton button:hover{
    transform:scale(1.03);
    box-shadow:0 0 30px #00e5ff;
}

/* Result Card */
.result-card{
    background:rgba(255,255,255,0.08);
    border:1px solid #00e5ff;
    border-radius:20px;
    padding:20px;
    text-align:center;
    margin-top:20px;
    box-shadow:0 0 20px rgba(0,229,255,0.5);
}

</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🎓 Grade Calculator</h1>',
            unsafe_allow_html=True)

name = st.text_input("👤 Student Name")

m1 = st.number_input("📚 Subject 1", min_value=0, max_value=100)
m2 = st.number_input("📚 Subject 2", min_value=0, max_value=100)
m3 = st.number_input("📚 Subject 3", min_value=0, max_value=100)
m4 = st.number_input("📚 Subject 4", min_value=0, max_value=100)
m5 = st.number_input("📚 Subject 5", min_value=0, max_value=100)

if st.button("🚀 Calculate Grade"):

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
        rank = "🏆 Excellent"
        st.balloons()
    elif percentage >= 80:
        grade = "A"
        rank = "⭐ Very Good"
    elif percentage >= 70:
        grade = "B"
        rank = "👍 Good"
    elif percentage >= 60:
        grade = "C"
        rank = "🙂 Average"
    elif percentage >= 50:
        grade = "D"
        rank = "⚠ Needs Improvement"
    else:
        grade = "F"
        rank = "❌ Fail"

    st.progress(int(percentage))

    st.markdown(f"""
    <div class="result-card">
        <h2>🎯 Result</h2>
        <h3>Student: {name if name else "Unknown"}</h3>
        <h3>Total Marks: {total}/500</h3>
        <h2>Percentage: {percentage:.2f}%</h2>
        <h1>Grade: {grade}</h1>
        <h3>{rank}</h3>
    </div>
    """, unsafe_allow_html=True)
    """, unsafe_allow_html=True)
