sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def assignment_checker(assignment_string:str):
    assignment_list = [x.split(",") for x in assignment_string.splitlines()]
    print(assignment_list)
    overlapping = 0
    for list in assignment_list:
        assignment1 = [int(x) for x in list[0].split("-")]
        range1 = range(assignment1[0], assignment1[1]+1)
        print(range1)
        assignment2 = [int(x) for x in list[1].split("-")]
        range2 = range(assignment2[0], assignment2[1]+1)
        for area in range1:
            if area not in list(range2):
                print("hola")




assignment_checker(sample)