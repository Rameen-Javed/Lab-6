import pandas as pd
import matplotlib.pyplot as plt

# 1. Create the student dataset
data = {
    "Name": [
        " ali", "SARA ", "bilal", " Ayesha",
        "HAMZA", "zain ", "Noor", " usman "
    ],
    "Marks": ["72", "85", "absent", "64", "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

# 2. Clean student names
df["Name"] = df["Name"].str.strip().str.title()

# 3. Convert marks from text to numbers
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# 4. Replace the absent student's marks with the mean
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

# 5. Display the cleaned DataFrame
print("Cleaned Student Marks:")
print(df)

# 6. Draw the bar plot
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)

plt.tight_layout()

# 7. Save the plot
plt.savefig("marks_bar.png")
plt.show()

print("Saved marks_bar.png")
