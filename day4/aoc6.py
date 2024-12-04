def rotate_matrix(input:list[str], degree:int) -> list[str]:
    assert degree in [0,1,2,3] # 0˚, 90˚, 180˚, 270˚
    def ninety_degree_rotation(input:list[str]) -> list[str]:
        n = len(input)
        rotated = [""] * n
        for i in range(n):
            rotated[i] = "".join(input[n-1-j][i] for j in range(n))
        return rotated

    rotations = {
        0: lambda x: x,
        1: ninety_degree_rotation,
        2: lambda x: ninety_degree_rotation(ninety_degree_rotation(x)),
        3: lambda x: ninety_degree_rotation(ninety_degree_rotation(ninety_degree_rotation(x)))
    }
    return rotations[degree](input)


def detect_xmas(input:list[str]) -> bool:
    assert len(input) == 3
    assert len(input[0]) == 3
    assert len(input[1]) == 3
    assert len(input[2]) == 3
    diag1 = "" + input[0][0] + input[1][1] + input[2][2]
    diag2 = "" + input[2][0] + input[1][1] + input[0][2]
    return True if (
        (
            "MAS" in diag1 #or
            # "SAM" in diag1
        ) and (
            "MAS" in diag2 #or
            # "SAM" in diag2
        )
    ) else False


def main(input:list[str], debug=True) -> int:
    sum = 0
    in_length = len(input)
    in_width = len(input[0])

    # first iterate over the three rotations
    for i in [0,1,2,3]:
        rotated = rotate_matrix(input, i)
        for y in range(in_length - 2):
            for x in range(in_width - 2):
                selection = []
                for k in range(3):
                    selection.append(rotated[y+k][x:x+3])
                if detect_xmas(selection):
                    sum += 1

    return sum

if __name__ == "__main__":
    with open('day4/input.txt', 'r') as f:
        biglist = list()
        for line in f:
            row = line.strip().split()
            biglist.append(row[0])

    print("test")
    test_list = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
    ]

    print(
        main(test_list)
    )

    print("challenge")
    print(
        main(biglist)
    )
