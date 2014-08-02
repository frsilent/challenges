def main():
    n = 97
    for i in range(0, n):
        if (i % 3) == 0 and (i % 5) == 0:
            print "BooHoo"
        elif (i % 3) == 0:
            print "Boo"
        elif (i % 5) == 0:
            print "Hoo"
        else:
            print i


if __name__ == "__main__":
    main()
