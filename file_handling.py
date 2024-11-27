file=open("example.txt","w")
filename="example.txt"
#fileContent=file.readlines()
file=open(filename,"a")
datastring="Some dummy text data \n newline \t after tab".split()
#print(fileContent)
print(datastring)
#file.write("Hello, this is a test .")
fileContent=file.writelines(datastring)
file.close()  


