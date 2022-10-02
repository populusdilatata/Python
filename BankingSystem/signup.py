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



def validate(username, password):
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

user_accounts={'Brandon': 'brandon123ABC', 'Jack': 'jack123POU', 'James': '100jamesABD', 'Sarah': 'sd896ssfJJH'}
log_in = {'Brandon': 'False', 'Jack': 'False', 'James': 'False', 'Sarah': 'False'}
print(signup(user_accounts, log_in, "Brandon", "123abcABCD"))
#will return False
print(signup(user_accounts, log_in, "BrandonK", "123ABCD"))
# will return False
print(signup(user_accounts, log_in, "BrandonK","abcdABCD"))
# will return False
print(signup(user_accounts, log_in, "BrandonK", "123aABCD"))
# will return True. Then calling
print(user_accounts)
print(log_in)
print(signup(user_accounts, log_in, "BrandonK", "123aABCD"))
# again will return False
