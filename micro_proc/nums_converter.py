INPUT_SYSTEM = 10
OUTPUT_SYSTEM = 16
INPUT_NUM = "99.53"


def to_dec(base, num, part_type):
    result = 0
    hexdic = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    if part_type == "Целая":
        num = num[::-1]
    for ind in range(len(num)):
        if base == 16:
            if num[ind] in hexdic.keys():
                cur_num = hexdic[num[ind]]
            else:
                cur_num = int(num[ind])
        else:
            cur_num = int(num[ind])
        if part_type == "Целая":
            power = ind
        else:
            power = -ind - 1
        new_term = cur_num * base ** power
        print(f"{cur_num} * {base}^{power} = {new_term}")
        print(f"{result} + {new_term} = {result + new_term}\n")
        result += new_term
    if part_type == "Целая":
        return str(result)
    return str(result)[2:]


def from_dec(base, num, part_type):
    result = ""
    rounders = {2: 9, 16: 5}
    hexdic = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    if part_type == "Целая":
        while num != 0:
            new_num = num % base
            print(f"{num} % {base} = {new_num}")
            if new_num > 9:
                new_num = hexdic[new_num]
            num = num // base
            print(f"Новое число (10): {num}")
            result = str(new_num) + result
            print(f"Текущее число ({base}): {result}\n")
    else:
        while num != 0 and len(result) < rounders[base]:
            new_num = num * base
            print(f"{num} * {base} = {new_num}")
            new_int = int(new_num)
            if new_int > 9:
                new_int = hexdic[new_int]
            result += str(new_int)
            num = new_num - int(new_num)
            print(f"Текущее число: {result}\n")
    return result


def bin_to_hex(num):
    hexdic = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    result = ""
    dot_place = None
    if "." in num:
        int_num, frac_num = num.split(".")[0], num.split(".")[1]
    else:
        int_num, frac_num = num, None
    if len(int_num) % 4 != 0:
        int_num = int_num.zfill(len(int_num) + (4 - len(int_num) % 4))
    num = int_num
    if frac_num is not None:
        if len(frac_num) % 4 != 0:
            frac_num = frac_num.ljust(len(int_num) + (4 - len(int_num) % 4), "0")
        dot_place = len(num) // 4
        num += frac_num
    for ind in range(0, len(num), 4):
        if dot_place is not None and ind // 4 == dot_place:
            result += "."
            dot_place = None
        new_squad = num[ind:ind + 4]
        new_num = int(new_squad, 2)
        if new_num > 9:
            new_num = hexdic[new_num]
        print(f"{new_squad}(2) = {new_num} (16)")
        result += str(new_num)
        print(f"Текущее число: {result}\n")
    return result


def hex_to_bin(num):
    result = ""
    for symb in num:
        if symb != ".":
            new_num = bin(int(symb, 16))[2:].zfill(4)
            print(f"{symb} (16) = {new_num} (2)")
            result += bin(int(symb, 16))[2:].zfill(4)
            print(f"Текущее число: {result}\n")
        else:
            result += symb
    return result


def num_conv(base_in, base_out, input_num):
    result = ""
    if base_out == 10 or base_in == 10:
        if "." in input_num:
            int_num, frac_num = input_num.split(".")[0], input_num.split(".")[1]
        else:
            int_num, frac_num = input_num, None
        print("Целая часть:")
        if base_out == 10:
            result += to_dec(base_in, int_num, "Целая")
        else:
            result += from_dec(base_out, int(int_num), "Целая")
        if frac_num is not None:
            result += '.'
            print("Дробная часть:")
            if base_out == 10:
                result += to_dec(base_in, frac_num, "Дробная")
            else:
                result += from_dec(base_out, float("0." + frac_num), "Дробная")
    elif base_in == 2 and base_out == 16:
        result = bin_to_hex(input_num)
    elif base_in == 16 and base_out == 2:
        result = hex_to_bin(input_num)
    print(f"Ответ: {result}")
    return result


num_conv(INPUT_SYSTEM, OUTPUT_SYSTEM, INPUT_NUM)