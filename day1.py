# Day 1: Calorie Counting


def calorie_count(calorie_list:str):
    elf_calorie_list =[]
    for line in calorie_list.split("\n\n"):
        elf_calorie_list.append(sum([int(num) for num in line.split("\n")]))
    return elf_calorie_list


with open("input1.txt") as f:
    content= f.read()

calorie_list = calorie_count(content)

calorie_list.sort(reverse=True)

print(f"Top calories: {max(calorie_count(content))}")

top_three = [num for num in calorie_list[0:3]]

print(f"Sum of top 3: {sum(top_three)}")




