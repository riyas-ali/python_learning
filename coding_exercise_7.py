list = [[888, 888, 888],[888, 888, 888],[888, 888, 888]]
column = int(input("Enter the column no:"))
row = int(input("Enter the row no:"))
list[column-1][row-1] = "x"
print(f"{list[0]}\n{list[1]}\n{list[2]}")