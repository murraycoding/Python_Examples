# selection sort notes

example_list: list = [4,6,5,8,10,1,12,24,11,12,12,15]

for i in range(len(example_list)):
    # sets the first element as the "lowest"
    low = example_list[i]
    low_index = i
    
    # loops through a smaller an smaller sublist of the elements
    for j in range(i,len(example_list)):
        # if an element is lower than the "lowest" call the new one the lowest
        if example_list[j] < low:
            low = example_list[j]
            low_index = j
    
    # select the lowest and move it to the next lowest spot in line
    example_list[i], example_list[low_index] = example_list[low_index], example_list[i]

print(example_list)    
