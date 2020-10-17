def Mass(Peptide, weightOfSubPept):
    mas = 0
    for p in Peptide:
        mas += weightOfSubPept[p]
    return mas


def WeightList(listOfSubPept, wList, weightOfSubPept):
    wList = [0]
    for k in listOfSubPept:
        if len(k) == 1:
            wList.append(weightOfSubPept[k])
        else:
            tmp = 0
            for i in range(len(k)):
                tmp += weightOfSubPept[k[i:i + 1]]
            wList.append(tmp)
    wList.sort()
    return wList


def ParentMass(Spectrum):
    return max(Spectrum)


def Expand(Peptide, weightOfSubPept):
    oldPeptide = Peptide.copy()
    Peptide.clear()
    for i in range(len(oldPeptide)):
        for k in weightOfSubPept:
            Peptide.append(oldPeptide[i] + k)
    return Peptide


def SubPeptide(pept): # в презентации эта функция называется Cyclospectrum
    n = len(pept)
    listOfSubPept = []
    pept1 = pept
    pept += pept
    for i in range(1, len(pept1)):
        for j in range(0, len(pept1)):
            listOfSubPept.append(pept[j: j + i])
    listOfSubPept.append(pept1)
    return listOfSubPept

def LinearSubPeptide(pept):
    n = len(pept)
    listOfSubPept = []
    for i in range(1, len(pept)):
        for j in range(0, len(pept)):
            if pept[j: j + i] not in listOfSubPept:
                listOfSubPept.append(pept[j: j + i])
    listOfSubPept.append(pept)
    return listOfSubPept


def PrintPeptide(Peptide, weightOfSubPept, lst):
    tmpStr = ""
    for i in range(len(Peptide) - 1):
        tmpStr += str(weightOfSubPept[Peptide[i]])
        tmpStr += "-"
        # print(weightOfSubPept[Peptide[i]], "-", sep='', end="")
    tmpStr += str(weightOfSubPept[Peptide[len(Peptide) - 1]])
    # print(weightOfSubPept[Peptide[len(Peptide) - 1]])
    if tmpStr not in lst:
        print(tmpStr)
        lst.append(tmpStr)


def Consistens(Peptide, Spectrum, weightOfSubPept, wList):
    PeptideSpectr = WeightList(Peptide, wList, weightOfSubPept)
    tmpPeptSpectr = PeptideSpectr.copy()
    for s in Spectrum:
        for m in PeptideSpectr:
            if m == s:
                tmpPeptSpectr.remove(m)
                break
        PeptideSpectr = tmpPeptSpectr
    if PeptideSpectr:
        return False
    else:
        return True


weightOfSubPept = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'N': 114,
    'D': 115,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}
sSpectrum = input()
Spectrum = [int(x) for x in sSpectrum.split()]
Peptide = []
lst = [] # так как есть пептиды с одинаковыми массами (I & L , K & Q), то мне приходится перед тем как печатать, смотреть не было ли уже такого
# Для этого добавляю уже напечатанные в lst
for s in weightOfSubPept:
    Peptide.append(s)
listOfSubPept = []
wList = [0]
c = 0
ourPeptide = [] # ourPeptide - массы пептидов, которые присутствуют в нашем спектре
# for j in Spectrum:
#     for k in Peptide:
#         if j == weightOfSubPept[k]:
#             ourPeptide.append(k)
# Peptide = ourPeptide.copy()
while Peptide and c <= 100:
    tmpPept = Peptide.copy()
    for p in Peptide:
        # if p == "TCI":
            # print(1)
        if Mass(p, weightOfSubPept) == ParentMass(Spectrum):
            if WeightList(SubPeptide(p), wList, weightOfSubPept) == Spectrum:
                PrintPeptide(p, weightOfSubPept, lst)
                c += 1
            tmpPept.remove(p)
        elif not Consistens(LinearSubPeptide(p), Spectrum, weightOfSubPept, wList):
            tmpPept.remove(p)

    Peptide = tmpPept
    Peptide = Expand(Peptide, weightOfSubPept)
