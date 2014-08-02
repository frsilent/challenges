"""
J Delta
Given N numbers , [N<=10^5] you'll need to count the number of pairs of numbers which have a delta / difference of D.
[D>0 and D<10^9]. Your program should have as low of a computational time complexity as possible.

Input Format:
First line contains N & D (integers).
Second line contains N numbers. All the N numbers are distinct.

Output Format:
One integer: number of pairs of numbers that have a delta of D.

Sample Input #00:
6 2
1 12 5 3 4 2

Sample Output #00:
3
Explanation:
The pairs are (5,3), (4,2) and (3,1).

Sample Input #01:
10 1
363374226 364147430 61825063 1073065618 1281246124 1399469812 428047535 491595154 879792081 1069262693

Sample Output #01:
0

Explanation:
There are no such pairs.

"""


def main():
    n, delta = raw_input().split()
    inputs = map(int, raw_input().split())
    delta = int(delta)

    pairs = []

    for i in inputs:
        for j in inputs:
            if abs(i - j) == delta:
                pairs.append([i, j])

    for i in pairs:
        print i

if __name__ == "__main__":
    main()
