def calculate_grade(subjects):
    total = 0
    for subject, score in subjects.items():
        if score < 0 or score > 100:
            return "Unrecognized marks/avg"
        total += score

    average = total / len(subjects)

    if 0 <= average <= 30:
        return "D"
    elif 31 <= average <= 50:
        return "C"
    elif 51 <= average <= 70:
        return "B"
    elif 71 <= average <= 100:
        return "A"
    else:
        return "Unrecognized marks/avg"

# Input scores for each subject
math_score = int(input("Enter Math score: "))
physics_score = int(input("Enter Physics score: "))
geo_score = int(input("Enter Geography score: "))
chem_score = int(input("Enter Chemistry score: "))

# Create a dictionary of subjects and their scores
subjects = {"Math": math_score, "Physics": physics_score, "Geography": geo_score, "Chemistry": chem_score}

# Calculate the average grade and display the result
grade = calculate_grade(subjects)
print(f"Average Grade: {grade}")
