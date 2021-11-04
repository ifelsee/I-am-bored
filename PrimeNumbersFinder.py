result = []
for i in range(2,11): 
    flag = False
    oi = i 
    if i < 0 : i = -(i)
    if i != 0 :
            for j in range(2,(int(i)//2)+1):

                    if (i % j) == 0:
                            flag = True
                            break
            if flag == False:
                    if oi < 0: result.append(oi)
                    else: result.append(i)


with open('primeNumbers.cv', 'a') as f:
    f.write(",".join([str(i) for i in result]))
