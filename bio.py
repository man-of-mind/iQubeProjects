first_semester = {
    "GNS 207": 2, 
    "CSC 201": 3, 
    "CSC 203": 1, 
    "CSC 205": 2, 
    "CSC 207": 2, 
    "CSC 209": 3, 
    "CSC 211": 3, 
    "INS 201": 3,
    "INS 223": 2
}

second_semester = {
    "PHY 204": 3,
    "GNS 202": 2,
    "CSC 202": 3,
    "CYB 204": 3,
    "CSC 206": 2,
    "CSC 212": 3,
    "CYB 202": 3,
    "INS 202": 2,
    "INS 216": 1
}

def print_first_semester():
    print("***Enter your first semester results***")
    

def print_second_semester():
    print("***Enter your second semester results***")
    

def calulate_grade(score: int, v: int):
    total = 0
    if score in range(70, 101):
        total += v * 5
    elif score in range(60, 70):
        total += v * 4
    elif score in range(50, 60):
        total += v * 3
    elif score in range(45, 50):
        total += v * 2
    elif score in range(40, 45):
        total += v * 1
    elif score in range(0, 40):
        total += v * 0
    return total


def calculate_gp():
    total = 0
    for k, v in first_semester.items():
        score = int(input("Enter your score in {}: ".format(k)))
        total += calulate_grade(score, v) 
    print_second_semester()
    for k, v in second_semester.items():
        score = int(input("Enter your score in {}: ".format(k)))
        total += calulate_grade(score, v) 
    load = sum(first_semester.values())
    load += sum(second_semester.values())
    CGPA = total/load
    
    return CGPA


database = {}
for val in range(3):
    name = input("Enter your name: ")
    print_first_semester()
    database[name] = calculate_gp()


def find_highest(data: dict):
    highest = 0
    for k, v in data.items():
        if v > highest:
            highest = v
            name = k
    return name, highest

answer = find_highest(database)
print("The person with the highest CGPA is {} with {}.".format(answer[0], answer[1]))
