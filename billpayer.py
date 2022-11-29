import random
names=input("ENTER EVERYBODY'S NAME SEPERATED BY A COMMA \n")
split_name=names.split(",")
num_of_names=(len(split_name))
a=random.randint(1,num_of_names-1)
bill_payer=(split_name[a])
print("{} has to pay the bill 😄".format(bill_payer))