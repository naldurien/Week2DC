# Advent of Code 2020 Challenges

# 1) You have a list of unknown length. Two of its values will sum to 2020. Find# them, multiply them, then return the multiplied value.

def sum_multiple(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            sum = lst[i] + lst[j] 
            if sum == 2020:
                mult = lst[i] * lst[j]
                return mult

testlist = [1977, 1802, 1856, 1309, 2003, 1854, 1898, 1862, 1857, 542, 1616, 1599, 1628, 1511, 1848, 1623, 1959, 1693, 1444, 1211, 1551, 1399, 2010, 1855, 1538, 1869, 1664, 1719, 1241, 1875, 1733, 1547, 1813, 1531, 1773, 624, 10, 1336, 1897, 1179, 1258]

        
# 2) Password Validation - Given a list of passwords, check each to be sure it
# fits within the min/max length promps and contains the required letter at least twice.  Admin should be able to input a custom required letter and custom required min/max lengths.

passwords = ['aAA2424', 'wERI334', 'LIKO332', 'FKE33', 'dfk42p3', 'aaaer34', 'rree324', 'uewo43u', 'eoitn4lka', '32095jfdsklj', 'eoekjlks', 'ljsjste', '3uvdnEE', 'EErhjs', 'OEIRn3']

def pswd_validate(min_len, max_len, letter):
    for i in passwords:
        if len(i) < min_len or len(i) > max_len:
            print(i, " - Invalid password")
        elif  len(i) >= min_len and len(i) <= max_len:
            count = 0
            for j in i:
                if j == letter or j == letter.upper():
                    count += 1
            if count >= 2:
                print(i, " - VALID password")
            else:
                print(i, " - Invalid password")


