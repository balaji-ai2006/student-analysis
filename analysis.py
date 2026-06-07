# Sample Data
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Pooja", "Vikram"],
    "Marks": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Average marks
print("\nAverage Marks:", df["Marks"].mean())

# Topper
topper = df.loc[df["Marks"].idxmax()]
print("\nTopper is:")
print(topper)

# Graph
plt.bar(df["Name"], df["Marks"])
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()