# kata # 1 - Multiply
def multiply(a, b):
    return a * b


# Kata # 2
sentence = "Hey fellow warriors"
sentenceArray = sentence.split()
reversed_sentence = ""
for sent in sentenceArray:
    if len(sent) > 4:
        reversed_sent = ""
        for char in reversed(sent):
            reversed_sent += char
    else:
        reversed_sent = sent
    if sent == sentenceArray[-1]:
        reversed_sentence += reversed_sent
    else:
        reversed_sentence += reversed_sent + " "
print(reversed_sentence)


# Kata # 3 - Find the odd int
def find_it(seq):
    unique_ints = set(seq)
    frequencies = {}
    for j in seq:
        for z in unique_ints:
            if z == j:
                if frequencies.get(z) is None:
                    frequencies[z] = 1
                else:
                    frequencies[z] += 1
                break
    for freq in frequencies:
        if frequencies[freq] % 2 != 0:
            return freq


# Kata # 4 - Array.diff
def array_diff(a, b):
    if len(a) == 0 or len(b) == 0:
        return a
    for number in b:
        a = list(filter(lambda x: x != number, a))
    return a


# kata # 5 - Create Phone Number
def create_phone_number(n):
    phone_number = '('
    for (idx, i) in enumerate(n):
        if idx == 3:
            phone_number += ') '
        elif idx == 6:
            phone_number += '-'
        phone_number += str(i)
    return phone_number


# kata # 6 - Highest and Lowest
def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    return "{} {}".format(max(numbers), min(numbers))


# kata # 7 - RGB To Hex Conversion
def rgb(r, g, b):
    def int_to_hex(n):
        if n <= 0:
            return '00'
        if 1 <= n < 16:
            return '0' + hex(n)[-1].upper()
        elif n >= 255:
            return 'FF'
        else:
            return hex(n)[2:4].upper()
    return "{}{}{}".format(int_to_hex(r), int_to_hex(g), int_to_hex(b))



