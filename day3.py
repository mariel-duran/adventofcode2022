sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def check_rucksack(rucksacks:str):
    rucksacks_list = rucksacks.split()
    shared_items = []
    for rucksack in rucksacks_list:
        half1 = rucksack[slice(0, len(rucksack)//2)]
        half2 = rucksack[slice(len(rucksack)//2, len(rucksack))]
        for x in half1:
            if x in half2:
                if x.islower():
                    shared_items.append(ord(x)-96)
                    break
                else:
                    shared_items.append(ord(x) - 38)
                    break
            continue
    return sum(shared_items)


def check_rucksack1(rucksacks:str):
    rucksacks_list = rucksacks.split()
    grouped_list = [rucksacks_list[i * 3:(i + 1) * 3] for i in range((len(rucksacks_list) + 3 - 1) // 3 )]
    shared_items = []
    for group in grouped_list:
        for x in group[0]:
            if x in group[1] and x in group[2]:
                if x.islower():
                    shared_items.append(ord(x)-96)
                    break
                else:
                    shared_items.append(ord(x) - 38)
                    break
            continue
    return sum(shared_items)



with open("input3.txt") as f:
    content = f.read()

print(check_rucksack1(content))