phonebook={}

while True:
    operation=int(input("\npress number for operatio \n1.CREATE: \n2.RETRIEVE: \n3.UPDATE: \n4.DELETE \n5.EXIT\n"))
    if operation==1:
        name=input("enter name: ")
        phone=input("enter phone: ")
        phonebook.update({name:{"name":name,"phone":phone}})
        

    elif operation==2:
        if len(phonebook)==0:
            print("No elements to show")
        else:
            for i in phonebook:
                print(f"\n{phonebook[i]["name"]}:{phonebook[i]["phone"]}")
        

    elif operation==3:
        if len(phonebook)==0:
            print("No elements to update add item:3")
        else:
            print("\n names in directory:")
            for i in phonebook:
                print(f"names:{phonebook[i]["name"]}")

                name=input("\nenter name to update phone:")
            
                if name==phonebook[i]["name"]:
                    num=input("enter number: ")
                    phonebook[i]["phone"]=num
                else:
                    print("invalid name")


    elif operation==4:
        print("available names: ")
        for i in phonebook:
            print(f"\n{phonebook[i]["name"]}")
        name=input("enter name")
        if name in phonebook:
            phonebook.pop(name)
    elif operation==5:
        break
         
        



    else:
        print("invalid operation")



