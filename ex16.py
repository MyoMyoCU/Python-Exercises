from sys import argv

script , filename = argv 

print (f"We're going to erase {filename}.")
print ("If you don't want that , hit CTRL-C(^C)>")
print ("It you do want that , Hit RETURN ")

input("?")


print ("Opening the files .....")
target = open(filename,'w')
print("Truncating the file, Goodbye! ")
target .truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1 : ")
line2 = input("line2 : ")
line3 = input("line3 : ")

print("I'm going to write thest to the files.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it .")
target.close()

