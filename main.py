# `card name`: `winning_numbers` | `our_numbers`

INFILE = "input.txt"
# INFILE = "example.txt"


def main():
    with open(INFILE, 'r') as f:
        process_file(f.readlines())



def process_file(lines):
    points = 0
    for line in lines:
        split_line = line[line.find(":") + 1:].strip().split('|')

        winning_numbers = [number for number in split_line[0].split(' ') if number]
        our_numbers = [number for number in split_line[1].split(' ') if number]

        matches = set(winning_numbers) & set(our_numbers)
        if matches:
            points += 2 ** (len(matches) - 1)
    print("points: " + str(points))



if __name__ == "__main__":
    main()
