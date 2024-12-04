import re

def concat(input:list):
    return ''.join(input)

def process_line(line: str) -> int:
    # Keep track of whether multiplications are enabled
    enabled = True
    total = 0

    # Position in the string as we process it
    pos = 0

    while pos < len(line):
        # Check for do() instruction
        do_match = re.match(r'do\(\)', line[pos:])
        if do_match:
            enabled = True
            pos += do_match.end()
            continue

        # Check for don't() instruction
        dont_match = re.match(r"don't\(\)", line[pos:])
        if dont_match:
            enabled = False
            pos += dont_match.end()
            continue

        # Check for mul instruction
        mul_match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', line[pos:])
        if mul_match:
            if enabled:
                num1 = int(mul_match.group(1))
                num2 = int(mul_match.group(2))
                total += num1 * num2
            pos += mul_match.end()
            continue

        # Skip any other character
        pos += 1

    return total

def solve_part1(lines: list[str]) -> int:
    total = 0
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    for line in lines:
        matches = re.finditer(pattern, line)
        for match in matches:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            total += num1 * num2

    return total

def solve_part2(lines: list[str]) -> int:
    return process_line(lines)

if __name__ == "__main__":
    with open('day3/input.txt', 'r') as f:
        lines = [line.strip() for line in f]
        string = concat(lines)

    # Part 1
    print(f"Part 1: {solve_part1(lines)}")

    # Part 2
    print(f"Part 2: {solve_part2(string)}")
