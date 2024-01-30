stack = [None for index in range(10)]
basePointer = 0
topPointer = -1
stackFull = 10
item = None

def showStack():
    for i in range(10):
        print(stack[i], end = ' ')
    print('\nTop Pointer: ', topPointer)

showStack()

def pop():
    global basePointer, topPointer, item
    if topPointer == basePointer - 1:
        print('Stack is empty, cannot pop.')
    else:
        item = stack[topPointer]
        stack[topPointer] = None
        topPointer = topPointer - 1
        showStack()

def push(item):
    global topPointer
    if topPointer < stackFull - 1:
        topPointer = topPointer + 1
        stack[topPointer] = item
        showStack()
    else:
        print('Stack is full, cannot push.')
