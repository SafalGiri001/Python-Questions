applicant = {"name": "Priya", "skills":["Java", "SQL"], "experience_years":1}
required_skills = {"Python","Java"}
applicant_skills = set(applicant['skills'])
common_skills = required_skills.intersection(applicant_skills)
if (common_skills in required_skills) and applicant["experience_years"] >= 2:
    print("Priya qualifies")
else:
    print("Priya does not qualify")