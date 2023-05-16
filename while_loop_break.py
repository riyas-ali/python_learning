print("Fill in the blank lyrics!")
lyrics = input("Never going to ____ you up: ")
count = 1
while True:
  if lyrics == "give":
    break
  count += 1
  lyrics = input("Nope, try again.: ")
print("Never going to give you up", "Well done! It only took you", count,"attempts.")