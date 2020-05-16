# python3
import sys
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    position = 0
    for i, next in enumerate(text):
        position = i + 1
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((position, next))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                opening_brackets_stack.append((position, next))
                break
            if are_matching(opening_brackets_stack[-1][1],  next):
                opening_brackets_stack.pop()
            else:
                opening_brackets_stack.append((position, next))
                break

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[-1][0]
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
# Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()

# class Bracket:
#     def __init__(self, bracket_type, position):
#         self.bracket_type = bracket_type
#         self.position = position
#         if self.bracket_type == '[' and c == ']':
#             return True
#         if self.bracket_type == '{' and c == '}':
#             return True
#         if self.bracket_type == '(' and c == ')':
#             return True
#         return False


# if __name__ == "__main__":
#     text = sys.stdin.read()
#     opening_brackets_stack = []
#     for i, next in enumerate(text):
#         if next == '(' or next == '[' or next == '{':
#             top = Bracket(next, i)
#             opening_brackets_stack.append([top.bracket_type, top.position])
#         if next == ')' or next == ']' or next == '}':
#             if len(opening_brackets_stack) == 0:
#                 print(i + 1)
#                 sys.exit()
#             top = Bracket(
#                 opening_brackets_stack[-1][0], len(opening_brackets_stack) - 1)
#             if not top.Match(next):
#                 print(i + 1)
#                 sys.exit()

#             if top.Match(next):
#                 opening_brackets_stack.pop()
#     if opening_brackets_stack != []:
#         print(opening_brackets_stack[0][1] + 1)
#     else:
#         print("Success")
