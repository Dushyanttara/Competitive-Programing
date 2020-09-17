def isHappy(n):
    words_digits = list(str(n))
    new_num = 0
    for digit in words_digits:
        new_num += int(digit)*int(digit)
    if new_num == 1:
        print("Happy Number")
    else:
        try:
            isHappy(new_num)
        except RecursionError:
            print("unhappy number")


def isHappy(n):
    words = list(str(n))
    new_num = 0
    repeat_digits = set()
    for digit in words:
        new_num += int(digit)*int(digit)
    if new_num in repeat_digits:
        return False
    elif new_num == 1:
        return True 
        repeat_digits.add(new_num)
        isHappy(new_num)

def isHappy(n) :
    repeat_list = []
    words_digits = list(str(n))
    new_num = 0
    for digit in words_digits:
        new_num += int(digit)*int(digit)
    
    if new_num != 1:
        if new_num in repeat_list:
            return False
        else:
            repeat_list.append(new_num)
            isHappy(new_num)
    else:
        return True

def numSquare(n):
    """Utility function to return sum of square of all digits of a number

    Args:
        n (integer): Input number whose digits need to be squared and summed

    Returns:
        square_sum: Output with the square sum of all digits of n.
    """
    digits = list(str(n))
    square_num = 0
    for digit in digits:
        square_num += int(digit)*int(digit)

    return square_num

#test1 = 15
#test2 = 121212
#sss1 = numSquare(test1)
#ss2 = numSquare(test2)

#print(sss1, ss2)
def isHappy(n):
    s = set()
    set.add(n)

    while True:
        if (n==1):
            return True
        n = numSquare(n)

        if n is s:
            return False
        
        s.add(n)
    return False


"""
class Solution:
    def __init__(self):
        self.repeat_list = []
        self.new_num = 0

    def isHappy(self, n: int) -> bool:
        words_digits = list(str(n))
        for digit in words_digits:
            self.new_num += int(digit)*int(digit)
        
        if self.new_num != 1:
            if self.new_num in self.repeat_list:
                return "this is an unhappy no."#return False
            else:
                self.repeat_list.append(self.new_num)
                self.isHappy(self.new_num)
        else:
            return "this is a happy no."#return True
param_1 = 19
ret = Solution().isHappy(param_1)
print(ret)
"""