'''
Sample Input
10  # number of shoes available 
2 3 4 5 6 8 7 6 5 18  # size of the shoes
6       # no of customers
6 55    # size, prize
6 45
6 55
4 40
18 60
10 50

Sample Output
200

Explanation
Customer 1: Purchased size 6 shoe for $55. 
Customer 2: Purchased size 6 shoe for $45. 
Customer 3: Size 6 no longer available, so no purchase. 
Customer 4: Purchased size 4 shoe for $40. 
Customer 5: Purchased size 18 shoe for $60. 
Customer 6: Size 10 not available, so no purchase.

Total earned: 55 + 45 + 40 + 60 = 200
'''

from collections import Counter

N = int(input())
shoesize = list(map(int, input().split(' ')))
shoecounter = Counter(shoesize)
C = int(input())
netsale = 0
for _ in range(C):
    size, price = map(int,input().split(" "))
    if size in shoecounter.keys() and shoecounter[size]!=0:
        netsale += price
        shoecounter[size] -= 1
print(netsale)
