from quizA_others import sum_of_odd_place, prefix_matched, get_prefix


def is_valid(number):
    return (sum_of_odd_place(number) + sum_of_double_even_place(number)) % 10 == 0


def sum_of_double_even_place(number):
    total = 0
    s = str(number)
    for i in range(-2, -len(s) - 1, -2):
        doubled = (int(s[i]) * 2)
        d_s = str(doubled)
        if len(d_s) == 2:
            total += int(d_s[0]) + int(d_s[1])
        else:
            total += doubled
    return total


def get_digit(number):
    total = 0
    for num in str(number):
        total += int(num)
    return total


def get_size(d):
    return len(str(d))


cc = 4388576018402626
print sum_of_double_even_place(cc)
print get_digit(2)
print get_digit(12)
print get_size(4)
print get_size(37)
print is_valid(cc)
for i in [4388576018410707, 371826291433349, 5411045872559122, 6011432717792989]:
    print is_valid(i)
