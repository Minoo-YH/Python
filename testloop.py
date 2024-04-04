listingThing = []

def functionExample() :
        while True:
                listingThing.append(input("input:"))
                if len(listingThing) >=5:
                        for i in listingThing:
                                print(i)
                                print("/n" ,"Exiting") , exit()

  functionExample ()                              