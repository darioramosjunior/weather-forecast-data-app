import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
          help="Select the number of forecasted days")
option = st.selectbox("Select Data to View", options=("Sky", "Temperature"))
st.subheader(f"{option} for next {days} days in {place}")

def get_data(days):
    dates = ["25-10", "26-10", "27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

graph = px.line(x=d, y=t, labels={"x":"Date", "y":"Temperature (C)"})
st.plotly_chart(graph)