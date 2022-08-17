def find_max(arrr_of_numbers):
    max_number = arrr_of_numbers[0]
    for number in arrr_of_numbers:
        if number > max_number:
            max_number = number
    return max_number
