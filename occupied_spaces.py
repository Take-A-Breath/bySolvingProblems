# You supervise a small parking lot which has N parking spaces.
# 
# Yesterday, you recorded which parking spaces were occupied by cars and which were empty.
# 
# Today, you recorded the same information.
# 
# How many of the parking spaces were occupied both yesterday and today?
# Input Specification
# 
# The first line of input contains the integer N ( 1 ≤ N ≤ 100 ) . The second and third lines of input contain N characters each. The second
# line of input records the information about yesterday's parking spaces, and the third line of input records the information about today's
# parking spaces. Each of these 2 N characters will either be C to indicate an occupied space or . to indicate it was an empty parking space.
#
# Output Specification:
# Output the number of parking spaces which were occupied yesterday and today.

n = int(input())
yesterday = input()
today = input()

occupied = 0

for i in range (len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1

print(occupied)
