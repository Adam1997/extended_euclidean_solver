class Matrix:

#functional
    def __init__(self, r, c):
        self.nrow = r
        self.ncol = c
        self.data = [[0]*r,[0]*c]

    #other parameterised constructors needed

    def getCol(self):
        return self.ncol

    def getRow(self):
        return self.nrow
    #setters

    def setData(self, list):
        for row in range(len(list)):
            for col in range(len(list[row])):
                self.data[row][col] = list[row][col]

    def multiply(self, other):
        #need to check if defined
        result = Matrix(self.getRow(), other.getCol())
        for row in range(self.getRow()):
            for col in range(other.getCol()):
                for item in range(self.getCol()):
                    result.data[row][col] += self.data[row][item] * other.data[item][col]
        return result

    def __str__(self):
        result = ""
        for row in range(len(self.data)):
            result = result + "["
            for col in range(len(self.data[row])):
                result = result + str(self.data[row][col]) + " "
            result = result + "] \n"
        return result
