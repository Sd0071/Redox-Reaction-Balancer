import re




class Molecule:
    def __init__(self, molecule, central_atom, charge, coff=1):
        atoms = {}
        atom_regex = '(\D{1,2})(\d)'
        atom_pattern = re.compile(atom_regex, re.UNICODE)

        for atom in re.findall(atom_pattern, molecule):
            (symbol, count) = atom
            # print(symbol, count)
            atoms[symbol] = int(count)

        # print(atoms)
        self.molecule = molecule
        self.atoms = atoms
        self.central_atom = central_atom
        self.charge = charge
        self.coff = coff

    def get_atom(self, atom):
        return self.atoms[atom] * self.coff if atom in self.atoms else 0

    def get_central_atom(self):
        return self.atoms[self.central_atom] * self.coff

    def get_charge(self):
        return self.charge * self.coff

    def get_os(self):
        return (self.get_atom("H")*(-1)+self.get_atom("O")*(+2))/self.get_central_atom()

    # UPDATE: From ionic to covalent
    def set_atom(self, atom, num):
        if num <= 0:
            del self.atoms[atom]
        else:
            self.atoms[atom] = num
    

""" class Reaction:
    def __init__(self): """
def merge_molecule(reaction):
    # merge molecule of same side
    for side in reaction:
        for i in range(len(side)):
            for j in i:
                if side[i].molecule == side[j].molecule:
                    print(side[i].molecule, side[j].molecule)
                    # side[j].coff += side[i].coff
                    # del side[i]

def redox_identify(reaction):
    
    red_rxn = {"reactant" : [],"product" : []}
    ox_rxn = {"reactant" : [],"product" : []}
    
    for reactant in reaction['reactant']:
        for product in reaction['product']:
            
            if reactant.central_atom == product.central_atom:
                if reactant.get_os()>product.get_os():
                    red_rxn['reactant'].append(reactant)
                    red_rxn['product'].append(product)
                else :
                    ox_rxn['reactant'].append(reactant)
                    ox_rxn['product'].append(product)
    return (red_rxn,ox_rxn)

# def merge_rxn(reaction):


def print_rxn(reaction, extra=''):
    for side in reaction:
        for molecule in reaction[side]:
            print(molecule.coff,  sep='', end='')

            for atom in molecule.atoms:
                print(atom, '(', molecule.atoms[atom], ')', sep='', end='')

            print('[', molecule.charge, ']', ' + ',  sep='', end='')

        print('\b\b\b', ' ---> ', end='')

    print('\b\b\b\b\b\b', extra)
