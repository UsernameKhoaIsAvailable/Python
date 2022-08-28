a = {


    "so chan": [2, 4, 6],


    "so le": [1, 3, 7, 9]


}


b = {


    "so chan": [8, 10, 12, 14],


    "so am": [-1, -2, -8, -10]


}


# aKeys = list(a.keys())


# bKeys = list(b.keys())


# for i in range(len(aKeys)):


#     for k in range(len(bKeys)):


#         if aKeys[i] == bKeys[k]:


#             a[aKeys[i]] += b[bKeys[k]]
#         else:


#             for r in range(len(aKeys)):


#                 if aKeys[r] == bKeys[k]:
#                     break
#                 else:


#                     a.update({bKeys[k]:b[bKeys[k]]})


result = a.copy()


for key, num_list in b.items():
    if key in result:

        result[key] = result[key] + num_list
    else:
        result[key] = num_list


print(result)
