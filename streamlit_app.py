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
    st.subheader("Interactive Moving Average")
    window = st.slider("Select Moving Average Window (Days)", min_value=5, max_value=50, value=20)

    df_ma = df.copy()
    df_ma[f'{window}-Day MA'] = df_ma['Close'].rolling(window=window).mean()

    st.line_chart(df_ma[['Close', f'{window}-Day MA']])
