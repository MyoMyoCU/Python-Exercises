#test

print ( "Enter file name ")
filename = input()

print(f"Your file is {filename}")
fileopen = open(filename)

print(fileopen.read())

