#My name is BVS Rohith , My Roll no is 1901EE16


def meraki_helper(x):
    flag=True  #flag is set to false if we find any adjacent digits difference is not equal to 1
    temp=x #as x keep changing temp is used to print final statement
    prev=x%10 #prev and cur variables are used to find diff of adjacent digits
    x=int(x/10)
    while(x>0):
        cur=x%10
        x=int(x/10)
        if(cur-prev!=1 and prev-cur!=1):
            flag=False
            break
        prev=cur
        
    if(flag):
        print("Yes - {} is a Meraki number".format(temp))
        return 1
    else:
        print("NO - {} is not a Meraki number".format(temp))
        return 0




lst = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]

#meraki variable is used for counting number of meraki numbers in given list
meraki=0
#not_meraki variable is used for counting number of not meraki numbers in given list
not_meraki=0

for x in lst:
    if(meraki_helper(x)==0):
        not_meraki+=1
    else:
        meraki+=1

print("the input list contains {} meraki and {} non meraki numbers.".format(meraki,not_meraki))
