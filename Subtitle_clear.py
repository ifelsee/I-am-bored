import os
import sys
def rmn(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        x = ""
        c = 0
        temp = []
        for i in lines:
            c += 1
            if c == 1 :
                x = i
                pass
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

#[rmn(i) for i in os.listdir() if i[-3:] == "srt"]

for i in os.listdir():
	if i != sys.argv[0]:
		os.chdir(i)
		for j in os.listdir():
			if j[-3:] =="srt":
				rmn(j)
			print(j)
		os.chdir("..")
