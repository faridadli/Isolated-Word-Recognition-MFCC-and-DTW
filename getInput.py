import shutil
import os

#Get current working directory
FOLDER = r"\assets"
CWD = os.getcwd() 
PATH = CWD+FOLDER  
# Destination path
#"/Users/Farid Adli/OneDrive/Documents/Algo Design and Analysis/Algo Project/Speech-Recognition-Using-Dynamic-Time-Warping-master/assets"

def fileInput(source, destination):
    
    # Copy the content of
    # source to destination
    try:
        shutil.copy(source, destination)
        print("File copied succesfully")
        ans = input("Do you want to add more file? 1 for Yes, 0 for No: ")
        if(int(ans) == 1):
            return fileInput(srcPath(), PATH)
        else:
            return fileList(PATH)
        
    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")
        return userInput()

    # If destination is a directory.
    except IsADirectoryError:
        print("Destination is a directory.")
        return userInput()

    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")
        return userInput()

    # For other errors
    except:
        print("Error occurred while copying file.")
        return userInput()

#display list of wav file in asset and choose file to analyse
def fileList(path):
    files = os.listdir(path)

    for i in range (len(files)):
        print(i,":",files[i])

    template = input("Choose template file: ")
    target = input("Choose target file: ")
    tplate, targ = files[int(template)], files[int(target)]
    print("Template file choosen: ",tplate)
    print("Target file choosen: ",targ)
    return tplate, targ

def srcPath():
    source = input("Enter the full path of your file in wav format: ")
    # example source = "/Users/Farid Adli/Downloads/doors-and-corners-kid_thats-where-they-get-you-2.wav"
    return source

def userInput():   
    # Source path
    opt = input("0: Add new wav file\n1: Choose from existing file\n")
    if(int(opt)==0): 

        return fileInput(srcPath(), PATH)
    else:
        return fileList(PATH)