### TO PRINT ALL OF THECONTENTS :

'''
def main():

    infile = open('philosophers.txt','r')

    file_contents = infile.read()

    print(file_contents)

main()

'''

### TO PRINT ONE LINE AT A TIME :

def main():
    
    infile = open('philosophers.txt','r')

    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline()
    line3 = infile.readline().rstrip('\n')
    line4 = infile.readline()

    print(line1)
    print(line2.rstrip('\n'))
    print(line3)
    print(line4)

main()