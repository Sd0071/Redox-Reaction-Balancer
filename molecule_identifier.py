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
        return (self.get_atom('H')*(-1)+self.get_atom('O')*(+2))/self.get_central_atom()

    # UPDATE: From ionic to covalent
    def set_atom(self, atom, num):
        if num <= 0:
            del self.atoms[atom]
        else:
            self.atoms[atom] = num


def merge_molecule(reaction):
    # merge molecule of same side
    for side in reaction:
        for i in range(len(side)):
            for j in i:
                if side[i].molecule == side[j].molecule:
                    print(side[i].molecule, side[j].molecule)
                    # side[j].coff += side[i].coff
                    # del side[i]


def split_rxn(reaction):
    red_rxn = {'reactant': [], 'product': []}
    ox_rxn = {'reactant': [], 'product': []}

    for reactant in reaction['reactant']:
        for product in reaction['product']:
            if reactant.central_atom == product.central_atom:
                if reactant.get_os() > product.get_os():
                    red_rxn['reactant'].append(reactant)
                    red_rxn['product'].append(product)
                else:
                    ox_rxn['reactant'].append(reactant)
                    ox_rxn['product'].append(product)

    return (red_rxn, ox_rxn)


def merge_rxn(red_rxn, ox_rxn):
    reaction = {'reactant': [*red_rxn['reactant'], *ox_rxn['reactant']],
                'product': [*red_rxn['product'], *ox_rxn['product']]}

    for r in range(len(reaction['reactant'])):
        for p in range(len(reaction['product'])):
            if reaction['reactant'][r].molecule == reaction['product'][p].molecule:
                if reaction['reactant'][r].coff == 0 | reaction['product'][p].coff == 0:
                    continue
                elif reaction['reactant'][r].coff > reaction['product'][p].coff:
                    reaction['reactant'][r].coff -= reaction['product'][p].coff
                    reaction['product'][p].coff = 0
                elif reaction['reactant'][r].coff < reaction['product'][p].coff:
                    reaction['product'][p].coff -= reaction['reactant'][r].coff
                    reaction['reactant'][r].coff = 0
                else:
                    reaction['product'][p].coff = 0
                    reaction['reactant'][r].coff = 0

    reaction['reactant'] = filter(lambda molecule: bool(molecule.coff), reaction['reactant'])
    reaction['product'] = filter(lambda molecule: bool(molecule.coff), reaction['product'])

    return reaction


def print_rxn(reaction, extra=''):
    for side in reaction:
        for molecule in reaction[side]:
            print(molecule.coff,  sep='', end='')

            for atom in molecule.atoms:
                print(atom, '(', molecule.atoms[atom], ')', sep='', end='')

            print('[', molecule.charge, ']', ' + ',  sep='', end='')

        print('\b\b\b', ' ---> ', end='')

    print('\b\b\b\b\b\b', extra)
