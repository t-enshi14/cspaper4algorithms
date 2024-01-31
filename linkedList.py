myLinkedList = [None for index in range(12)]
myLinkedListPointers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]
heapStartPointer = 0
startPointer = -1
nullPointer = -1

def display():
    print("Index | Value | Pointer")
    for index in range(len(myLinkedList)):
        value = myLinkedList[index]
        pointer = myLinkedListPointers[index]
        print(f"{index:5} | {str(value):5} | {pointer:7}")
    print()

display()

def find(itemSearch):
    itemPointer = startPointer
    found = False
    while itemPointer != nullPointer and not found:
        if myLinkedList[itemPointer] == itemSearch:
            found = True
        else:
            itemPointer = myLinkedListPointers[itemPointer]
    return itemPointer

def linkedListAdd(itemAdd):
    global heapStartPointer, startPointer
    if heapStartPointer == nullPointer:
        print('Linked list full')
    else:
        newPointer = heapStartPointer
        heapStartPointer = myLinkedListPointers[heapStartPointer]
        myLinkedList[newPointer] = itemAdd
        myLinkedListPointers[newPointer] = startPointer
        startPointer = newPointer
    display()

def linkedListDelete(itemDelete):
    global heapStartPointer, startPointer
    if startPointer == nullPointer:
        print('Linked list empty')
    else:
        index = startPointer
        oldIndex = nullPointer
        while myLinkedList[index] != itemDelete and myLinkedListPointers[index] != nullPointer:
            oldIndex = index
            index = myLinkedListPointers[index]
        if myLinkedList[index] != itemDelete:
            print('Item', itemDelete, 'not found')
        else:
            if oldIndex == nullPointer:
                startPointer = myLinkedListPointers[index]
            else:
                myLinkedListPointers[oldIndex] = myLinkedListPointers[index]
            myLinkedListPointers[index] = heapStartPointer
            heapStartPointer = index
    display()
