from time import sleep; from re import sub
def readBF (name):
    with open(name, 'r') as f: return sub("[^\[\]+-.,<>]", "", f.read())

def printStack(stack, pointer = -1):
    for i, s in enumerate(stack): print(f"[{s}]" if i == pointer else s, end = " ")
    print()

def getMatch(code, pos, fwd = True):
    if (pos < 0 or pos >= len(code)): print("Array index out of range: " + str(pos)); return
    if (code[pos] != "[" and fwd or code[pos] != "]" and not fwd): print(f"Wrong starting position: code[{pos}] = {code[pos]}"); return 
    openBr = 1
    x = 1 if fwd else -1
    for i in range(pos + x, len(code) if fwd else x, x):
        if code[i] == "[": openBr += 1 * x
        if code[i] == "]": openBr -= 1 * x
        if openBr == 0: return i - pos

def compute(code, show = False, timeStep = 0):
    stack = [0]; pointer = 0; output = ""; i = 0
    while (i < len(code)):
        c = code[i]
        if   c == '>': 
            pointer += 1
            if (pointer >= len(stack)): stack.append(0)
        elif c == '<':
            if (pointer < 0): print("Memory error: -1")
            else: pointer -= 1
        elif c == '+': stack[pointer] = stack[pointer] + 1 if (stack[pointer] <= 255 ) else 0
        elif c == '-': stack[pointer] = stack[pointer] - 1 if (stack[pointer] > 0) else 255
        elif c == '.': output += chr(stack[pointer]); print(chr(stack[pointer]), end = '')
        elif c == ',': stack[pointer] = ord(input("Input: "))
        elif c == ']' and stack[pointer] != 0: i += getMatch(code, i, False)
        elif c == '[' and not stack[pointer]: i += getMatch(code, i)
        if (show): printStack("\n" + stack, pointer); sleep(timeStep)
        i += 1
    print(f"Output: {output}")

code = readBF("test.bf")
compute(code)
