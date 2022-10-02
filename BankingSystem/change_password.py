def change_password(user_accounts, log_in, username, old_password, new_password):
    '''
    This function allows users to change their password.

    If all of the following requirements are met, changes the password and returns True. Otherwise, returns False.
    - The username exists in the user_accounts.
    - The user is logged in (the username is associated with the value True in the log_in dictionary)
    - The old_password is the user's current password.
    - The new_password should be different from the old one.
    - The new_password fulfills the requirement in signup.

    For example:
    - Calling change_password(user_accounts, log_in, "BrandonK", "123abcABC" ,"123abcABCD") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "123abcABCD", "123abcABCDE") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "brandon123ABC", "brandon123ABC") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "brandon123ABC", c"123abcABCD") will return True

    Hint: Think about defining and using a separate valid(password) function that checks the validity of a given password.
    This will also come in handy when writing the signup() function.
    '''

    # your code here
    print("="*50)
    print("Vstup do metody change_password")
    #print(user_accounts)
    #print(username)
    if (old_password == new_password):
        return False
    else:
        for keys in user_accounts.keys():
            print(keys)
            print("Timto jmenem se prihlasujes ", username)
            if (keys == username):
                print("Toto ulozene heslo", user_accounts[keys])
                print("Toto napsane heslo", old_password)
                if (user_accounts[keys] != old_password):
                    return False
                else:
                    print("Vypisuju log_in", log_in[keys])
                    #print(((validate(username, new_password)) and log_in[keys]))
                    if (validate(username, new_password)) and log_in[keys]=='True':
                        print("2")
                        return True

                    else:
                        print("3")
                        return False

    return False

def login(user_accounts, log_in, username, password):
    '''
    This function allows users to log in with their username and password.
    The user_accounts dictionary stores the username and associated password.
    The log_in dictionary stores the username and associated log-in status.

    If the username does not exist in user_accounts or the password is incorrect:
    - Returns False.
    Otherwise:
    - Updates the user's log-in status in the log_in dictionary, setting the value to True.
    - Returns True.

    For example:
    - Calling login(user_accounts, "Brandon", "123abcAB") will return False
    - Calling login(user_accounts, "Brandon", "brandon123ABC") will return True
    '''

    # your code here
    #print("Toto: " ,user_accounts)
    #print("Vstup do metody login")
    for keys in user_accounts:
        if (keys == username):
            #print("Jsem nasel jmeno")
            #print(user_accounts[keys])
            #print(password)
            if (user_accounts[keys] == password):
                #print("Jsem nasel jmeno a heslo")
                log_in[keys]='True'
                return True
            else:
                #print("Jsem nasel jmeno bez hesla")
                return False
        else:
            return False

    #print("Tamto: ", log_in)

    return True

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
    #print("Vstup do metody import_and_create_bank")
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
def validate(username, password):
    #print("Vstup do metody validate")
    l, u, d = 0, 0, 0
    if (len(password) < 7 ):
        result = False
    for i in password:
        # counting lowercase alphabets
        if (i.islower()):
            l+=1
        # counting uppercase alphabets
        if (i.isupper()):
            u+=1
            # counting digits
        if (i.isdigit()):
                d+=1
    if (l>=1 and u>=1 and d>=1 and l+u+d==len(password)) and (username != password):
        result = True
    else:
        result = False

    return result

def import_and_create_accounts(filename):
    user_accounts = {}
    log_in={}
    value=0

    # your code here
    #print("Vstup do metody import_and_create_accounts")
    with open(filename, "r") as file:

        for line in file:
            #print(i)
            name = line.rstrip('\n').split("-")
            #(name, amt) = line.rstrip('\n').split(":")
            zapis = True

            if (len(name)) ==2:
                name2=name[0].strip()

                for keys in user_accounts:
                    if (keys == name2):
                        #print("Jsem nasel stejne jmeno")
                        zapis = False



                password=name[1].strip()
                #print("name2: "+name2)
                #print("password: "+password)
                # Validation of password
                res=validate(name2,password)
                if res:
                    #print(password)
                    value=password
                else:
                    zapis = False
                #print(type(amt1))
            else:
                name2=name[0].strip()
                zapis = False
            #print(name2)
            #print(amt2)
            key=name2
            #print(value)
            if zapis:
                user_accounts.update({key : value} )
                log_in.update({key : "False"})

            #i += 1
    #print(user_accounts)
    return user_accounts, log_in
##########################
### TEST YOUR SOLUTION ###
##########################
bank = import_and_create_bank("bank.txt")
user_accounts, log_in = import_and_create_accounts("user.txt")
print(log_in)
#tools.assert_false(change_password(user_accounts,log_in,"BrandonK","123abcABC","123abcABCD"))
print("Prvni", change_password(user_accounts,log_in,"BrandonK","123abcABC","123abcABCD"))
#tools.assert_false(change_password(user_accounts,log_in,"Brandon","brandon123ABC","123abcABCD"))
print("Neni prihlaseny")
print("Druhe", change_password(user_accounts,log_in,"Brandon","brandon123ABC","123abcABCD"))

login(user_accounts,log_in,"Brandon","brandon123ABC")
print(log_in)
#tools.assert_false(change_password(user_accounts,log_in,"Brandon","123abcABCD","123abcABCDE"))
print("Treti",change_password(user_accounts,log_in,"Brandon","123abcABCD","123abcABCDE"))

#tools.assert_false(change_password(user_accounts,log_in,"Brandon","brandon123ABC","brandon123ABC"))
print("Ctvrte", change_password(user_accounts,log_in,"Brandon","brandon123ABC","brandon123ABC"))
#tools.assert_false(change_password(user_accounts,log_in,"Brandon","brandon123ABC","123ABCD"))
print("Pate", change_password(user_accounts,log_in,"Brandon","brandon123ABC","123ABCD"))

#tools.assert_true(change_password(user_accounts,log_in,"Brandon","brandon123ABC","123abcABCD"))
print("Je prihlaseny")
print("Seste",change_password(user_accounts,log_in,"Brandon","brandon123ABC","123abcABCD"))
#tools.assert_equal("123abcABCD",user_accounts["Brandon"])
print("Success!")
