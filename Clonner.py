import os
import sys
def download(URLName):
    print("Installing")
    pre = "wget.exe"
    mid = " -r "
    link = URLName
    Url = pre+mid+link
    os.system(Url)
def help():
    print("Usage:Clonner <Clone> or <C> <Website URL> to clone a website")
    sys.exit(1)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:Clonner <Clone> <Website URL>")
        sys.exit(1)
    else:
        function_name = sys.argv[1]
        if function_name == "Clone" or function_name == "C":
            URLName = sys.argv[2]
            download(URLName)
        elif function_name == "help":
            help()
        else:
            print("Invalid Operation")
            print("Usage:Clonner <Clone> <Website URL>")
            sys.exit(1)


    