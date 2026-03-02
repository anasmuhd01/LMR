# fp= open("File_handling/files.txt")
# print(fp.read())

# fp=open("File_handling/file1.txt","w")
# fp.write("file 1 is writted")


# print(fp.readline()) #- readline() --> will read file line by line


# print(fp.readlines()) # will return as list of file items

#when multiple unknown data to be added to file 
# fp=open("FIle_handling/file2.txt","w")
# data=['line1','line2','line3','']

# for i in data:
#     fp.write(i+"\n")

#append
# fp=open("FIle_handling/file2.txt","a")
# fp.write("append testing line ")

#x mode
# open("File_handling/XmodeFile.txt","x")

fp=open("File_handling/file3.txt","r+")
print(fp.read())
# fp.seek(0) # will start the index at zero
fp.write("line 2")