# Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail 
# messages. The program looks for 'From ' lines and takes 
# the second word of those lines as the person 
# who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to 
# a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads 
# through the dictionary using a maximum loop to find 
# the most prolific committer.
############################################################
#name = input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)
di=dict()
############################################################
############################################################
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
        line = line[1]
        #print(line)
        di[line]=di.get(line,0)+1
    count += 1
############################################################
############################################################


#print(di)

largest=-1
theword=None
for k,v in di.items():
    #print("First print", k,v)
    if v > largest:
        largest=v
        theword=k
        
print(theword, largest)
#print("There were",count,"lines in the file with From as the first word")
