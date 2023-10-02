import pandas as pd
from datetime import timedelta

""" Reading the data """

df = pd.read_excel("Assignment_Timecard.xlsx")


""" Preprocessing """

# Extracting day from datetime
df["Day"] = df["Time"].map(lambda time: time.day)

# Time difference between start of current shift and end of last shift
df["Shift Difference"] = df["Time"] - df["Time Out"].shift(1)

# Recalculating shift time as Timecard Hours aren't accurate enough
df["Shift Time"] = df["Time Out"] - df["Time"]


""" Task 1 """

df1 = df

# Removing consecutive same days (only considering one shift per day)
df1 = df1[df1["Day"] != df1["Day"].shift(-1)]

# If the difference between current day and the day exactly 7 rows above is 7, then the employee must've worked for 7 consecutive days
df1 = df1[df1["Day"] - df1["Day"].shift(7) == 7]

# Extracting only the name and the position
df1 = df1.loc[:, ["Employee Name", "Position ID"]].drop_duplicates()

print("\n\nEmployees who have worked for 7 consecutive days:\n")
print(df1)


""" Task 2 """

df2 = df

# Considering only the shifts done on the same day as valid (removing false positives)
df2 = df2[df2["Day"] == df2["Day"].shift(1)]

# Only considering and rows with shift difference more than 1 hour
df2 = df2[df2["Shift Difference"] > timedelta(hours=1)]

# Only considering and rows with shift difference less than 10 hours
df2 = df2[df2["Shift Difference"] < timedelta(hours=10)]

# Extracting only the name and the position
df2 = df2.loc[:, ["Employee Name", "Position ID"]].drop_duplicates()

print(
    "\n\nEmployees who have less than 10 hours of time between shifts but greater than 1 hour:\n"
)
print(df2)


""" Task 3 """

df3 = df

# Keeping only the rows with shift time greater than 14 hours
df3 = df3[df3["Shift Time"] > timedelta(hours=14)]

# Extracting only the name and the position
df3 = df3.loc[:, ["Employee Name", "Position ID"]].drop_duplicates()

print("\n\nEmployees who have worked for more than 14 hours in a single shift:\n")
print(df3)
print("\n\n")

# Output stored in output.txt using the command "python script.py > output.txt"
