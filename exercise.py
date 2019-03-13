def ordinal_indicator(num):
    indicator = ""
    num_string = str(num)
    if num == 1 or num_string.endswith('1'):
        indicator = str(num) + "st"
    elif num == 2 or num_string.endswith('2'):
        indicator = str(num) + "nd"
    elif num == 3 or num_string.endswith('3'):
        indicator = str(num) + "rd"
    else:
        indicator = str(num) + "th"
    return indicator

# Testing
# number = ordinal_indicator(1)
# print(number)
# number = ordinal_indicator(2)
# print(number)
# number = ordinal_indicator(3)
# print(number)
# number = ordinal_indicator(4)
# print(number)
# number = ordinal_indicator(5)
# print(number)
# number = ordinal_indicator(21)
# print(number)
# number = ordinal_indicator(22)
# print(number)
# number = ordinal_indicator(23)
# print(number)
# number = ordinal_indicator(33)
# print(number)
# number = ordinal_indicator(34)
# print(number)
# number = ordinal_indicator(35)
# print(number)
# number = ordinal_indicator(101)
# print(number)
