def isBalanced(self, num: str) -> bool:
    even = 0
    odd = 0

    for i, char in enumerate(num):
        if i % 2 == 0:
            even += int(char)
        else:
            odd += int(char)

    if even == odd:
        return True
    else:
        return False