
def making_lists():
    thislist = ["apple","banana","orange","kiwi","mango","strawberry","melon","mango"]
    thislist2 = ["blueberry","raspberry","blackberry"]
    thislistberry = []
    print(thislist[2:4])
    print(thislist[-5:-1])
    if "cherry" in thislist:
        print("Yes, cherry is in this list")
    else:
        print("Added cherry to the list")
        thislist.append("cherry")
    thislist.extend(thislist2)
    thislist.pop(3)
    print(thislist)
    for x in thislist:
        if "berry" in x:
            thislistberry.append(x)
    thislistberry.sort()
    print(thislistberry)
    thislist.clear()
    print(thislist)


def main():
    making_lists()

main()