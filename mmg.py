import sys


def main(expression: str, notes: str) -> str:
	number_list = parse(expression)
	notes_list = notes.split()
	base: int = len(notes_list)
	number_list = convert(number_list, base)
	return generate(number_list, notes_list)


def parse(expression: str) -> list:
	return [int(c) for c in expression if c.isdigit()]


def convert(number_list, base: int) -> list:
	converted_number = []
	for d in number_list:
		converted_number.append(d % base)
	return converted_number


def generate(numbers: list, notes: str) -> str:
	melody = []
	for i in numbers:
		melody += notes[i]
	melody = ' '.join(melody)
	return melody


if __name__ == '__main__':
	print(main(sys.argv[1], sys.argv[2]))
