file_path="example.txt"
#open the files in read mode
with open(file_path,"r")as file:
 #read the entire content of the file
 content=file.read()
#print the content
 print(content)
