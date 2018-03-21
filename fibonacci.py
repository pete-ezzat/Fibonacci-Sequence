from math import sqrt

def fibonacci(sequence_number):
	# Golden Ratio:
	x = (1 + sqrt(5)) / 2
	y = (1 - sqrt(5)) / 2

	number = int((x**sequence_number - y**sequence_number) / (x-y))

	return number

#.#.#.

def calculate_fibonacci(sequence_number):
	sequence = ''

	for i in range(0, sequence_number+1):
		sequence += str(fibonacci(i)) + ' '

	return sequence

#.#.#.

while True:
	sequence_number = int(input("Sequence number: "))
	print(calculate_fibonacci(sequence_number), '\n')
