from time import sleep
import re
stack = [0]

def readBF (name):
    code = ""
    with open(name, 'r') as f:
        for line in f:
            code += line.strip()
    return re.sub("[^\[\]+-.,<>]", "", code)

def printStack(stack, pointer = -1):
    for i, s in enumerate(stack):
        print(f"[{s}]" if i == pointer else s, end = " ")
    print()

def getMatch(code, pos, forward = True):
    openBr = 1
    if (pos < 0 or pos >= len(code)):
        print("Array index out of range: " + str(pos))
        return

    if forward:
        if (code[pos] != "["):
            print("Wrong starting position: " + str(pos))
            return 

        for i in range(pos + 1, len(code)):
            if code[i] == "[":
                openBr += 1
            if code[i] == "]":
                openBr -= 1
            if openBr == 0:
                return i - pos
    else:
        if (code[pos] != "]"):
            print("Wrong starting position: " + str(pos))
            return 

        for i in range(pos - 1, -1, -1):
            if code[i] == "[":
                openBr -= 1
            if code[i] == "]":
                openBr += 1
            if openBr == 0:
                return i - pos

def getSubCode(code, pos):
    return code[pos + 1 : getMatch(code, pos) + pos]

def compute(code, show = False):
    global stack
    pointer = 0
    output = ""
    offset = 0

    i = 0
    while (i + offset < len(code)):
        c = code[i + offset]
        if c == '>':
            pointer += 1
            if (pointer >= len(stack)):
                stack.append(0)
        if c == '<':
            pointer -= 1
            if (pointer < 0):
                print("Memory error: -1")
        if c == '+':
            stack[pointer] += 1
        if c == '-':
            stack[pointer] -= 1
            if stack[pointer] < 0: stack[pointer] = 255
        if c =='.':
            output += chr(stack[pointer])
            #print(f"Output: {output}")
        if c ==',':
            stack[pointer] = ord(input("Input: "))
        if c == ']':
            if stack[pointer] != 0:
                offset += getMatch(code, i + offset, False)
        if c == '[':
            if stack[pointer] == 0:
                 offset += getMatch(code, i + offset)
        
        if (show):
            printStack(stack, pointer)
            #sleep(0.1)
        i += 1

    print(f"Output: {output}")

code = readBF("test.bf")
compute(code)
