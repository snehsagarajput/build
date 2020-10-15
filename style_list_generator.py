import os

def generator():
    # Getting the current work directory (cwd)
    thisdir = os.path.dirname(os.path.realpath(__file__))+"/Content Images"


    images = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            images.append(file)
            #print(file)
    images.sort()
    #print("\n\nTotal Images : "+str(len(images))+"\n\n")
    
    def itemName(item):
        name=""
        for i in item:
            if i==".":
                break
            name+=i
        return name

    f = open("style_image_list.txt", "w")

    for item in images:
        f.write(itemName(item))
        f.write("\n")

    f.close()
