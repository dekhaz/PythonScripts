import time

def sort_this_list(working_list):
    #this is a simple bubble sort.
    #it is inefficient, comparing every member of the list to every other member
    #one might say that it is the least efficient
    #but it functions, so...
    #step counter is incremented after every line of code in the sort
    basic_step_counter = 0
    for section in range(1,int(len(working_list))):
        for current in range(1,int(len(working_list))):
            basic_step_counter+=1
            if (working_list[current-1] > working_list[current]):
                #store value of lower indexed value
                temp_int = working_list[current-1]
                basic_step_counter+=1
                #move upper indexed value into lower indexed spot
                working_list[current-1] = working_list[current]
                basic_step_counter+=1
                #move stored value to upper indexed spot
                working_list[current] = temp_int
                basic_step_counter+=1
    #print (working_list)
    print ("step counter incremented " + str(basic_step_counter) + " times.")
    return working_list


def better_sorter(working_list):
    #this is an attempt at a better sorting mechanism
    #i will be using some functions of python lists
    #again step counter will be increment after each line of code ran
    basic_step_counter = 0
    new_list = []
    while (len(working_list) > 0):
        basic_step_counter+=1
        new_value = 0
        basic_step_counter+=1
        new_value = min(working_list)
        basic_step_counter+=1
        new_list.append(new_value)
        basic_step_counter+=1
        working_list.remove(new_value)
        basic_step_counter+=1
    
    print ("step counter incremented " + str(basic_step_counter) + " times.")
    return (new_list)   
        


small_list = [67,45,2,13,1,998]
big_list = [89,23,33,45,10,12,45,45,45]



print("Here are the results for sort_this_list( list ):")

print ("before: " + str(small_list))
time.sleep(0.5)
small_list = sort_this_list(small_list)
print ("after: " + str(small_list))
time.sleep(0.5)
print ("\n")
time.sleep(0.5)
print ("before: " + str(big_list))
time.sleep(0.5)
big_list = sort_this_list(big_list)
print ("after: " + str(big_list))
time.sleep(0.5)
print ("\n")
time.sleep(0.5)

print("Resetting variables\n")
time.sleep(0.5)
small_list = [67,45,2,13,1,998]
big_list = [89,23,33,45,10,12,45,45,45]
print("unsorted variables:\n\tsmall_list: "+str(small_list)+"\n\tbig_list: "+str(big_list))
time.sleep(0.5)

waitin = input("\nPress Enter to Continue\n")

print("")
time.sleep(0.5)
print("Now for better_sorter( list ) results:")
time.sleep(0.5)
print ("before: " + str(small_list))
time.sleep(0.5)
small_list = better_sorter(small_list)
print ("after: " + str(small_list))
time.sleep(0.5)
print ("\n")
time.sleep(0.5)
print ("before: " + str(big_list))
time.sleep(0.5)
big_list = better_sorter(big_list)
print ("after: " + str(big_list))
time.sleep(0.5)

print ("")
time.sleep(0.5)

finished_program = input("\nPress enter to exit\n")
