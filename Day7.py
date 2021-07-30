#First list to choose the students name
list1 = ["athish", "siddharth", "dennis", "haarvish"]
list2 = [52, 49, 69, 61]

res = str(list1) [1:-1]

res = "\n".join("{} {}".format(x, y) for x, y in zip(list1, list2))

print( res)
