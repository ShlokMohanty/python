#interacting with files 
#its pretty common to need to read 
xmen_file = open('xmen_base.txt', 'r')
xmen_file 
xmen_file.read()
xmen_file.seek(0)
xmen_file.read()
for line in xmen_file :
  print(line, end="")
  
#storm 
#wolverine
#Cyclops
#Bishop 
#Nightcrawler 

xmen_file.close()
xmen_base = open('xmen_base.txt')
new_xmen = open('new_xmen.txt','w')
new_xmen.write(xmen_base.read())
new_xmen.close()
new_xmen = open(new_xmen.name, 'r+')
new_xmen.read()
#read from the base file and used the return value as teh argument to write for our new file .
#we closed the new file 
#we reopened the new file, using the r+ mode which will allow us to read and write content to the file.
#we read the content from the new file to ensure that it wrote properly 
#Now taht we have a file that we can read and write from lets add some more names :
new_xmen.seek(0)
new_xmen.write("Beast\n")
new_xmen.write("Phoenix\n")
new_xmen.seek(0)
new_xmen.read()

#Appending to the file 
xmen_file.close()
with open('xmen_base.txt', 'a') as f:
  f.write('Professor Xavier\n')
f = open('xmen_base.txt', 'a')
with f:
  f.write('Something\n')
exit()

#Functions are a great way to organize your code for reuse and clarity .script does the following:

