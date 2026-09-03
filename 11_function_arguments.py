def student(name, age=18, *marks, **details):
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)
    print("Other details:", details)

student("Abhiram", 19, 85, 90, 88, course="Python", city="India")
