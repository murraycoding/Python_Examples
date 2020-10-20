# insertion sort notes

example_list_1: list = [1,4,6,5,8,10,12,24,11,12,12,15]

for i in range(len(example_list_1)):
    # only considers the range from 0 to i as I gets bigger 
    for j in range(0,i):
        # if the next in line is smaller than the one before, switch them
        if example_list_1[j+1] < example_list_1[j]:
            example_list_1[j], example_list_1[j+1] = example_list_1[j+1], example_list_1[j]

