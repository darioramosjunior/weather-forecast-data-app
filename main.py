import streamlit as st
import plotly.express as px
from backend import get_data

# Front-end
st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
          help="Select the number of forecasted days")
option = st.selectbox("Select Data to View", options=("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place}")

if place:
    # Get the temperature or Sky data
    try:
        filtered_data = get_data(place, days)

        # Create the plot
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            # Convert all values to deg C by dividing them by 10
            temperatures = [ each / 10 for each in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            graph = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(graph, theme=None)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a translation dictionary of each condition to their equivalent  image paths
            images = {"Clouds": "images/cloud.png", "Clear": "images/clear.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            # Get image paths for each condition in the sky conditions
            image_paths = [images[condition] for condition in sky_conditions]
            # render list of images with corresponding dates as caption
            st.image(image_paths, width=170, caption=dates)
    except KeyError:
        st.error("You entered a place that is non-existent.")