import sys
n = 30
myDyanamicArray = []
for i in range(n):
    myLenth = len(myDyanamicArray)
    myByte = sys.getsizeof(myDyanamicArray)
    print(f"Length: {myLenth} Byte: {myByte}")
    myDyanamicArray.append(n)
