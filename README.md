💸 **Expense Tracker – TrackSo**

A simple, clean, and modern Streamlit-based Expense Tracker that allows you to quickly add, view, and download your daily expenses.
This project is created as a Python Semester Project using Streamlit + Pandas.

🚀 **Features**

✅ Add Expenses Easily
Enter amount, category, and description
Auto-stored with timestamp

**📊 **View Expense History****

Displays your expense list in a beautiful, interactive table

Shows all saved entries for the entire session

Categories: Food, Travel, Shopping, Bills, Other

**💰 Total Expense Calculation**

Automatically calculates and displays the total money spent

📥 Download as CSV

Export your expenses with one click

File: expenses.csv

**🎨 Modern UI with Custom CSS**

Neon-themed dark UI

Styled buttons, cards, table view

Fully responsive layout

**🛠️ Tech Stack**
Component	Technology
Frontend UI	Streamlit + HTML/CSS
Backend Logic	Python
Data Handling	Pandas
Storage	Streamlit Session State
Output	CSV Download
📂 Project Structure
📦 Expense-Tracker
│
├── app.py        # Main Streamlit Application
├── requirements.txt  # Required Python dependencies
└── README.md     # Documentation

▶️ How to Run This Project

1️⃣ Install Dependencies

Make sure Python is installed.
Then install required libraries:

pip install streamlit pandas

2️⃣ Run the Streamlit App
streamlit run app.py

App will open in your browser automatically.

**📸 Features Explained**
Add Expense Section

Inputs for amount, category, description

Adds into st.session_state memory

Clean notification on successful entry

Expense Dashboard

A pandas DataFrame displayed using st.dataframe()

Realtime summary calculation

Download button to save expense data locally

**📁 Data Storage Logic**

All expenses are stored temporarily inside:

st.session_state.expenses

This means data resets when page reloads—perfect for simple projects or demos.

**⭐ Future Improvements** 

Add charts for spending visualization

Save data permanently using SQLite

Add login system

Monthly category-wise analysis

Export PDF report

**🧑‍💻 Author**

Sohely Das and Sougata Mondal
