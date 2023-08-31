l = [1,2,5,17,6,7,8]
# c = 0
maximo = l[0]
# while c < len(l):
#     if l[c]> maximo:
#         maximo = l[c]
#     l[c] += 5
#     print(l[c])
#     c += 1
# print("El valor maximo es", maximo)
# print(l)
for e in l:
    maximo = max(e,maximo)
print(maximo)
print(float('inf')-9)