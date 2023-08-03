import requests

API_KEY = "9c0eb41cbe331e3cfeaf5a9220f50322"


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    num_of_data = days * 8
    filtered_data = content["list"][:num_of_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Carcar", days=1))
