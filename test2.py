unu = ['  #', '  #', '  #', '  #', '  #']
doi = ['###', '  #', '###', '#  ', '###']
trei = ['###', '  #', '###', '  #', '###']
patru = ['# #', '# #', '###', '  #', '  #']
cinci = ['###', '#  ', '###', '  #', '###']
sase = ['###', '#  ', '###', '# #', '###']
sapte = ['###', '  #', '  #', '  #', '  #']
opt = ['###', '# #', '###', '# #', '###']
noua = ['###', '# #', '###', '  #', '  #']

listaCifre = [unu, doi, trei, patru, cinci, sase, sapte, opt, noua]

def unesteCifre (nr):
    global listaCifre
    totalCifre =['', '', '', '', '']
    for n in nr:
        for i in range(5):
            totalCifre[i] += listaCifre[int(n)-1][i]
            totalCifre[i] += ' '
    return totalCifre

def printNr(nr):
    for i in range(5):
        print(nr[i])

numarIntrodus = input("Introdu un numar: ")
nrList = unesteCifre(numarIntrodus)

printNr(nrList)
