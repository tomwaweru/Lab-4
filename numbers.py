import math

def numbers():
    myfile = open("numbers.txt", "w")
    myfile.write("Numbers Squared Sq. Root\n")
    myfile.write("------- ------- --------\n")
    
    for i in range(1,101):
        myfile.write('%6d %7d %7.3f' % (i, i*i, math.sqrt(i)))
        
    myfile.close()
    print("Finished writing the File")

numbers()

def read_numbers():
    infile = open("numbers.txt", "r")
    #allstr = infile.read()
    #print(allstr)
    #allstr = infile.read()
   # print(allstr)

    for i in range(10):
        s=infile.readline()
        print(s[:-1])
        
    infile.close()

read_numbers()


def read_numbers2():
    infile = open("numbers.txt", "r")
    ##lines = infile.readlines()

    #for s in lines:
    for s in infile:
         print(s[:-1])
         

    infile.close()

read_numbers2()
