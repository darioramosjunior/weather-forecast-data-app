import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
          help="Select the number of forecasted days")
option = st.selectbox("Select Data to View", options=("Sky", "Temperature"))
st.subheader(f"{option} for next {days} days in {place}")
