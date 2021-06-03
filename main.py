import readchar
import os
import sys

screen = []
position = len(screen) - 1
old_pos = position

if len(sys.argv) == 2:
	with open(sys.argv[1]) as f:
		screen = list(f.read())

def add_to_screen(character: str):
	global position, old_pos
	screen.insert(position, character)
	position += 1
	reload_screen()

def remove_from_screen(index: int):
	global position
	position -= 1
	del screen[index]
	reload_screen()

def reload_screen():
	global position
	os.system("cls")
	print_screen = screen[:]
	print_screen.insert(position, "|")
	print("".join(print_screen))

def save_to_file():
	os.system("cls")
	file_name = input("File: ")
	if file_name == "": file_name = sys.argv[1]
	reload_screen()
	with open(file_name, "w") as f:
		f.write("".join(screen))

reload_screen()

while True:
	c = readchar.readkey()

	if c == "\r":
		add_to_screen("\n")
		continue

	if c == "\x1b[D" and position >= 1:
		old_pos = position
		position -= 1
		reload_screen()
		continue

	if c == "\x1b[C" and position < len(screen):
		old_pos = position
		position += 1
		reload_screen()
		continue

	if c == "\x08" and position >= 1:
		remove_from_screen(position-1)
		continue

	if c == "\x13":
		save_to_file()
		continue

	if c == "\x18":
		os.system("cls")
		sys.exit()

	if not c.isprintable():
		continue


	add_to_screen(c)
