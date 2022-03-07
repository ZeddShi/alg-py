
def valid(s):
    stack = []
    for i in s:
        if is_left(i):
            stack.append(i)
        elif is_right(i):
            if not stack:
                return False
            if not is_oppsite(stack[-1], i):
                return False
            stack.pop(-1)
    if not stack:
        return True
    return False


def is_oppsite(v1, v2):
    if v1 == '(' and v2 == ')':
        return True
    elif v1 == '[' and v2 == ']':
        return True
    elif v1 == '{' and v2 == '}':
        return True
    else:
        return False


def is_left(v1):
    if v1 in ('{', '(', '['):
        return True
    return False

def is_right(v1):
    if v1 in ('}', ')', ']'):
        return True
    return False
