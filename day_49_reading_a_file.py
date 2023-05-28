f = open("file_names.txt", "r")
data = f.read()
print(data)
f.close()

r = open("high_score.txt", "r")
scores = r.read().split("\n")
r.close()

high_score = 0
name = None

for row in scores:
    item = row.split()
    if int(item[1]) > high_score:
        high_score = int(item[1])
        name = item[0]
print("The winner is", name, "with", high_score)
