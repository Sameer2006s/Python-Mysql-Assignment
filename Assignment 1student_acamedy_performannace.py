import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create dataset

data = {
    "Semester": [
        1,1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,2,2,
        3,3,3,3,3,3,3,3,3,3,
        4,4,4,4,4,4,4,4,4,4,
        5,5,5,5,5,5,5,5,5,
        6,6,6,6,6,6,6,6,6
    ],

    "Subject": [
        "Engineering Chemistry",
        "Engineering Mathematics-I",
        "Fundamentals of Electrical Engineering",
        "Programming for Problem Solving",
        "Environment and Ecology",
        "Engineering Chemistry Lab",
        "Basic Electrical Engineering Lab",
        "Programming for Problem Solving Lab",
        "Engineering Graphics & Design Lab",

        "Engineering Physics",
        "Engineering Mathematics-II",
        "Fundamentals of Electronics Engineering",
        "Fundamentals of Mechanical Engineering",
        "Soft Skills",
        "Engineering Physics Lab",
        "Basic Electronics Engineering Lab",
        "English Language Lab",
        "Workshop Practice Lab",
        "Sports and Yoga",

        "Material Science",
        "Technical Communication",
        "Data Structure",
        "Computer Organization and Architecture",
        "Discrete Structures & Theory of Logic",
        "Cyber Security",
        "Data Structure Lab",
        "Computer Organization and Architecture Lab",
        "Web Designing Workshop",
        "Internship Assessment / Mini Project",

        "Mathematics-IV",
        "Universal Human Values and Professional Ethics",
        "Operating System",
        "Theory of Automata and Formal Languages",
        "Object Oriented Programming with Java",
        "Python Programming",
        "Operating System Lab",
        "Object Oriented Programming with Java Lab",
        "Cyber Security Workshop",
        "Sports and Yoga-II",

        "Database Management System",
        "Web Technology",
        "Design and Analysis of Algorithm",
        "Object Oriented System Design with C++",
        "Data Warehousing & Data Mining",
        "Database Management System Lab",
        "Web Technology Lab",
        "Design and Analysis of Algorithm Lab",
        "Mini Project or Internship Assessment",

        "Software Engineering",
        "Game Design",
        "Computer Networks",
        "Blockchain Architecture Design",
        "Idea to Business Model",
        "Software Engineering Lab",
        "Game Design Lab",
        "Computer Networks Lab",
        "Essence of Indian Traditional Knowledge"
    ],

    "Internal": [
        26,24,25,24,25,43,42,41,43,
        24,23,23,23,26,40,39,44,38,78,
        26,26,26,26,26,26,44,43,43,55,
        26,27,27,27,26,28,46,45,44,90,
        26,26,26,26,26,43,43,44,92,
        27,28,27,28,27,45,47,46,26
    ],

    "External": [
        33,47,42,44,30,43,43,43,44,
        33,31,41,24,36,39,40,45,42,0,
        28,37,32,44,26,50,43,43,43,0,
        30,41,52,27,39,34,46,45,44,0,
        36,37,33,46,46,41,42,41,0,
        45,35,50,52,47,44,43,44,42
    ]
}


df = pd.DataFrame(data)

df["Total Marks"] = df["Internal"] + df["External"]


# Number of semesters

print("Number of semesters:", df["Semester"].nunique())


# Total number of subjects

print("Total subjects:", len(df))


# Highest marks

print("Highest marks:", df["Total Marks"].max())


# Lowest marks

print("Lowest marks:", df["Total Marks"].min())


# Semester with highest total marks

semester_total = df.groupby("Semester")["Total Marks"].sum()

print("Highest total marks semester:", semester_total.idxmax())


# Semester with lowest total marks

print("Lowest total marks semester:", semester_total.idxmin())


# First five records

print(df.head())


# Average marks of each semester

semester_average = df.groupby("Semester")["Total Marks"].mean()

print(semester_average)


# Semester average line graph

plt.figure(figsize=(8,5))

plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Semester Wise Average Marks")

plt.show()


# Subject average bar graph

subject_average = df.groupby("Subject")["Total Marks"].mean()

plt.figure(figsize=(15,7))

plt.bar(
    subject_average.index,
    subject_average.values
)

plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.title("Subject Wise Average Marks")

plt.xticks(rotation=90)

plt.show()


# Highest performing subject

highest_subject = df.loc[df["Total Marks"].idxmax()]

print("Highest performing subject:", highest_subject["Subject"])
print("Marks:", highest_subject["Total Marks"])


# Lowest performing subject

lowest_subject = df.loc[df["Total Marks"].idxmin()]

print("Lowest performing subject:", lowest_subject["Subject"])
print("Marks:", lowest_subject["Total Marks"])


# Best and worst semester

best_semester = semester_average.idxmax()
worst_semester = semester_average.idxmin()

print("Best semester:", best_semester)
print("Worst semester:", worst_semester)


# Improvement from semester 1 to semester 6

sem1_avg = semester_average.loc[1]
sem6_avg = semester_average.loc[6]

improvement = sem6_avg - sem1_avg

print("Semester 1 average:", sem1_avg)
print("Semester 6 average:", sem6_avg)
print("Improvement:", improvement)


# Calculate mean median maximum minimum and standard deviation

marks = df["Total Marks"].to_numpy()

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard deviation:", np.std(marks))


# Performance across semesters

plt.figure(figsize=(8,5))

plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Performance Across Semesters")

plt.show()


# Set target marks

plt.figure(figsize=(8,5))

plt.plot(
    semester_average.index,
    semester_average.values,
    marker="o",
    label="My Performance"
)

plt.axhline(
    y=75,
    linestyle="--",
    label="Target 75%"
)

plt.xlabel("Semester")
plt.ylabel("Average Marks")
plt.title("Performance and Target")

plt.legend()

plt.show()


# Compare with class average

# Class data is not available


# 2x2 dashboard

fig, ax = plt.subplots(2, 2, figsize=(14,10))


ax[0,0].plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

ax[0,0].set_title("Semester Average")
ax[0,0].set_xlabel("Semester")
ax[0,0].set_ylabel("Average Marks")


ax[0,1].bar(
    semester_total.index,
    semester_total.values
)

ax[0,1].set_title("Semester Total Marks")
ax[0,1].set_xlabel("Semester")
ax[0,1].set_ylabel("Total Marks")


ax[1,0].bar(
    ["Highest", "Lowest"],
    [df["Total Marks"].max(), df["Total Marks"].min()]
)

ax[1,0].set_title("Highest and Lowest Marks")
ax[1,0].set_ylabel("Marks")


ax[1,1].plot(
    semester_average.index,
    semester_average.values,
    marker="o"
)

ax[1,1].axhline(
    y=75,
    linestyle="--",
    label="Target 75%"
)

ax[1,1].set_title("Performance vs Target")
ax[1,1].set_xlabel("Semester")
ax[1,1].set_ylabel("Average Marks")

ax[1,1].legend()

plt.tight_layout()
plt.show()


# Observations

print("1. Semester 6 shows good performance.")
print("2. Semester 2 has comparatively lower average marks.")
print("3. The highest marks are obtained in a practical subject.")
print("4. Performance improved from Semester 1 to Semester 6.")
print("5. Semester averages can be compared with the 75% target.")