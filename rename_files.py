import os
#from str import maketrans   # Required to call maketrans function.

def rename_files():
    # comment 1: get file names from a folder
    file_list = os.listdir(r"C:\Users\jalpa\Desktop\secret message - python\prank")  # r = raw path
    #print (file_list)
    
    saved_path = os.getcwd()
    print("Current Working Diresctory is " + saved_path)
    os.chdir(r"C:\Users\jalpa\Desktop\secret message - python\prank")
    
    # comment 2: for each file, rename filename
    for file_name in file_list:
        print ("Old Name - " +file_name)
        a = file_name.maketrans(" "," ", "0123456789")
        print ("New Name - "+file_name)
        os.rename(file_name, file_name.translate(a))
        
rename_files()
