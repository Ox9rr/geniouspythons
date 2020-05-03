result = open("result.txt","w")
f = open('test.txt', 'r')
x = f.readlines()
xtestSplit = str(x).split(',')
y=len(xtestSplit)
print(xtestSplit[35])
# x = f.readlines()
# print(len(x))

# sosi 4len
# def pars (count):
#     f = open('test.txt','r')
#     xtest = f.readlines()

#     xtestSplit = str(xtest).split(',')
#     lol = str(xtestSplit[count]).split('>')
    
#     lolSplit = str(lol[1]).split('<')
#     print(lolSplit[0])
#     result.write((lolSplit[0] + '\n'))


# for n in range(0,7):

#     pars(n)