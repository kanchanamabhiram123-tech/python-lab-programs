print("Using range:")
for i in range(1, 6):
    print(i)

print("\nUsing enumerate:")
names = ["Abhiram", "Rahul", "Anil"]
for index, name in enumerate(names, start=1):
    print(index, name)

print("\nUsing zip:")
subjects = ["Python", "Math", "English"]
marks = [90, 85, 88]

for subject, mark in zip(subjects, marks):
    print(subject, ":", mark)
