import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read dataset

df = pd.read_csv(r"C:\Users\9\Desktop\EducationDataset_2023-24 (1).csv")

print(df.head())
print(df.columns)

# Highest and lowest number of schools

highest_school = df.loc[df["No of Schools - Total"].idxmax()]
lowest_school = df.loc[df["No of Schools - Total"].idxmin()]

print("District with highest schools:", highest_school["District"])
print("Number of schools:", highest_school["No of Schools - Total"])

print("District with lowest schools:", lowest_school["District"])

print("Number of schools:", lowest_school["No of Schools - Total"])


# Highest total student enrollment

highest_students = df.loc[df["No of Students - Total"].idxmax()]

print("District:", highest_students["District"])
print("Total students:", highest_students["No of Students - Total"])


# Gender difference

df["Gender Difference"] = abs(
    df["No of Students - Boys"] - df["No of Students - Girls"]
)

largest_difference = df.loc[df["Gender Difference"].idxmax()]

print("District:", largest_difference["District"])
print("Gender difference:", largest_difference["Gender Difference"])


# Highest Class X pass percentage

highest_x = df.loc[
    df[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"].idxmax()
]

print("District:", highest_x["District"])
print(
    "Class X pass percentage:",
    highest_x[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"]
)

# Highest Class XII pass percentage

highest_xii = df.loc[
    df["PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"].idxmax()
]

print("District:", highest_xii["District"])
print(
    "Class XII pass percentage:",
    highest_xii["PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"]
)


# Compare Class X and XII pass percentage

x_pass = df[
    " PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"
].mean()

xii_pass = df[
    "PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"
].mean()

print("Average Class X pass percentage:", x_pass)
print("Average Class XII pass percentage:", xii_pass)

plt.figure(figsize=(12,6))

plt.plot(
    df["District"],
    df[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"],
    marker="o",
    label="Class X"
)

plt.plot(
    df["District"],
    df["PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"],
    marker="o",
    label="Class XII"
)

plt.xlabel("District")
plt.ylabel("Pass Percentage")
plt.title("Class X vs Class XII Pass Percentage")

plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()


# Schools vs Class X pass percentage

plt.figure(figsize=(8,5))

plt.scatter(
    df["No of Schools - Total"],
    df[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"]
)

plt.xlabel("Number of Schools")
plt.ylabel("Class X Pass Percentage")
plt.title("Schools vs Class X Pass Percentage")

plt.show()

print(
    "Correlation:",
    df["No of Schools - Total"].corr(
        df[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"]
    )
)


# Students vs Class X pass percentage

plt.figure(figsize=(8,5))

plt.scatter(
    df["No of Students - Total"],
    df[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"]
)

plt.xlabel("Total Students")
plt.ylabel("Class X Pass Percentage")
plt.title("Student Enrollment vs Class X Pass Percentage")

plt.show()

print(
    "Correlation:",
    df["No of Students - Total"].corr(
        df[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"]
    )
)

# Students per school

df["Students per School"] = (
    df["No of Students - Total"] /
    df["No of Schools - Total"]
)

highest_students_per_school = df.loc[
    df["Students per School"].idxmax()
]

print(
    "District with highest students per school:",
    highest_students_per_school["District"]
)

print(
    "Students per school:",
    highest_students_per_school["Students per School"]
)

# print(
#     "Correlation with Class X pass percentage:",
#     df["Students per School"].corr(
#         df[" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"
#     )
# )

plt.figure(figsize=(8,5))

plt.scatter(
    df["Students per School"],
    df[" PASS PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"]
)

plt.xlabel("Students per School")
plt.ylabel("Class X Pass Percentage")
plt.title("Students per School vs Class X Performance")

plt.show()

" PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"

# Observations

print("1. Some districts have a much higher number of schools and student enrollment than others.")

print("2. Class XII pass percentage is generally higher than Class X pass percentage.")

print("3. A higher number of students per school does not necessarily mean better Class X performance.")

# Observations

print("1. Some districts have a much higher number of schools and student enrollment than others.")

print("2. Class XII pass percentage is generally higher than Class X pass percentage.")

print("3. A higher number of students per school does not necessarily mean better Class X performance.")

print(df.columns.tolist())