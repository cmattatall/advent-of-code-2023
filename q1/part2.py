

def is_number(string: str) -> bool:
    return string.isnumeric()

numbers_table = {
    "0": "0",
    "zero": "0",
    "1": "1",
    "one": "1",
    "2": "2",
    "two": "2",
    "3": "3",
    "three": "3",
    "4": "4",
    "four": "4",
    "5": "5",
    "five": "5",
    "6": "6",
    "six": "6",
    "7": "7",
    "seven": "7",
    "8": "8",
    "eight": "8",
    "9": "9",
    "nine": "9" 
}



READ_BUFFER_LEN = 0
for key in numbers_table.keys():
    key_len = len(key)
    if key_len > READ_BUFFER_LEN:
        READ_BUFFER_LEN = key_len

def calculate_line_sum(numbers: list[str]) -> int:
    first = numbers_table[numbers[0]]
    last = numbers_table[numbers[-1]]
    line_sum = int(first + last)
    return line_sum




def main() -> None:
    with open("./q1/input.txt", "r") as file:
        total_sum = 0

        line_index = 0
        for line in file:
            found_numbers = []
            for search_index in range(len(line) - READ_BUFFER_LEN):
                view = line[search_index: search_index + READ_BUFFER_LEN]

                for number_text, number_string in numbers_table.items():
                    number_index = view.find(number_text, line_index)
                    if number_index == -1:
                        continue
                    number_index += len(number_string)
                    found_numbers.append(number_string)
            total_sum += calculate_line_sum(found_numbers)

    print(total_sum)
            

main()


