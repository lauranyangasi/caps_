colors = {
    "red": "rot",
    "green": "grun",
    "blue": "blau",
    "yellow": "gelb"
}
print(colors)
eng_color = input("please input english color: ")
ger_color = input("please input germany translation: ")
colors[eng_color] = ger_color

print(colors)

say_color = input("Which color should be translated?: ")
print("The German word for", say_color, "is", colors[say_color])