from sys import argv
#print(argv)

if len(argv) < 2:
    print("Please provide a filename.")
    
else:
    file = open(argv[1])
    lines = file.read()
    print(type(lines))
    print(lines)