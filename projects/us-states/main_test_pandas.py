# import csv
#
# temperatures = []
# with open("weather_data.csv") as file:
#     weather = csv.reader(file)
#     for row in weather:
#         if row[1] != "temp":
#             temperatures.append(float(row[1]))
#         print(row)
#
# print(temperatures)
import pandas
import pandas as pd


def celsius_to_fahrenheit(temp_in_celsius):
    return (9/5)*temp_in_celsius + 32


data = pd.read_csv("weather_data.csv")
temperatures = data["temp"].to_list()

average_temp = sum(temperatures)/len(temperatures)
print(f"Average temperature: {average_temp:.2f}")

print(f"Maximum temperature: {data['temp'].max():.2f}")

# which day had the maximum temperature
row = data[data.temp == data.temp.max()]
print(row.day)

monday = data[data.day == "Monday"]
temperature = float(monday.temp)
print(f"Monday's temperature in F: {celsius_to_fahrenheit(temperature):.2f}")

# Create and save data
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")









