import pandas as pd 
data = pd.read_csv("new.csv")
sorted_df1 = sorted_df.sort_values(by=["Rating","Confidence"], ascending=False)
print(sorted_df1)


import csv
# with open('new.csv') as csvfile:
#   rows = csv.reader(csvfile)
#   _ = next(rows)
#   sorted1 = sorted(rows, key=lambda row: (int(float(row[1])),int(float(row[2]))), reverse=True)
#   for row in sorted1:
#     print(row[1],row[2])

# use pandas library ot count
#     create a map, rating (key) and confidens(value)
