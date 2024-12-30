import pandas as pd

path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/region.csv"
result = pd.read_csv(path)
print(pd.DataFrame(result))