todo_dict={
    'one':1
}

while True:
    val=input("what you want to do : 1.add to do 2.view to do 3.delete to do")
    if val == '1':
        count=int(input("how many to dos"))
        for i in range(count):
            todo=input(f"Enter to do {i +1} : ")
            todo_dict.update({i:todo})

    if val == '2':
        if len(todo_dict) == 0:
            print("no to dos ! ")
        else:
            for i in todo_dict:
                print(todo_dict[i])



