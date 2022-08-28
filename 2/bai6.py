numList = input("Nhap vao 1 day so: ")
numList = numList.split()

# for i in range(len(numList)):
#     a = 0
#     loop = 1

#     for k in range(i, 0, -1):
#         a = 0
#         if numList[i] == numList[k]:
#             a = 1
            
#     if a == 1:
#         continue
   
#     for r in range(i+1, len(numList)):
#             if numList[i] == numList[r]:
#                 loop += 1

#     print(numList[i], ":", loop, "lan")

numDict = {}
for num in numList:
    if num in numDict:
        numDict[num] += 1
    else:
        numDict[num] = 1 

for num, count in numDict.items():
    # print(str(num) + ': ' + str(count) + 'lan')
    print(f"{num}: {count} lần")
