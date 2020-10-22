# binary insertion example

example_list: list = [4,6,5,8,10,1,12,24,11,5,5,5,5,12,12,15]

for i in range(len(example_list)):
    # only considers the range from 0 to i as I gets bigger 
    for j in range(0,i):
        # if the next in line is smaller than the one before, switch them
        if example_list[i-j] <= example_list[i-j-1]:
            example_list[i-j-1], example_list[i-j] = example_list[i-j], example_list[i-j-1]

# element to put into the list in the correct place
element: int = 25

inserted = False
low = 0
high = len(example_list)-1
mid = int((low+high)/2)

# takes care of the edge cases that the element is the highest or lowest in the list

if element > example_list[high]: # element is the highest on the list
    print('Element is the highest on the list')
    example_list.append(element)
elif element < example_list[low]: # element is the lowest on the list
    print('Element is the lowest on the list')
    example_list.insert(0, element)


while inserted == False:
    # found codition
    if element >= example_list[mid] and element <= example_list[mid+1]:
        print('Element inserted')
        example_list.insert(mid+1,element)
        inserted = True
    elif element < example_list[mid]:
        # condenses the search area to low - mid
        high = mid
    elif element > example_list[mid]:
        # condenses the search area to mid - high
        low = mid
    else:
        print('Error')
        inserted = True

    mid = int((low+high)/2)





