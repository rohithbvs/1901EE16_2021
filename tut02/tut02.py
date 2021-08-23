#MY name is BVS Rohith Roll no 1901ee16
def get_memory_score(input):
    invalid_list = []#This list stores all invalid inputs
    flag=False#if there is invalid input this flag is set to true
    for i in input:
        if type(i) is not int:
            flag=True
            invalid_list.append(i)
    
    if(flag):
        print("Please enter a valid input list. Invalid inputs detected:{}".format(invalid_list))
    else:
        score=0#score counts the number our required ans
        memory_list = []#this is the memory list which stores the values remembered
        for i in input:
            if len(memory_list)<5:
                if i in memory_list:
                    score = score +1
                else:
                    memory_list.append(i)
            else:
                if i in memory_list:
                    score = score +1
                else:
                    memory_list.pop(0)
                    memory_list.append(i)

        print("Score:{}".format(score))
                



    return

input_nums = [7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]
get_memory_score(input_nums)