class Hamiltonian:
    def __init__(self,matrix):
        self.n = len(matrix)
        self.adjacency_matrix = matrix
        self.path = [0]
    def hamiltonian_path(self):
        if self.solve(1):
            self.show_hamiltonian_path()
        else:
            print("no hamiltonian path")
    def solve(self,position):
        if position == self.n:
            return True
        for vertex_index in range(1,self.n):
            if self.feasible(vertex_index,position):
                self.path.append(vertex_index)
                if self.solve(position+1):
                    return True
                self.path.pop()
        return False
    def feasible(self,vertex,actual_position):
        if self.adjacency_matrix[self.path[actual_position-1]][vertex]==0:
            return False
        for i in range(actual_position):
            if self.path[i] == vertex:
                return False
        return True

    def show_hamiltonian_path(self):
        for v in self.path:
            print(v)


if __name__ == '__main__':
    m = [[0, 1, 0, 0, 0, 1],
         [1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1],
         [0, 0, 1, 1, 0, 1],
         [1, 0, 0, 1, 1, 0]]

    hamiltonian_path = Hamiltonian(m)
    hamiltonian_path.hamiltonian_path()