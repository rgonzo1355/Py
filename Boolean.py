#!/usr/bin/env python3
# Booleans are 1 0r 0, on or off, and true or false type. 
#12-7-23

child1 = 5
child2 = 8
child3 = 15
child4 = 28
child5 = 28

# 5 != 8
if child1 != child2:
    print('They are not the same age!')
# 28 == 28
elif child4 == child5:
    print('They are the same age!')
# 15 > 15
elif child3 > 15:
    print('The child is older than 15 years old!')
else:
    print('They are different ages!')

