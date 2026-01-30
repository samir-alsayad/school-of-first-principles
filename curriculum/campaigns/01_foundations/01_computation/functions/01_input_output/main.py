CHAR_TO_INT_MAP = {
    '0':0, '1':1, '2':2, '3':3, '4':4,'5':5, '6':6, '7':7, '8':8, '9':9
}




def string_to_int(number_string):


    total_len = len(number_string)
    result = 0

    for i, char in enumerate(number_string):


        real_number = CHAR_TO_INT_MAP[char]
        digit_value = real_number * 10 ** (total_len - i - 1)
        result = digit_value + result
    return(result)


print(string_to_int("123") + 100)