phonebook={}
x=5


while True:
    operation=int(input("\npress number for operatio \n1.CREATE: \n2.RETRIEVE: \n3.UPDATE: "))
    if operation==1:
        name=input("enter name: ")
        phone=input("enter phone: ")
        phonebook.update({name:{"name":name,"phone":phone}})
        

    elif operation==2:
        for i in phonebook:
            print(f"\n{phonebook[i]}")
        

    elif operation==3:
        for i in phonebook:
            print(f"names:{phonebook[i]}")
        name=input("\nenter name to update:")
        for i in phonebook:
            if name==
                phonebook.update({"name":{"phone":name}})

    elif operation==4:
        for i in phonebook:
            

    else:
        print("invalid operation")



print(phonebook)  