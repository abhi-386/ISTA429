'''This  is programthat uses the method split.
    This will help us to identify if two date are similar or older
'''
def gt_dates (date1 , date2):
    if date1 == date2 :
        print ("Both dates are same")
        return 
    list1 = date1.split("/")
    list2 = date2.split("/")
    if list1[2] > list2[2]:
        return True
    else:
        if list1[0] > list2[0]:
            return True
        else:
            if list1[1] > list2[1]:
                return True
            else:
                return False
def main():
    # This is the main method which is called first
    #Takes the two input for the date:
    #Here we assume the input date are in correct format
    str1 = input("Enter date1 in format MM/DD/YYYY: ")
    str2 = input("Enter date1 in format MM/DD/YYYY: ")
    if (gt_dates (str1,str2) == 'null' ):
        pass
    elif (gt_dates (str1,str2)):
        print(str2 + " is before " + str1)
    else:
        print(str1 + " is before " + str2)
main()
