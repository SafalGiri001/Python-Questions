club_A = {"ram", "hari", "shyam"}
club_B = {"ram", "gita", "hari"}

common = club_A.intersection(club_B)

if common:
    print("Following members exist in both groups:", common)
else:
    print("No overlapping members found between groups")