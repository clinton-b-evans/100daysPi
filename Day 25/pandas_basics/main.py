import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

# print(data_dict["temp"])

temperature_list = data["temp"].to_list()

# def get_average_temp(temperatures):
#     average_temp = 0
#     for temp in temperatures:
#         average_temp += temp
#         print(average_temp)
#     average_temp = average_temp / len(temperatures)
#     print(average_temp)

# get_average_temp(temperature_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# fahrenheit_temp = (monday.temp * 9/5) + 32
# print(fahrenheit_temp)

 #(Temperature in degrees Celsius (°C) * 9/5) + 32

data_dict = { 
    "students":["Clinton","Victoria","Connor"],
    "scores":[80,90,100],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")