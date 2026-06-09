file_path="output.txt"
with open(file_path,"w")as file:
    #write content to the file
    file.write("hello,world!\n")
    file.write("this is a sample text")
print("content writen to",file_path)
