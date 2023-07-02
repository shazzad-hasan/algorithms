class Matrix:
    def __init__(self, values, rows, cols):
        self.values = values
        self.rows = rows
        self.cols = cols
        
    def __getitem__(self, idxs):
        return self.values[idxs[0]][idxs[1]]
    
    def __setitem__(self, idxs, value):
        self.values[idxs[0]][idxs[1]] = value
        
    def print_mat(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.values[i][j], end=" ")
            print()
    
    def matadd(self, other):
        """ Elementwise sum """
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError("Matrices are not compatible.")
            
        result = Matrix([[0 for _ in range(self.cols)] for _ in range(self.rows)], self.rows, self.cols)
        for m in range(self.rows):
            for n in range(self.cols):
                result[m,n] = self.values[m][n] + other.values[m][n]
        return result
    
    def matsub(self, other):
        """ Elementwise difference """

        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError("Matrices are not compatible.")
            
        result = Matrix([[0 for _ in range(self.cols)] for _ in range(self.rows)], self.rows, self.cols)
        for m in range(self.rows):
            for n in range(self.cols):
                result[m,n] = self.values[m][n] - other.values[m][n]
        return result

    def elementwise_mul(self, other):
        """ Elementwise multiplication """
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError("Matrices are not compatible.")
        
        result = Matrix([[0 for _ in range(self.cols)] for _ in range(self.rows)], self.rows, self.cols)
        for m in range(self.rows):
            for n in range(self.cols):
                result[m,n] = self.values[m][n] * other.values[m][n]
        return result
            
    def matmul(self, other):
        """ Matrix multiplication"""

        if self.cols != other.rows:
            raise ValueError("Matrices are not compatible.")
            
        result = Matrix([[0 for _ in range(other.cols)] for _ in range(self.rows)], self.rows, other.cols)
        for m in range(self.rows):
            for n in range(other.cols):
                for k in range(self.cols):
                    result[m,n] += self.values[m][k] * other.values[k][n]
        return result
    
    def elementwise_div(self, other):
        """ Elementwise division """
        if self.rows != other.rows and self.cols != other.cols:
            raise ValueError("Matrices are not compatible.")
        
        result = Matrix([[0 for _ in range(self.cols)] for _ in range(self.rows)], self.rows, self.cols)
        for m in range(self.rows):
            for n in range(self.cols):
                result[m,n] = self.values[m][n] / other.values[m][n]
        return result
    

if __name__=="__main__":
    
    A = Matrix([[1,2],[3,4]], 2, 2)
    B = Matrix([[5,6],[7,8]], 2, 2)
    
    print("Elementwise sum:")
    add = A.matadd(B)
    add.print_mat()
    print()
    
    print("Elementwise subtraction:")
    sub = A.matsub(B)
    sub.print_mat()
    print()

    print("Elementwise multiplication:")
    elementwise_prod = A.elementwise_mul(B)
    elementwise_prod.print_mat()
    print()

    print("Elementwise division:")
    elementwise_division = A.elementwise_div(B)
    elementwise_division.print_mat()
    print()
    
    print("Matrix multiplication:")
    mul = A.matmul(B)
    mul.print_mat()
    print()