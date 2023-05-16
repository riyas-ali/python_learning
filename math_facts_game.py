print("Math fact game")
number = int(input("Name your multiples: "))
right_answers = 0
for i in range(1, 11):
    answer = number * i
    print(i, "x", number)
    user_answer = int(input(">: "))
    if user_answer == answer:
        print("You got it right!")
        right_answers += 1
    else:
        print("That's not correct. It should have been", answer)

if right_answers == 10:
    print("Wow! A perfect score! 🥳")
else:
    print("You got", right_answers, "out of 10 correct.")