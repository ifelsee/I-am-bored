import os
def rmn(file_name):
    with open(file_name) as file:
        lines = [line.rstrip() for line in file.readlines()]
        x = ""
        c = 0
        temp = []
        for i in lines:
            c += 1
            if c == 1 :
                x = i
            else :
                if c == 3 :
                    i = i.replace (x,"",1)
                temp.append(i)
            if c == 4 :
                c = 0
        [print(i) for i in temp]
        os.remove(file_name)
        f = open(file_name, "a")
        c = 0
        for i in temp:
            c +=1
            if c == 3:
                c = 0
                f.writelines("\n")
                f.writelines("\n")
                f.writelines(i)
            else :


                f.writelines("\n")
                f.writelines(i)

[rmn(i) for i in os.listdir() if i[-3:] == "srt"]

