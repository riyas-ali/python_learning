print("STAR WARS NAME GENERATOR")
first = input("First name: ").strip()
last = input("Last name: ").strip()
maiden = input("Mum's maiden name: ").strip()
city = input("City where you were born: ").strip()

name = f"{first[:3].title()}{last[:2].lower()} {maiden[:2].title()}{city[:-3].lower()}"
print(f"You Star Wars name is {name}")