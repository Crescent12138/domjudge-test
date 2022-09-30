import sys
try:
    number = int(sys.argv[1])
except Exception as e:
    print(e,"请输入参数为数字")
    exit(0)
f = open("teams.tsv","w")
n = 0
# ss = str(n) + "\tteam" + "\tteam"
# ss = ss[::-1].zfill(2)[::-1]
# print(ss)
f.write("teams\t1\n")
while n < number:
    n += 1
    ss = str(n)
    ss = ss.zfill(3)
    ss = str(n) +"\tteam"+ss + "\t3\tteam" + ss + "\tGXU\tGXU\tCHN\tGXU"+"\n"
    f.write(ss)
