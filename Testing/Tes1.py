class Interview():
    def swap(a,b):
        c=a
        a=b
        b=c
        print(a,b)
    def find(searchElement,mainString):
        if searchElement in mainString:
            print("foud")
        else:
            print("Not found")

Obj1=Interview
Obj1.swap(12,33)
Obj1.find("doodle","Hello World")

