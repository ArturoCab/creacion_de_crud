import random

def binary_search(data, target, low, top, step):
    print("step",step)
    if low>top:
        #print("not found")
        return False
    mid = (low + top) // 2
    if target == data[mid]:
        #print("target is ",data[mid])
        return True
    elif target < data[mid]:
        #print("target is lower than ",data[mid])
        return binary_search(data,target, low, mid - 1, step + 1)
    else:
        #print("target is greater than ",data[mid])
        return binary_search(data,target, mid + 1, top,step + 1)

if __name__ == '__main__':
    #random.seed(0)
    data  = [random.randint(0,100000) for i in range(256)]

    data.sort()
    print(data)

    target = random.randint(0,100000)
    print("target:", target)
    found = binary_search(data, target, 0, len(data)-1,0)

    print("found?>",found)
