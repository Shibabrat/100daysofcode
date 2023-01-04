import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")
fur_color = data["Primary Fur Color"]

# print(f"Sum of brown color fur: {fur}")
gray_fur_color = sum(fur_color == "Gray")
cinnamon_fur_color = sum(fur_color == "Cinnamon")
black_fur_color = sum(fur_color == "Black")

data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_fur_color, cinnamon_fur_color, black_fur_color]
}

data_save = pandas.DataFrame(data_dict)
data_save.to_csv("fur_color.csv")

