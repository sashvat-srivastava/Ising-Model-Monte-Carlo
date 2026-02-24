import numpy as np

choose = np.random.choice

IM_initial = np.zeros((10,10))
spins = [1,-1]
J = 1
k = 1.38
Temp = 2.269
def Probability(dE):
    p = np.exp(-1*dE/(k*Temp))
    return p

for r in range(10):
    for c in range(10):
       IM_initial[r,c] = choose(spins)

def neighbors(i, j, lattice):
    L = lattice.shape[0]
    n = [
        lattice[(i+1) % L, j],
        lattice[(i-1) % L, j],
        lattice[i, (j+1) % L],
        lattice[i, (j-1) % L]
    ]
    return n

def Hamiltonian(lattice):
    H = 0
    for r in range(lattice.shape[0]):
        for c in range(lattice.shape[0]):
            H += -1*J*(lattice[r,c])*(sum(neighbors(r,c,lattice)))
    return H/2

print(f'Initial Energy: {Hamiltonian(IM_initial)} Joules(e-23)')

def Metropolis(lattice):
    for i in range(10000):  

        a = choose(range(lattice.shape[0]))
        b = choose(range(lattice.shape[0]))  
        p = lattice[a,b]
        q = -1*p

        lattice1 = lattice.copy()
        lattice1[a,b] = q

        dE = Hamiltonian(lattice1)-Hamiltonian(lattice)

        if dE <= 0:
            lattice[a,b] = q
        else:
            prob = Probability(dE)
            if np.random.rand()<prob:
                lattice[a,b] = q

    return lattice

def print_lattice(lattice):
    for r in range(lattice.shape[0]):
        row = ""
        for c in range(lattice.shape[1]):
            if lattice[r, c] == 1:
                row += "O "
            else:
                row += "X "
        print(row)


IM_final = Metropolis(IM_initial)
print_lattice(IM_final)
print(f'final Energy is {Hamiltonian(IM_final)} Joules(e-23)')