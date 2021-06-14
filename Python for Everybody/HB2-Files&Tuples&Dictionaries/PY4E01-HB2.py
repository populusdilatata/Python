# Write a program to read through the mbox-short.txt 
# and figure out the distribution by hour of the day 
# for each of the messages. You can pull the hour out 
# from the 'From ' line by finding the time and 
# then splitting the string a second time using a colon.
# 
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# 
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below.
#############################################################

#name = input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)
di=dict()
##############################################################
##############################################################
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        #wds = line.split()
       	#line = line[1]
        #print(line)
        ##########################
        ##########################
        line = line.split()
        #print(line)
        line = line[5]
        #print(line)
        line=line[:2]
        #print(line)
        di[line]=di.get(line,0)+1
    count += 1
#############################################################
#############################################################


#print("Toto je slovník", di)
newdic=dict()
tmpdic= ( sorted ([(k,v) for k,v in di.items()]))

for item in tmpdic:
    print(item[0], item[1])
    
