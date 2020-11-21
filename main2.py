# Input ------------------------------------
s = str(input())
t = str(input())
# ------------------------------------------
matrix = [[0] * (len(t) + 1) for i in range(len(s) + 1)]


def LCS_DYN(x, y):
    L = matrix
    LCS = []
    x_i, y_i = len(x) - 1, len(y) - 1
    while x_i >= 0 and y_i >= 0:
        if x[x_i] == y[y_i]:
            LCS.append(x[x_i])
            x_i, y_i = x_i - 1, y_i - 1
        elif L[x_i - 1][y_i] > L[x_i][y_i - 1]:
            x_i -= 1
        else:
            y_i -= 1
    LCS.reverse()
    return LCS


n = len(s)
m = len(t)
maxvalue = 0
c = -1
r = -1
result = ''
for column in range(1, n + 1):
    for row in range(1, m + 1):
        matrix[column][0] = matrix[column - 1][0]
        diag = 0
        if s[column - 1] == t[row - 1]:
            diag = 1
        matrix[column][row] = max(matrix[column - 1][row], matrix[column][row - 1], matrix[column - 1][row - 1] + diag)


result = ''.join(LCS_DYN(t, s))
print(matrix[n][m])
print(result)
