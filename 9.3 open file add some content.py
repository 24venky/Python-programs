file_path="output,txt"
#open the file in append mode
with open (file_path,"a")as file:
    #append content to the file
    file.write("\n this is an additional line:")
print("content append to",file_path)
