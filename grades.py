from statistics import mean
void = 0
num = 1
quanSubjects = int(input("How many subjects? "))
subjects = []
for i in range(quanSubjects):
    subjects.append(input(("Subject number ", num)))
    num = (num++1)

grade = []
grades_dict = dict.fromkeys(subjects)
for i in subjects:
    grade = []
    print ([subjects[void]])
    quanGrades = int(input("How many grades for subject listed above? "))
    for i in range(quanGrades):
        grade.append(float(input("Grades for the above subject: ")))
    grades_dict[subjects[void]] = (grade)
    void = (void++1)

for st,vals in grades_dict.items():
    print ("Average for {} is {}".format(st,mean(vals)))

avg_dict = {}
void = 0

for st,vals in grades_dict.items():
    avg = (mean(vals))
    avg_dict[subjects[void]] = avg
    void = (void++1)

avg_final = [*avg_dict.values()]

def Average(avg_final):
    return sum(avg_final) / len(avg_final)

print ("The overall average is: ", Average(avg_final))