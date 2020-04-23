def reststrs(inputstring):
    allzips = inputstring.split("@")[0].split(",")
    usedzips = inputstring.split("@")[1].split(",")

    allalpha, usedalpha = [], []
    allnum, usednum = [], []
    rest = ""
    for all in allzips:
        allalpha.append(all.split(":")[0])
        allnum.append(int(all.split(":")[1]))

    try:
        for used in usedzips:
            usedalpha.append(used.split(":")[0])
            usednum.append(int(used.split(":")[1]))
    except:
        pass

    for i in range(len(allalpha)):
        restalpha = allalpha[i]
        if allalpha[i]  not in usedalpha:
            restnum = allnum[i]
        else:
            restnum = allnum[i] - usednum[usedalpha.index(allalpha[i])]
        if restnum > 0:
            if rest == "":
                rest= restalpha + ":" + str(restnum)
            else:
                rest = rest + "\n" + restalpha + ":" + str(restnum)
        # elif restnum < 0:
        #     return print(restalpha + "字符已占用超标！")
    return rest

if __name__ == "__main__":
    strs = "A:3,a:4,b:5,c:2@a:1,b:4"
    print(reststrs(strs))
