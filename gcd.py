import matrix

class extended_gcd_solver:

    #add other constructors/exceptions
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.quotient_list = []
        self.gcd = self.gcd_solver(self.a, self.b)
        #list of matricies
        self.quotient_matricies = self.quotient_matricies_solver(self.quotient_list)
        self.xy = self.getresults(self.quotient_matricies)

    def gcd_solver(self, a, b):
        if b == 0:
            return a
        else:
            #Integer division
            self.quotient_list.append(a//b)
            return self.gcd_solver(b, a%b)

    def quotient_matricies_solver(self, list):
        multiplying_quotient_list = []
        quotient_matrix_list = []
        for i in list:
            #make square matrix
            ith_matrix = matrix.Matrix(2,2)
            #instantiate data
            ith_matrix.setData([[0, 1], [1, i]])
            multiplying_quotient_list.append(ith_matrix)
        #create first 2 matricies before iteratively creating rest
        initial_quotient_matrix = matrix.Matrix(2,2)
        initial_quotient_matrix.setData([[0, 1], [1, 0]])
        quotient_matrix_list.append(initial_quotient_matrix)
        for i in range(len(multiplying_quotient_list)):
            new_matrix = quotient_matrix_list[i].multiply(multiplying_quotient_list[i])
            quotient_matrix_list.append(new_matrix)
        return quotient_matrix_list

    def getresults(self, list):
        answer_list = []
        answer_matrix = list[len(list) - 2]
        first = answer_matrix.data[0][1]
        second = answer_matrix.data[1][1]
        if(first*self.a + second*self.b*-1 == self.gcd):
            answer_list.append(first)
            answer_list.append(-1*second)
        else:
            answer_list.append(-1*first)
            answer_list.append(second)
        return answer_list



#getting the correct answers in matricies bit not in xy?
new_solver = extended_gcd_solver(463463, 38636)
print(new_solver.gcd)
print(new_solver.quotient_list)
for i in new_solver.quotient_matricies:
    print(i)
print(new_solver.xy)
