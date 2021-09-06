import os



#This function takes the data which is to be written and filename where it has to be written
def write_file(data, file):
    with open(file, "w") as f:
        f.write("rollno,register_sem,subno,sub_type")
        for row in data:
            temp=""
            for x in row:
                temp+=x
                temp+=","
            
            temp=temp[:-1]
            print(temp)
            f.write("\n"+temp)
            
 
 
def output_individual_roll():
    DIR = "output_individual_roll"
    roll_dict = {}
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
 
    if not os.path.exists(DIR):
        os.makedirs(DIR)
 
    for rollno in roll_dict:
        write_file(roll_dict[rollno], os.path.join(DIR, rollno + ".csv"))
 
 
def output_by_subject():
    DIR = "output_by_subject"
    subject_dict = {}
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
 
    if not os.path.exists(DIR):
        os.makedirs(DIR)
 
    for subno in subject_dict:
        write_file(subject_dict[subno], os.path.join(DIR, subno + ".csv"))
 
   
 
output_by_subject()
output_individual_roll()

