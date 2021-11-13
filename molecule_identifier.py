import re
import atomic_symbols


class Molecule:
    def __init__(self, molecule, charge, coff=1):
        atoms = {}
        atom_regex = '(\D{1,2})(\d)'
        atom_pattern = re.compile(atom_regex, re.UNICODE)
        central_atom_index = 118

        for atom in re.findall(atom_pattern, molecule):
            (symbol, count) = atom
            # print(symbol, count)
            atoms[symbol] = int(count)

            # UPDATE: Properly find central atom
            if central_atom_index > atomic_symbols.symbols.index(symbol):
                central_atom_index = atomic_symbols.symbols.index(symbol)

        self.atoms = atoms
        self.central_atom = atomic_symbols.symbols[central_atom_index]
        self.charge = charge
        self.coff = int(coff)

    def get_atom(self, atom):
        return self.atoms[atom] * self.coff if atom in self.atoms else 0

    def get_central_atom(self):
        return self.atoms[self.central_atom] * self.coff

    def get_charge(self):
        return self.charge * self.coff

    # UPDATE: Properly find Oxidation State
    def get_os(self):
        return (self.get_atom('H')*(-1)+self.get_atom('O')*(+2))/self.get_central_atom()

    # UPDATE: Conversion from ionic to covalent
    def set_atom(self, atom, num):
        if num <= 0:
            del self.atoms[atom]
        else:
            self.atoms[atom] = num


class Reaction:
    def __init__(self, reactant='', product=''):
        def parse_side(reaction):
            molecules = {}
            molecule_regex = '\((.+?)\)(.+?)\[(.+?)\]'
            molecule_pattern = re.compile(molecule_regex)

            for molecule in re.findall(molecule_pattern, reaction):
                (coff, symbol, charge) = molecule
                molecules[symbol] = Molecule(symbol, charge, coff)

            return molecules

        self.reactant = parse_side(reactant)
        self.product = parse_side(product)

    def add_molecule(self, symbol, charge, coff):
        # Positive Coff means in reactant side
        # Negative Coff means in product side
        same_side = self.reactant if coff >= 0 else self.product
        opp_side = self.reactant if coff < 0 else self.product
        coff = -abs(coff)
        # Adding to the opposite side with negative sign
        if symbol in opp_side:
            opp_side[symbol].coff += coff
        else:
            opp_side[symbol] = Molecule(symbol, charge, coff)

        # Removing form the opposite side if needed
        if opp_side[symbol].coff > 0:
            return

        coff = -opp_side[symbol].coff
        opp_side.pop(symbol)

        # Adding to the same side form the opposite side sign inverted
        if symbol in same_side:
            same_side[symbol].coff += coff
        else:
            same_side[symbol] = Molecule(symbol, charge, coff)

        # Removing form the same side if needed
        if same_side[symbol].coff > 0:
            return

        coff = 0
        same_side.pop(symbol)

    def remove_molecule(self, symbol):
        if symbol in self.reactant:
            self.reactant.pop(symbol)

        if symbol in self.product:
            self.product.pop(symbol)

    def split_rxn(self):
        reduction_reaction = Reaction()
        oxidation_reaction = Reaction()

        for reactant_symbol in self.reactant:
            for product_symbol in self.product:
                reactant = self.reactant[reactant_symbol]
                product = self.product[product_symbol]

                reactant_charge = reactant.charge
                product_charge = product.charge

                reactant_coff = reactant.coff
                product_coff = product.coff

                if reactant.central_atom == product.central_atom:
                    if reactant.get_os() > product.get_os():
                        reduction_reaction.add_molecule(reactant_symbol, reactant_charge, reactant_coff)
                        reduction_reaction.add_molecule(product_symbol, product_charge, product_coff)
                    else:
                        oxidation_reaction.add_molecule(reactant_symbol, reactant_charge, reactant_coff)
                        oxidation_reaction.add_molecule(product_symbol, product_charge, product_coff)

        return (reduction_reaction, oxidation_reaction)

    def merge_rxn(self):
        # TODO: Merge Reaction
        return

    def print_rxn(self, before='', after=''):
        def print_side(side):
            for symbol in side:
                molecule = side[symbol]
                print('(', molecule.coff, ')',  sep='', end='')

                for atom in molecule.atoms:
                    print(atom, sep='', end='')
                    print(molecule.atoms[atom], sep='', end='')

                print('[', molecule.charge, ']', ' + ',  sep='', end='')

        print(before, end='')
        print_side(self.reactant)
        print('\b\b\b', ' ---> ', end='')

        print_side(self.product)
        print(after)


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
