print("30 Days Down -  What did you think?")
for i in range(1, 31):
    thought = input(f"Day {i} was\n")
    result = f"You thought Day {i} was"
    line_2 = f"{thought}"
    print(f"{result: ^35}")
    print(f"{line_2: ^35}")
