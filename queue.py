size = input('Enter the size of the queue: ')
queue = [None for index in range(int(size))]
frontPointer = 0
rearPointer = -1
queueFull = len(queue)
queueLength = 0

def display():
    for i in range(queueFull):
        print(i, '  |', queue[i], '|')
    print('Front pointer is at', frontPointer)
    print('Rear pointer is at', rearPointer)
    print('-' * 15)

display()

def enqueue(item):
    global queueLength,  rearPointer
    if queueLength < queueFull:
        if rearPointer < queueFull - 1:
            rearPointer = rearPointer + 1
        else:
            rearPointer = 0
        queueLength = queueLength + 1
        queue[rearPointer] = item
        display()
    else:
        print('Queue is full, cannot enqueue.')

def dequeue():
    global queueLength, frontPointer, item
    if queueLength == 0:
        print('Queue is empty, cannot dequeue.')
    else:
        item = queue[frontPointer]
        queue[frontPointer] = None
        if frontPointer == queueFull - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
        queueLength = queueLength - 1
        display()
