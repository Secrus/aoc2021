import math

with open("input.txt", "r") as input_file:
    crabs = list(map(int, input_file.read().split(",")))


def solution(data):
    best = float("inf")
    best_2 = float("inf")

    for pos in range(min(crabs), max(crabs)+1):
        fuel = sum(list(map(lambda x: math.fabs(x-pos), crabs)))
        fuel_2 = sum(list(map(lambda x: (math.fabs(x-pos) * (math.fabs(x-pos)+1) /2), crabs)))
        if fuel < best:
            best = fuel
        if fuel_2 < best_2:
            best_2 = fuel_2
    return best, best_2

part_1, part_2 = solution(crabs)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")