def getInversedNumber(decimal):
    binary_rep = bin(decimal)[2:]  # Casts to binary & removes 0b prefix
    binary_rep = binary_rep.zfill(8)

    inverse = ''.join('1' if i == '0' else '0' for i in binary_rep)  # Reverse
    return int(inverse, 2)


def main():
    print getInversedNumber(50)

if __name__ == "__main__":
    main()
