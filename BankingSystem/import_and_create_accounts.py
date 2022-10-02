def import_and_create_accounts(filename):
    user_accounts = {}
    log_in={}
    value=0

    # your code here
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
                        print("Jsem nasel stejne jmeno")
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
            print(value)
            if zapis:
                user_accounts.update({key : value} )
                log_in.update({key : "False"})

            #i += 1
    print(user_accounts)
    return user_accounts, log_in


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


print(validate("Brandon","brandon123ABC"))
print(validate("Jack","jac123"))
print(validate("Jack","jack123POU"))
print(validate("Patrick","patrick5678"))
print(validate("Brandon","brandon123ABCD"))
print(validate("James","100jamesABD"))
print(validate("Sarah","sd896ssfJJH"))
print(validate("Jennie","sadsaca"))

user_accounts, log_in= import_and_create_accounts("user_accounts.txt")
print(user_accounts)
print(log_in["Sarah"])
