# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Isha Dhir")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "Something"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

#Tab 4: 
with tabs[3]:
    st.subheader(f"💡 Microsoft Investment Simulator")
    # 1. User inputs
        investment_amount = st.number_input("Enter investment amount ($):", min_value=10, value=100, step=10)
    # 2. Get the most recent closing price from your existing DataFrame (df)
        latest_price = df['Close'].iloc[-1]
    # 3. Simple calculation
        shares_bought = investment_amount / latest_price
    # 4. Display results cleanly
        st.metric(label="Latest MSFT Price", value=f"${latest_price:,.2f}")
        st.success(f"With **${investment_amount:,.2f}**, you could purchase **{shares_bought:.4f}** shares of MSFT.")

