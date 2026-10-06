import pandas as pd

#CSV file ko load karo
df = pd.read_csv("data/students.csv")

# Pura data dikhao
print(df)

#Sirf pehli 2 rows dekho
print(df.head(2))

#Colour name dekho
print(df.columns)

#Sirf ek column dekho (jaise sirf "marks")
print(df["marks"])

#Basic statistics (mean, max min, stc. sab ek saath)
print(df.describe())

# Live data load karo
df_live = pd.read_csv("data/live_students.csv")

print("----- REFERENCE DATA -----")
print(df["marks"].describe())

print("----- LIVE DATA -----")
print(df_live["marks"].describe())