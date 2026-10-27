import pandas as pd

data = pd.DataFrame({
    "Age": [19, 19, 20, 20, 21, 21],
    "City": ["Delhi", "Delhi", "Delhi", "Delhi", "Delhi", "Delhi"],
    "Course": ["CS", "CS", "CS", "CS", "CS", "CS"],
    "Score": [82, 85, 74, 77, 91, 88]
})

# Generalize age into groups of 2 years.
data["Age_Group"] = (data["Age"] // 2) * 2
data = data.drop(columns=["Age"])

quasi_identifiers = ["Age_Group", "City", "Course"]
group_sizes = data.groupby(quasi_identifiers).size()

print("Anonymized dataset:")
print(data.to_string(index=False))
print("
Equivalence-class sizes:")
print(group_sizes)

k = 2
print(f"
Target k = {k}")
print("K-anonymity satisfied:",
      bool((group_sizes >= k).all()))
