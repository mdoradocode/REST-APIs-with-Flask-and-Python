##used in a key value pair
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
##Dictionary with 3 key value pairs
friend_ages["Bob"] = 20
##This accesses the "Bob" Key and adds the value. if the key already exist, then you can just use the existing key and modify its value

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]
##A list of dicitonaries

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")
# Better
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values))
