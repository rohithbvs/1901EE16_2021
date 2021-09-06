import os        
 
def output_individual_roll():
    DIR = "output_individual_roll"

    '''roll_dict is a dictnary with key=roll number and it has list of list in it'''
    roll_dict = {}

    '''we are opening the given file and taking input as dict with key as roll no'''
    with open("regtable_old.csv", "r") as f:
        i=0
        for row in f:
            if i==0:
                i+=1#as first row is not related to student information we are not taking it
            else:
                row = row.strip().split(",")#here row is a list of words which are splited by ","
                rollno = row[0]
                register_sem = row[1]
                subno = row[3]
                sub_type = row[-1]
                if rollno not in roll_dict:
                    roll_dict[rollno] = []
                roll_dict[rollno].append([rollno, register_sem, subno, sub_type])

    '''This code is useful if the dir is not present then it will make the dir'''
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    
    '''The below code is responsible for creating and writing in the file'''
    for rollno in roll_dict:
        data = roll_dict[rollno]
        file = os.path.join(DIR, rollno + ".csv")
        with open(file, "w") as f:
            f.write("rollno,register_sem,subno,sub_type")
            for row in data:
                temp=""
                for x in row:
                    temp+=x
                    temp+=","
                
                temp=temp[:-1]
                f.write("\n"+temp)
 
 
def output_by_subject():
    DIR = "output_by_subject"

    '''subject_dict is a dictnary with key=subject number and it has list of list in it'''
    subject_dict = {}

    '''we are opening the given file and taking input as dict with key as subject no'''
    with open("regtable_old.csv", "r") as f:
        i=0
        for row in f:
            if i==0:
                i+=1#as first row is not related to student information we are not taking it
            else:    
                row = row.strip().split(",")#here row is a list of words which are splited by ","
                rollno = row[0]
                register_sem = row[1]
                subno = row[3]
                sub_type = row[-1]
                if subno not in subject_dict:
                    subject_dict[subno] = []
                subject_dict[subno].append([rollno, register_sem, subno, sub_type])
    
    '''This code is useful if the dir is not present then it will make the dir'''
    if not os.path.exists(DIR):
        os.makedirs(DIR)
 
    '''The below code is responsible for creating and writing in the file'''
    for subno in subject_dict:
        data = subject_dict[subno]
        file = os.path.join(DIR, subno + ".csv")
        with open(file, "w") as f:
            f.write("rollno,register_sem,subno,sub_type")
            for row in data:
                temp=""
                for x in row:
                    temp+=x
                    temp+=","
                
                temp=temp[:-1]
                f.write("\n"+temp)

output_by_subject()
output_individual_roll()

