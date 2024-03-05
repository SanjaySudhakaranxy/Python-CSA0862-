batch_names = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W',
    24: 'X',
    25: 'Y',
    26: 'Z'
}
batch_number = int(input("Enter a number between 1 and 40: "))
if 1 <= batch_number <= 40:
    batch_name = batch_names[batch_number // 5 + 1]
    print("Batch name:", batch_name)
else:
    print("Invalid input. Please enter a number between 1 and 40.")
