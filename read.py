class read:
    def __init__(self, name, extra):
        self.name = name
        self.extra = extra 
    def readFile(self):
        x=[]
        y = []
        f= open(self.name,'r')
        content = f.read()
        # change . with any symbols or letter you want
        x = content.split(".")
        if self.extra == 'y': 
            for t in x:
                # replace 1 and 2 with anythong that need to goes before and after text
                y.append("1 " + t + " 2")
        return y if y else x

        # add file name be careful with the directory
        # n if you dont want to add 
read1 = read("text.txt",'y')
print(read1.readFile())