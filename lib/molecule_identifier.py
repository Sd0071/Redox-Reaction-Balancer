import re
from . import atomic_symbols


class Molecule:
    def __init__(self, molecule: str, coff: int = 1):
        molecule_regex = '(.+?)\[(.+?)\]'
        molecule_pattern = re.compile(molecule_regex, re.UNICODE)
        (molecule, charge) = re.match(molecule_pattern, molecule).groups()

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
        self.charge = int(charge)
        self.coff = int(coff)

    def get_atom(self, atom: str):
        return self.atoms[atom] * self.coff if atom in self.atoms else 0

    # UPDATE: Conversion from ionic to covalent
    def set_atom(self, atom: str, num: int):
        if num <= 0:
            del self.atoms[atom]
        else:
            self.atoms[atom] = num

    def get_central_atom(self):
        return self.atoms[self.central_atom] * self.coff

    def get_charge(self):
        return self.charge * self.coff

    # UPDATE: Properly find Oxidation State
    def get_os(self):
        total_charge = self.charge
        ligand_charge = (self.get_atom('H')*(+1) + self.get_atom('O')*(-2) + self.get_atom('S')*(-2))
        return (total_charge - ligand_charge) / self.get_central_atom()


class Reaction:
    def __init__(self, reactants: str = '', products: str = ''):
        def parse_side(reaction):
            molecules = {}
            molecule_regex = '\((.+?)\)(.+?\])'
            molecule_pattern = re.compile(molecule_regex)

            for molecule in re.findall(molecule_pattern, reaction):
                (coff, symbol) = molecule
                molecules[symbol] = Molecule(symbol, coff)

            return molecules

        self.reactants = parse_side(reactants)
        self.products = parse_side(products)

    def print_rxn(self, before: str = '', after: str = ''):
        def print_side(side):
            for symbol in side:
                molecule = side[symbol]
                print('(', molecule.coff, ')',  sep='', end='')

                for atom in molecule.atoms:
                    print(atom, sep='', end='')
                    print(molecule.atoms[atom], sep='', end='')

                print('[', molecule.charge, ']', ' + ',  sep='', end='')

        print(before, end='')
        print_side(self.reactants)
        print('\b\b\b', ' ---> ', end='')

        print_side(self.products)
        print('\b\b\b', '      ', end='')
        print(after, '\n')

    def get_side(self, side: str):
        side = self.reactants if side == 'reactant' else self.products
        return list(side.values())

    def add_molecule(self, symbol: str, coff: int = 1):
        # Positive Coff means in reactant side
        # Negative Coff means in product side
        same_side = self.reactants if coff >= 0 else self.products
        opp_side = self.reactants if coff < 0 else self.products
        coff = -abs(coff)
        # Adding to the opposite side with negative sign
        if symbol in opp_side:
            opp_side[symbol].coff += coff
        else:
            opp_side[symbol] = Molecule(symbol, coff)

        # Removing form the opposite side if needed
        if opp_side[symbol].coff > 0:
            return

        coff = -opp_side[symbol].coff
        opp_side.pop(symbol)

        # Adding to the same side form the opposite side sign inverted
        if symbol in same_side:
            same_side[symbol].coff += coff
        else:
            same_side[symbol] = Molecule(symbol, coff)

        # Removing form the same side if needed
        if same_side[symbol].coff > 0:
            return

        coff = 0
        same_side.pop(symbol)

    def remove_molecule(self, symbol: str, coff: int = 0):
        if coff > 0:
            if symbol in self.reactants:
                self.reactants[symbol].coff -= min(self.reactants[symbol].coff, abs(coff))
        elif coff < 0:
            if symbol in self.products:
                self.products[symbol].coff -= min(self.products[symbol].coff, abs(coff))
        else:
            if symbol in self.reactants:
                self.reactants.pop(symbol)

            if symbol in self.products:
                self.products.pop(symbol)

    def split_rxn(self):
        reduction_reaction = Reaction()
        oxidation_reaction = Reaction()

        for reactant_symbol in self.reactants:
            for product_symbol in self.products:
                reactant = self.reactants[reactant_symbol]
                product = self.products[product_symbol]

                if reactant.central_atom == product.central_atom:
                    if reactant.get_os() > product.get_os():
                        reduction_reaction.add_molecule(reactant_symbol, reactant.coff)
                        reduction_reaction.add_molecule(product_symbol, -product.coff)
                    else:
                        oxidation_reaction.add_molecule(reactant_symbol, reactant.coff)
                        oxidation_reaction.add_molecule(product_symbol, -product.coff)

        return (reduction_reaction, oxidation_reaction)

    def merge_rxn(self, reaction):
        def merge_side(side, side_rxn):
            side = 1 if side == 'reactant' else -1

            for molecule_symbol in side_rxn:
                molecule = side_rxn[molecule_symbol]
                self.add_molecule(molecule_symbol, side * molecule.coff)

        merge_side('reactant', reaction.reactants)
        merge_side('product', reaction.products)

        return self
