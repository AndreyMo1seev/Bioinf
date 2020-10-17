def SubPeptide(pept, listOfSubPept):
    n = len(pept)
    pept1 = pept
    pept += pept
    for i in range(1,len(pept1)):
        for j in range(0, len(pept1)):
            listOfSubPept.append(pept[j: j + i])
    listOfSubPept.append(pept1)


def WeightList(listOfSubPept, wList, weightOfSubPept):
    for k in listOfSubPept:
        if len(k) == 1:
            wList.append(weightOfSubPept[k])
        else:
            tmp = 0
            for i in range(len(k)):
                tmp += weightOfSubPept[k[i:i + 1]]
            wList.append(tmp)

def Score(wList, expPeptide):
    c = 0
    tmp = expPeptide.copy()
    lst = []
    for w in wList:
        lst = []
        for e in expPeptide:
            if w == e and w not in lst:
                tmp.remove(w)
                c += 1
                lst.append(w)
                expPeptide = tmp
    return c

weightOfSubPept = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}
peptide = str(input())
sexpPeptide = str(input())
expPeptide = [int(x) for x in sexpPeptide.split()]
listOfSubPept = []
SubPeptide(peptide, listOfSubPept)
wList = [0]
WeightList(listOfSubPept, wList, weightOfSubPept)
print()
print(Score(wList, expPeptide))
