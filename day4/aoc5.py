def detect_xmas(input:str) -> int:
    xmas_count = input.count('XMAS')
    return xmas_count

def get_diag_char(input:list[str], x:int, y:int) -> str:
    return input[y][x]

def main(input:list[str], debug=False):
    sum = 0
    ltrc = 0
    rtlc = 0
    for row in input:
        # left-to-right
        ltrc += detect_xmas(row)
        # right-to-left
        rtlc += detect_xmas(
            row[::-1]
        )
    print("ltrc: ", ltrc) if debug else None
    print("rtlc: ", rtlc) if debug else None
    sum += rtlc + ltrc


    page_length = len(input)
    page_width = len(input[0])

    # top-to-down & bottom to top
    ttbc = 0
    bttc = 0
    string = ""
    for x in range(page_width):
        for y in range(page_length):
            string = string + input[y][x]
        assert len(string) == page_length
        ttbc += detect_xmas(string)
        bttc += detect_xmas(string[::-1]) # bottom-to-top
        string = ""
    print("ttbc: ", ttbc) if debug else None
    print("bttc: ", bttc) if debug else None
    sum += ttbc + bttc

    # diagonally
    diag_string_list = []
    for x in range(page_length):
        y = 0
        tl_ret_str = ""
        br_ret_str = ""
        while x >= 0 and y >= 0:
            tl_ret_str = tl_ret_str + get_diag_char(input, x, y)
            br_ret_str = br_ret_str + get_diag_char(input, page_width-1-x, page_length-1-y)
            x -= 1
            y += 1
        diag_string_list.append(tl_ret_str)
        diag_string_list.append(br_ret_str)

    # print("/", diag_string_list)
    # print("/", [len(x) for x in diag_string_list])

    tlbrc = 0
    brtlc = 0
    for row in diag_string_list[:-1]: # the last row is duplicated, so remove it (largest diagonal)
        # TL to BR
        tlbrc += detect_xmas(row)
        # BR to TL
        brtlc += detect_xmas(
            row[::-1]
        )
    print("tlbrc: ", tlbrc) if debug else None
    print("brtlc: ", brtlc) if debug else None
    sum += tlbrc + brtlc

    diag_string_list = []
    for x in range(page_length):
        y = page_length-1
        bl_ret_str = ""
        tr_ret_str = ""
        while x >= 0 and y >= 0:
            bl_ret_str = bl_ret_str + get_diag_char(input, x, y)
            tr_ret_str = tr_ret_str + get_diag_char(input, page_width-1-x, page_length-1-y)
            x -= 1
            y -= 1
        diag_string_list.append(bl_ret_str)
        diag_string_list.append(tr_ret_str)

    # print("\\", diag_string_list)
    # print("\\", [len(x) for x in diag_string_list])

    trblc = 0
    brtlc = 0
    for row in diag_string_list[:-1]: # the last row is duplicated, so remove it (largest diagonal)
        # TR to BL
        trblc += detect_xmas(row)
        # BR to TL
        brtlc += detect_xmas(
            row[::-1]
        )
    print("trblc: ", trblc) if debug else None
    print("brtlc: ", brtlc) if debug else None
    sum += trblc + brtlc
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
        main(test_list, debug=False)
    )

    print("challenge")
    print(
        main(biglist)
    )
