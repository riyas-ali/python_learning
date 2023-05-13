birthYear = int(input("What year were you born?"))
if birthYear <= 1946:
    print("You are a Traditionalist.")
elif 1947 <= birthYear <= 1964:
    print("Hey, Baby Boomer! How you doing?")
elif 1965 <= birthYear <= 1981:
    print("Gen X! What's up?")
elif 1982 <= birthYear <= 1995:
    print("Millenials! The age of tech!")
elif birthYear >= 1996:
    print("Hey, Gen Z! TikTok much?")
else:
    print("Try again!")
