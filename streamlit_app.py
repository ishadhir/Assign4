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
    st.subheader(f"Something New")
    st.bar_chart(df['Volume'])
# 1. Set up the Streamlit page title
    st.title("Simple Circle Drawer")

# 2. Create a figure and axis
    fig, ax = plt.subplots()

# 3. Draw a circle at center (0,0) with radius 1
    circle = plt.Circle((0, 0), radius=1, fill=False, color='blue', linewidth=2)
    ax.add_patch(circle)
    
# 4. Set equal scaling and limits so the circle doesn't look like an oval
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

# 5. Display the plot in the Streamlit app
    st.pyplot(fig)
