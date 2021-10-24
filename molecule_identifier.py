import re

""" TODO: Add later
class Reaction:
    def __init__(self): """


class Molecule:
    def __init__(self, string,charge):
        atoms = {}

        atoms_symbols = re.split('\d',string)
        atoms_symbols = list(filter(None, atoms_symbols))
        atoms_numbers = re.split('\D',string)
        atoms_numbers = list(filter(None, atoms_numbers))

        for i in range(len(atoms_symbols)):
            atoms[atoms_symbols[i]] = atoms_numbers[i]
        
        self.atoms = atoms
        self.charge = charge
    
    # TODO: Find center
    # def find_center():


# molecule = Molecule("Mn1O4",-2)

# ClO3¯ + SO2 ---> SO42¯ + Cl¯
reaction = [Molecule('Cl1O3',-1),Molecule('S1O2',0)]
# molecule = Molecule("Cr2O7",-2)

for molecule in reaction:
    for atom in molecule.atoms:
        print(atom,'(',molecule.atoms[atom],')',sep='',end='')

    print('(',molecule.charge,')',sep='')