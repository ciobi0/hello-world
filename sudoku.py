def gaseste_dublura(rand):
    for ind in range(len(rand)):
        if rand.find(rand[ind],ind+1, 8) != -1:
            return False
        else:
            continue
    return True

def verifica_rand(rand):
    if rand.isdigit() and len(rand) == 9 and gaseste_dublura(rand):
        print ("cifre corecte:" + rand)
        return True
    else:
        print ("cifre incorecte:" + rand)
        return False

matrice9x9 = [[0] * 9 for x in  range(9)]

# 295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672

for i in range(9):
    rand = input("introdu 9 cifre: ")
    if verifica_rand(rand) == False:
        print('sirul este gresit')
        break
    rand = list(rand)
    matrice9x9[i] = rand

# for i in range(9):
#     coloana = ""
#     for j in range(9):
#         coloana += matrice9x9[j][i]
#     verifica_rand(coloana)

for i in range(9):
    m3x3 = []
    m3x3.append(matrice9x9[i][:3])
    print(m3x3)

