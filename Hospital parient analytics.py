import numpy as np
import pandas as pd

# Patient data
patients = np.array([
    [25, 120, 80, 72],
    [45, 150, 95, 88],
    [32, 130, 85, 76],
    [60, 170, 110, 92],
    [50, 155, 100, 90]
])


# 1. Average age
average_age = np.mean(patients[:, 0])

print("Average age:")
print(average_age)


# 2. Average systolic and diastolic blood pressure
average_systolic = np.mean(patients[:, 1])
average_diastolic = np.mean(patients[:, 2])

print("\nAverage systolic BP:")
print(average_systolic)

print("Average diastolic BP:")
print(average_diastolic)


# 3. Highest systolic blood pressure
highest_systolic = np.max(patients[:, 1])

print("\nHighest systolic BP:")
print(highest_systolic)


# 4. Lowest systolic blood pressure
lowest_systolic = np.min(patients[:, 1])

print("\nLowest systolic BP:")
print(lowest_systolic)


# 5. Patients with systolic BP greater than 140
high_bp = np.where(patients[:, 1] > 140)

print("\nPatients with systolic BP greater than 140:")
print(high_bp[0] + 1)


# 6. Patients with heart rate greater than 85
high_heart_rate = np.where(patients[:, 3] > 85)

print("\nPatients with heart rate greater than 85:")
print(high_heart_rate[0] + 1)


# 7. Standard deviation of each numerical column
std = np.std(patients, axis=0)

print("\nStandard deviation of each column:")
print(std)


# 8. Classify patients as High or Normal based on systolic BP
status = np.where(
    patients[:, 1] > 140,
    "High",
    "Normal"
)

print("\nPatient BP classification:")
print(status)


# 9. Convert data into Pandas DataFrame
df = pd.DataFrame(
    patients,
    columns=["Age", "Systolic BP", "Diastolic BP", "Heart Rate"]
)

df["Status"] = status

print("\nFinal DataFrame:")
print(df)