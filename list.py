import random

greetings = ["Bonjour", "Hola", "Zdravstvuyte", "Nǐn hǎo", "Salve", "Konnichiwa", "Guten Tag", "Olá", "Anyoung haseyo", "Asalaam alaikum", "Goddag", "Shikamoo", "Goedendag", "Yassas", "Dzień dobry", "Selamat siang", "Namaste, Namaskar", "God dag", "Merhaba", "Shalom", "God dag"]

index = random.randint(1, len(greetings)-1)

print(greetings[index])