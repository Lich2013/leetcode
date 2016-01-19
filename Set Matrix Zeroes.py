class Solution(object):
    def setZeroes(self, matrix):
        index1 = []
        index2 = []
        for i, j in self.yeildMatrix(matrix):
            index1.append(i)
            index2.append(j)
        for index, i in enumerate(index1):
            j = index2[index]
            matrix[i][:] = [0] * len(matrix[i])
            print(matrix[i])
            for y in matrix:
                y[j] = 0
        print(matrix)
    def yeildMatrix(self, matrix):
        for index1, x in enumerate(matrix):
            for index2, y in enumerate(x):
                if y == 0:
                    yield index1, index2
