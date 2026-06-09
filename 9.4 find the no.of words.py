file_path="example.txt"
#open the file in read mode
with open(file_path,"r")as file:
    #read the entire content of the file
    content=file.read()
    #split the content into words
    words=content.split()
    #count the number of (words)
    word_count=len(words)
print("total words in",file_path,":",word_count)
