import pandas

def main():
      data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
      gray = len(data[data["Primary Fur Color"] == "Gray"])
      red = len(data[data["Primary Fur Color"] == "Cinnamon"])
      black = len(data[data["Primary Fur Color"] == "Black"])

      squirrel_count = {
          "Fur Color" : ["gray", "red", "black"],
          "Count" : [gray, red, black]
      }

      squirrel_count_df = pandas.DataFrame(squirrel_count)
      squirrel_count_df.to_csv("squirrel_count")
      print(squirrel_count_df)


if __name__ == "__main__":
    main()