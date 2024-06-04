import math
import cirq

'''
Questions:
    How to initialize and build a circuit?
    How to sample from a circuit?
    How to represent Paulis?
'''

class ShadowTomography:

    def __init__(self, circuit):
        self.circuit = circuit
        self.circuit_op = cirq.CircuitOperation(circuit.freeze())
        self.num_qubits = cirq.num_qubits(circuit)
        self.bell_samples = []
        self.support_graph = []
        self.colours = {}
        self.Pauli_lookup = {}
        self.colour_samples = {}
    
    def BellSample(self, num_samples):
        # Use circuit.freeze() and cirq.CircuitOperation()
        self.bell_samples = []
    
    def magnitude(self, Pauli):
        return 0
    
    def BuildGraph(self, Pauli_list, eps):
        for P in Pauli_list:
            if self.magnitude(P) >= eps:
                self.support_graph = []
    
    def ColourGraph(self, ):
        self.colours = {}
        self.colour_lookup = {}
    
    def MeasureColour(self, c, num_samples):
        self.colour_samples[c] = []
    
    def expectation(self, Pauli):
        if Pauli not in self.Pauli_lookup:
            raise ValueError('Requested Pauli not in list of observables.')
        return 0
    
    def RunShadowTomography(self, Pauli_list, eps):
        self.BellSample(math.ceil(1 / eps ** 4))
        self.BuildGraph(Pauli_list, eps)
        self.ColourGraph()
        for c in self.colours:
            self.MeasureColour(c, math.ceil(1 / eps ** 2))
    
    def PauliShadowTomography(self, eps):
        Pauli_list = []
        self.RunShadowTomography(Pauli_list, eps)
    
    def MajoranaShadowTomography(self, k, eps):
        Pauli_list = []
        self.RunShadowTomography(Pauli_list, eps)


if __name__ == '__main__':
    qubits = cirq.GridQubit.square(3)
    cz01 = cirq.CZ(qubits[0], qubits[1])
    x2 = cirq.X(qubits[2])
    cz12 = cirq.CZ(qubits[1], qubits[2])
    moment0 = cirq.Moment([cz01, x2])
    moment1 = cirq.Moment([cz12])
    C = cirq.Circuit((moment0, moment1))
    print(C)

