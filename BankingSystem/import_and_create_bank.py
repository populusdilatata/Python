def import_and_create_bank(filename):
    '''
    This function is used to create a bank dictionary.  The given argument is the filename to load.
    Every line in the file should be in the following format:
        key: value
    The key is a user's name and the value is an amount to update the user's bank account with.  The value should be a
    number, however, it is possible that there is no value or that the value is an invalid number.

    What you will do:
    - Create an empty bank dictionary.
    - Read in the file.
    - Add keys and values to the dictionary from the contents of the file.
    - If the key doesn't exist in the dictionary, create a new key:value pair.
    - If the key does exist in the dictionary, increment its value with the amount.
    - You should also handle the following cases:
    -- When the value is missing or invalid.  If so, ignore that line and don't update the dictionary.
    -- When the line is completely blank.  Again, ignore that line and don't update the dictionary.
    -- When there is whitespace at the beginning or end of a line and/or between the name and value on a line.  You
    should trim any and all whitespace.
    - Return the bank dictionary from this function.

    For example, here's how your code should handle some specific lines in the file:
    The 1st line in the file has a name and valid number:
        Brandon: 5
    Your code will process this line and add the extracted information to the dictionary.  After it does,
    the dictionary will look like this:
        bank = {"Brandon": 5}

    The 2nd line in the file also has a name and valid number:
        Patrick: 18.9
    Your code will also process this line and add the extracted information to the dictionary.  After it does,
    the dictionary will look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 3rd line in the file has a name but invalid number:
        Brandon: xyz
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 4th line in the file has a name but missing number:
        Jack:
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 5th line in the file is completely blank.
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 8th line in the file has a name and valid number, but with extra whitespace:
        Brandon:       10
    Your code will process this line and update the value associated with the existing key ('Brandon') in the dictionary.
    After it does, the value associated with the key 'Brandon' will be 10:
        bank = {"Brandon": 15, ...}

    After processing every line in the file, the dictionary will look like this:
        bank = {"Brandon": 115.5, "Patrick": 18.9, "Sarah": 827.43, "Jack": 45.0, "James": 128.87}
    Return the dictionary from this function.
    '''

    bank = {}

    # your code here
    #i = 1

    with open(filename, "r") as file:

        for line in file:
            #print(i)
            name = line.rstrip('\n').split(":")
            #(name, amt) = line.rstrip('\n').split(":")
            zapis = True

            if (len(name)) ==2:
                name2=name[0].strip()

                amt1=name[1].strip()
                # using isdigit() + replace()
                # Check for float string
                res = amt1.replace('.', '', 1).isdigit()

                # print result
                if res :
                    #print("Is string a possible float number ? : " + str(res))
                    amt2=amt1
                else:
                    amt2=0
                    zapis = False
                #print(type(amt1))
            else:
                name2=name[0].strip()
                zapis = False
            #print(name2)
            #print(amt2)
            key=name2
            value=float(amt2)
            #print(amt)
            if zapis:
                bank[key] = bank.get(key, 0) + value

            #i += 1

    return bank

    ##########################
### TEST YOUR SOLUTION ###
##########################
#print("BlaBla")
bank = import_and_create_bank("bank.txt")

print(bank)
