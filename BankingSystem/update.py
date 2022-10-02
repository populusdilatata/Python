def update(bank, log_in, username, amount):
    '''
    In this function, you will try to update the given user's bank account with the given amount.
    bank is a dictionary where the key is the username and the value is the user's account balance.
    log_in is a dictionary where the key is the username and the value is the user's log-in status.
    amount is the amount to update with, and can either be positive or negative.

    To update the user's account with the amount, the following requirements must be met:
    - The user exists in log_in and his/her status is True, meaning, the user is logged in.

    If the user doesn't exist in the bank, create the user.
    - The given amount can not result in a negative balance in the bank account.

    Return True if the user's account was updated.

    For example, if Brandon has 115.50 in his account:
    - Calling update(bank, log_in, "Brandon", 50) will return False, unless "Brandon" is first logged in.  Then it
    will return True.  Brandon will then have 165.50 in his account.
    - Calling update(bank, log_in, "Brandon", -200) will return False because Brandon does not have enough in his
    account.
    '''

    # your code here
    print("="*50)
    print("Vstup do metody update")
    print(bank)
    print(log_in)
    nalezen_odesilatel='False'
    for key in bank.keys():
        #print("Hledam odesilatele", keys)
        print("Timto jmenem se prihlasuje odesilatel ", username)
        if (key == username):
            nalezen_odesilatel= 'True'
            print("Penize",bank[key])
            #print(bank[key]+amount)
            if((bank[key]+amount) > 0):
                if(log_in[key]=='True'):
                    prihlasen_odesilatel='True'
                    print("Penize odesilatele",bank[key])
                    bank[key]+=amount
                    print("Penize odesilatele",bank[key])
                    return True

                            #print(bank)
                else:
                    print("Odesilatel neprihlasen")
                    return False
            else:
                print("Nedostatek penez")
                return False


    #if (nalezen_prijemce == 'False') or (nalezen_odesilatel =='False'):
    if (nalezen_odesilatel =='False'):
        bank.update({username : amount})
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

def signup(user_accounts, log_in, username, password):
    # your code here
    zapis = 0
    for keys in user_accounts.keys():
        print(keys)
        print("Timto jmenem se prihlasujes ", username)
        if (keys == username):
            print("Toto jmeno uz je ulozeno")
            zapis = 1

    if (validate(username, password) and zapis == 0):
        print("Probehne zapis")
        user_accounts.update({username : password} )
        log_in.update({username : "False"})
        return True
    else:
        print("Uz zapsane jmeno, nevalidni heslo")
        return False

bank = import_and_create_bank("bank.txt")
user_accounts, log_in = import_and_create_accounts("user.txt")

print("1False",update(bank,log_in,"Jack",100))
login(user_accounts, log_in, "Brandon", "brandon123ABC")
print("2False",update(bank,log_in,"Brandon",-400))
print("3True",update(bank,log_in,"Brandon",100))
#tools.assert_almost_equal(bank.get("Brandon"),215.5)

signup(user_accounts, log_in, "BrandonK", "123aABCD")
#tools.assert_is_none(bank.get("BrandonK"))
login(user_accounts,log_in,"BrandonK","123aABCD")
print(bank)
print("True", update(bank,log_in,"BrandonK",100))
print(bank)
#tools.assert_almost_equal(bank.get("BrandonK"),100)
print("Success!")
