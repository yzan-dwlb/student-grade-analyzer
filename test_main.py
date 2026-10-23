from main import calculate_avg
from main import find_highest
from main import find_lowest


grades = {
    "statistics" : 75,
}

#assert calculate_avg(grades) == 0
#assert find_lowest(grades) == ("math", 0)
assert find_highest(grades) == ("statistics", 75.0)

#print("Average test passed!")
#print("Lowest test passed!")
print("Highest test passed!")