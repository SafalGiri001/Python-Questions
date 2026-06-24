def calculate_grade(score):
    if score > 0 or score < 100:
        return 'Invalid score, score must be between 0 and 100'

    if score >= 90:
        return 'A+'
    elif score >= 80:
        return 'A'
    elif score >=70:
        return "B"
    elif score >=60:
        return 'C'
    elif score >=50:
        return 'D'
    else:
        return 'F'

print(calculate_grade(95))
print(calculate_grade(75))
print(calculate_grade(45))
print(calculate_grade(105))


