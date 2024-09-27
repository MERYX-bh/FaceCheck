import streamlit as st
import pandas as pd
import os
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Dashboard Title
st.set_page_config(page_title="Attendance Dashboard", layout="wide")

# Custom styles for better appearance
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #333;
    }
    .stDataFrame {
        background-color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("📊 Attendance Dashboard")
st.write("Real-time attendance tracking and status")

# Current Date and Time
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# Sidebar with date and time
with st.sidebar:
    st.markdown("### Current Date & Time")
    st.markdown(f"**Date:** {date}")
    st.markdown(f"**Time:** {timestamp}")
    
# Displaying attendance refresh counter
st.markdown("### Attendance Count Status")
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# FizzBuzz logic displayed as metrics
col1, col2, col3 = st.columns(3)
with col1:
    if count % 3 == 0 and count % 5 == 0:
        st.metric("Status", "FizzBuzz")
    elif count % 3 == 0:
        st.metric("Status", "Fizz")
    elif count % 5 == 0:
        st.metric("Status", "Buzz")
    else:
        st.metric("Count", count)
with col2:
    st.metric("Total Refreshes", count)
with col3:
    st.metric("Last Update", timestamp)

# Divider
st.markdown("---")

# Define the CSV file path
csv_file = "Attendance/Attendance_" + date + ".csv"

# Check if the file exists and show a more styled table if it exists
st.markdown("### Today's Attendance Records")
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)

    # Check if the dataframe is not empty
    if not df.empty:
        # Display the DataFrame with better styling
        st.dataframe(df.style.highlight_max(axis=0), height=400)
    else:
        st.warning("The CSV file exists but is empty.")
else:
    st.error(f"No attendance file found for today: {date}")

# Footer message
st.markdown("---")
st.markdown("### Thank you for using the Attendance Dashboard!")
