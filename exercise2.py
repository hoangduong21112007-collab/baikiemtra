import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["An", "Binh", "Cuong", "Dung", "Hoa"],
    "age": [20, 21, 19, 22, 20],
    "score": [8.5, 6.0, 9.0, 4.5, 7.5]
}

df = pd.DataFrame(data)

print("tất cả sinh viên:")
print(df)

df.to_csv("students.csv", index=False)

print("\nData saved to students.csv successfully!")

df = pd.read_csv("students.csv")

print(df)

print("\nHiển thị các sinh viên có điểm >= 8:")

high_score = df[df["score"] >= 8]
print(high_score)

average_score = df["score"].mean()

print("\nAverage score:", average_score)

df["result"] = df["score"].apply(
    lambda x: "Pass" if x >= 5 else "Fail"
)

print(df)

df.to_csv("students.csv", index=False)

print("\nUpdated data saved successfully!")
