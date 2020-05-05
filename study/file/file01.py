s = ["聂伟星\n", "聂星星\n", "聂小星\n"]

with open("file.txt","w",encoding='UTF-8') as f:
    f.writelines(s)