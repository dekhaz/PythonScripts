##python list sorter

def bubble_sorter(sortee):
    for x in range(len(sortee)-1,0,-1):
        for i in range(x):
            if sortee[i]>sortee[i+1]:
                temp = sortee[i]
                sortee[i] = sortee[i+1]
                sortee[i+1] = temp

test_list = [67,45,2,13,1,998]

bubble_sorter(test_list)
print(test_list)



def my_sorter(sortee):
    for x in range(0,len(sortee), 1):
        for current in range(x):
            #print (sortee[current])
            if sortee[current + 1] > sortee[current]:
                new_val = sortee[current]
                sortee[current] = sortee[current+1]
                sortee[current+1] = new_val


test_list = [67,45,2,13,1,998]

my_sorter(test_list)
print(test_list)





                

