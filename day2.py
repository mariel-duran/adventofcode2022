# Day 2: Rock Paper and Scissors

sample_input = """A Y
B X
C Z
"""
# part 1
# choices = {"A": ["Rock", 1], "B": ["Paper", 2], "C": ["Scissors", 3],
# #            "X": ["Rock", 1], "Y": ["Paper", 2], "Z": ["Scissors", 3]}
outcome = {"draw": 3, "lost": 0, "won": 6}

# part 2

choices = {"A": ["Rock", 1], "B": ["Paper", 2], "C": ["Scissors", 3],
           "X": [1, "lost"], "Y": [0, "draw"], "Z": [2, "won"]}

result_matrix = [
    # rock paper scissors  0 = draw, 1 = lose, 2 = win
    [0, 2, 1],
    [1, 0, 2],
    [2, 1, 0]
]


def total_score(strategy_guide:str):
    plays = strategy_guide.splitlines()
    result = 0
    for play in plays:
        draw = play.split()
        # part 1
        # if result_matrix[choices[draw[0]][1]-1][choices[draw[1]][1]-1] == 0:
        #     result += choices[draw[1]][1] + outcome["draw"]
        # elif result_matrix[choices[draw[0]][1]-1][choices[draw[1]][1]-1] == 2:
        #     result += choices[draw[1]][1] + outcome["won"]
        # else:
        #     result += choices[draw[1]][1] + outcome["lost"]

        # part 2
        x = len(result_matrix[choices[draw[0]][1]-1])
        for y in range(x):
            if result_matrix[choices[draw[0]][1]-1][y] == choices[draw[1]][0]:
                result += (y+1) + outcome[choices[draw[1]][1]]
            else:
                continue

    return result


with open("input2.txt") as f:
    content = f.read()

print(total_score(content))