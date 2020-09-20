rnaTable = {
'AAA': 'K',
'AAC': 'N',
'AAG': 'K',
'AAU': 'N',
'ACA': 'T',
'ACC': 'T',
'ACG': 'T',
'ACU': 'T',
'AGA': 'R',
'AGC': 'S',
'AGG': 'R',
'AGU': 'S',
'AUA': 'I',
'AUC': 'I',
'AUG': 'M',
'AUU': 'I',
'CAA': 'Q',
'CAC': 'H',
'CAG': 'Q',
'CAU': 'H',
'CCA': 'P',
'CCC': 'P',
'CCG': 'P',
'CCU': 'P',
'CGA': 'R',
'CGC': 'R',
'CGG': 'R',
'CGU': 'R',
'CUA': 'L',
'CUC': 'L',
'CUG': 'L',
'CUU': 'L',
'GAA': 'E',
'GAC': 'D',
'GAG': 'E',
'GAU': 'D',
'GCA': 'A',
'GCC': 'A',
'GCG': 'A',
'GCU': 'A',
'GGA': 'G',
'GGC': 'G',
'GGG': 'G',
'GGU': 'G',
'GUA': 'V',
'GUC': 'V',
'GUG': 'V',
'GUU': 'V',
'UAA':  '',
'UAC': 'Y',
'UAG': '',
'UAU': 'Y',
'UCA': 'S',
'UCC': 'S',
'UCG': 'S',
'UCU': 'S',
'UGA': '',
'UGC': 'C',
'UGG': 'W',
'UGU': 'C',
'UUA': 'L',
'UUC': 'F',
'UUG': 'L',
'UUU': 'F'
}


def proteinTranslation(rnaPattern):
    result = ''
    for i in range(0, len(rnaPattern), 3):
        result += rnaTable[rnaPattern[i:i + 3:]]
    # print(result)
    return result


def dnkTranscribe(dnk):
    if 'T' in dnk:
        dnkresult = dnk.replace('T', 'U')
    elif 'U' in dnk:
        dnkresult = dnk.replace('U', 'T')
    else:
        dnkresult = dnk
    return dnkresult


def reverseDnkTranscribe(dnk):
    # dnk = str(input())
    reversDnk = ''
    pairs = {'A': 'T', 'C': 'G', 'G': 'C', "T": 'A'}
    for i in dnk:
        reversDnk += pairs[i]
    reversDnk = reversDnk[::-1]
    return reversDnk


dna = str(input())
geneticCode = str(input())
result = []
# for i in range(0, len(dna) - len(geneticCode), len(geneticCode) * 3):
for i in range(0, len(dna) - len(geneticCode) * 3, 1):
    tmp = dna[i:i+len(geneticCode) * 3:]
    if proteinTranslation(dnkTranscribe(tmp)) == geneticCode:
        result.append(tmp)
    elif proteinTranslation(dnkTranscribe(reverseDnkTranscribe(tmp))) == geneticCode:
        result.append(tmp)
for j in result:
    print(j)
