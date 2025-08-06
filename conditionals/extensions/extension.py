def main():
    x = input("name: ").strip().casefold()
    extension(x)

def extension(n):
    if n[-4:] == ".ipg" or n[-5:] == ".ipeg":
        print("image/ipeg")
    elif n[-4:] == ".gif":
        print("image/gif")
    elif n[-4:] == ".png":
        print("image/png")
    elif n[-4:] == ".pdf":
        print("applications/pdf")
    elif n[-4:] == ".zip":
        print("applications/zip")
    elif n[-4:] == ".txt":
        print("text/plain")
    else:
        print("application/octet-stream")

main()



#def main():
    #name = input("File name: ").strip().lower()

    #if name.endswith(".gif"):
        #print("image/gif")
    #elif name.endswith(".jpg") or name.endswith(".jpeg"):
        #print("image/jpeg")
    #elif name.endswith(".png"):
        #print("image/png")
    #elif name.endswith(".pdf"):
        #print("application/pdf")
    #elif name.endswith(".txt"):
        #print("text/plain")
    #elif name.endswith(".zip"):
        #print("application/zip")
    #else:
        #print("application/octet-stream")

#main()



#def main():
    #name = input("name: ").strip().lower()
    #print(get_media_type(name))

#def get_media_type(filename):
    #if filename.endswith(".gif"):
        #return "image/gif"
    #elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        #return "image/jpeg"
    #elif filename.endswith(".png"):
        #return "image/png"
    #elif filename.endswith(".pdf"):
        #return "application/pdf"
    #elif filename.endswith(".txt"):
        #return "text/plain"
    #elif filename.endswith(".zip"):
        #return "application/zip"
    #else:
        #return "application/octet-stream"

#main()
