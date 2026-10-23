from main import calculate_avg, find_highest, find_lowest

grades = {
    "math": 90,
    "python": 80,
    "statistics": 100
}

assert calculate_avg(grades) == 90
assert find_highest(grades) == ("statistics", 100)
assert find_lowest(grades) == ("python", 80)
assert calculate_avg({}) == 0
assert find_highest({"math": 0, "python": 0}) == ("math", 0)
assert find_lowest({"statistics": 75}) == ("statistics", 75)

print("All 6 tests passed successfully!")