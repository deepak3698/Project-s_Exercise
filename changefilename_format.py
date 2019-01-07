import os
def soldier(path,filename,mode):
    f1 = open(filename)
    list1 = f1.read().split('\n')
    f1.close()
    os.chdir(path)
    files = os.listdir(path)
    i = 1
    for file in files:
        if file not in list1 and file.endswith(f'.{mode}'):
            os.rename(f"{file}", f"{i}.{mode}")
            i += 1
        else:
            if file not in list1:
                os.rename(file, file.capitalize())

if __name__ == '__main__':
    try:
        print("##The filename which you will write should be in your current directory..\n\n")
        print("##The filename(with extension) which you will write should be in your current directory..\n\n")
        path=input("Enter full path where you want to do changes ")
        filename=input("Enter file name ")
        mode=input("Plz define mode..for special changes ")
        soldier(path, filename, mode)
        print("!!!!!Work Done!!!!")
    except:
        print("Somethong Went Wrong!!!")

