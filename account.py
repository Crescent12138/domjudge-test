import random
import sys
number = 0
try :
    number = int(sys.argv[1])
except Exception as e:
    print(e,"请输入参数为数字")

    exit(0)

ls = []

for i in range(1,10):
    ls.append(chr(48+i))
for i in range(0,26):
    if i == 14:
        continue
    if i == 6:
        continue
    ls.append(chr(97+i))
    ls.append(chr(65+i))
# print(ls)
f = open("account.tsv","w")
f.write("accounts\t1\n")
n = 0
password = []
while n < number:
    n += 1
    rm = []
    # print(random.sample(ls,8))
    rm = rm + random.sample(ls,8)
    re = [str(i) for i in rm]
    pw = "".join(re)
    # print(pw)
    lse = ("team\t" + "team" + str(n).zfill(3) + "\t" + "team" + str(n).zfill(3) + "\t" + pw+"\n" )
    # print(ls)
    f.write(lse)