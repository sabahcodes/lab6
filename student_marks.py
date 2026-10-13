import pandas as pd
import matplotlib.pyplot as plt

# Messy data
names = [" ali", "SARA ", "bilal", " Ayesha", "HAMZA", "zain ", "Noor", " usman "]
marks = ["72", "85", "absent", "64", "90", "78", "81", "69"]

df = pd.DataFrame({"Name": names, "Marks": marks})

# (a) Name ko clean karo
df["Name"] = df["Name"].str.strip().str.title()

# (b) Marks ko number banao, "absent" NaN ban jata hai, phir mean se fill karo
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# (c) Cleaned DataFrame print karo
print(df)

# (d) Bar plot
plt.figure(figsize=(7, 4))
plt.bar(df["Name"], df["Marks"], color="steelblue")
plt.title("Marks per Student")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("marks_bar.png")
plt.show()
print("Saved marks_bar.png")