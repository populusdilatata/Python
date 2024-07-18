import pandas

data = pandas.read_csv("data-squirrel-census.csv")

gray_count = (len(data[data["Primary Fur Color"] == "Gray"]))
cinnamon_count = (len(data[data["Primary Fur Color"] == "Cinnamon"]))
black_count= (len(data[data["Primary Fur Color"] == "Black"]))
print(gray_count)
print(cinnamon_count)
print(black_count)

# Create a dataframe from scratch
data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count":[gray_count, cinnamon_count, black_count]
}

data_1 = pandas.DataFrame(data_dict)
print(data_1)
data_1.to_csv("squirrel_count.csv")

cinnamon = ((data[data["Primary Fur Color"] == "Cinnamon"]))
print(cinnamon.shape[0])