import requests

for i in range(10):
    result = requests.get('https://randomuser.me/api/')
    if result.status_code != 200:
        print("Couldn't get Api!")
    else:
        user = result.json()
        for person in user['results']:
            file_name = f"{person['name']['first'].lower()}_{person['name']['last'].lower()}.jpg"
            picture = requests.get(person["picture"]["large"])
            f = open(file_name, "wb")
            f.write(picture.content)
            f.close()
            print(f"Saved {file_name}")
