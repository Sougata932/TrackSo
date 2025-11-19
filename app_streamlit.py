import streamlit as st
import pandas as pd
from datetime import datetime

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="💸 Expense Tracker - Sohely Edition",
    page_icon="💸",
    layout="centered"
)

# -------------------------------------------------------
# CUSTOM CSS STYLING
# -------------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #00e5ff;
    padding-bottom: 10px;
}

.expense-card {
    background: #1b1f27;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 8px rgba(0,255,255,0.3);
    margin-bottom: 20px;
}

.stButton button {
    background-color: #00e5ff !important;
    color: black !important;
    border-radius: 10px !important;
    padding: 10px 20px;
    font-weight: 600;
}

.stDownloadButton button {
    background-color: #ffb300 !important;
    border-radius: 10px !important;
    color: black !important;
}

.dataframe {
    border-radius: 10px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------
st.markdown('<h1 class="title">💸 Expense Tracker</h1>', unsafe_allow_html=True)

# -------------------------------------------------------
# SESSION STORAGE
# -------------------------------------------------------
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# -------------------------------------------------------
# INPUT CARD
# -------------------------------------------------------
with st.container():
    st.markdown('<div class="expense-card">', unsafe_allow_html=True)

    st.subheader("➕ Add New Expense")

    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Amount (₹):", min_value=1)
    with col2:
        category = st.selectbox("Category", ["🍔 Food", "🚌 Travel", "🛍 Shopping", "📑 Bills", "📦 Other"])

    desc = st.text_input("Description")

    if st.button("Add Expense"):
        entry = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Amount": amount,
            "Category": category,
            "Description": desc,
        }
        st.session_state.expenses.append(entry)
        st.success("Expense added successfully!")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------
# SHOW TABLE + STATS
# -------------------------------------------------------
if st.session_state.expenses:
    st.markdown('<div class="expense-card">', unsafe_allow_html=True)

    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("📊 Expense History")

    st.dataframe(df, use_container_width=True)

    total = df["Amount"].sum()
    st.subheader(f"💰 Total Spent: **₹{total:.2f}**")

    # CSV Download
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="💾 Download CSV",
        data=csv,
        file_name="expenses.csv",
        mime="text/csv",
    )

    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No expenses added yet! Start by entering one above 👆")