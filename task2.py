from functools import reduce

orders=[
    
        {"product":"Laptop","price":50000},
        {"product":"Mouse","price":500},
        {"product":"Keybord","price":1500},
        {"product":"Monitor","price":12000},
    
]

# total=reduce(lambda var1,var2: var1+var2["price"],orders,0)
# print("total revenue : ",total)

# expe=reduce(lambda a,b:a if a["price"]>b["price"] else b,orders)
# print("expensive product : ",expe["product"])


attendance={"Rahul":"09:10",
            "Anu":"08:55",
            "Vishnu":"09:30",
            "Meera":"08:45",
            }



att=filter(lambda a:attendance[a]<"09:00",attendance)
print(list(att))



    

