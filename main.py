from molecule_identifier import Molecule, merge_rxn, split_rxn, print_rxn
from half_cell_reaction import balance_acid, balance_base, balance_electron


# ClO3¯ + SO2 ---> SO42¯ + Cl¯
# reaction = {'reactant': [Molecule('Cl1O3', 'Cl', -1),Molecule('S1O2', 'S', 0)],
#             'product': [Molecule('S1O4', 'S', -2), Molecule('Cl1', 'Cl', -1)]}

# Special Case: P4 ---> H2PO2 + PH3
# reaction = {'reactant': [Molecule('P4', 'P', 0)],
#             'product': [Molecule('P1H3', 'P', 0),Molecule('H2P1O2', 'P', -1)]}

# Cl2 ---> ClO- + Cl-
# reaction = {'reactant': [Molecule('Cl2', 'Cl', 0), Molecule('Cl2', 'Cl', 0)],
#             'product': [Molecule('Cl1', 'Cl', -1), Molecule('Cl1O1', 'Cl', -1)]}

# H2O2 ---> H2O + O2
# reaction = {'reactant': [Molecule('H2O2', 'O', 0), Molecule('H2O2', 'O', 0)],
#             'product': [Molecule('H2O1', 'O', 0), Molecule('O2', 'O', 0)]}

# NH3 + ClO¯ ---> N2H4 + Cl¯
reaction = {'reactant': [Molecule('Cl1O1', 'Cl', -1), Molecule('N1H3', 'N', 0)],
            'product': [Molecule('Cl1', 'Cl', -1), Molecule('N2H4', 'N', 0)]}

print_rxn(reaction, '\n')

(red_rxn, ox_rxn) = split_rxn(reaction)

print_rxn(red_rxn)
print_rxn(ox_rxn, '\n')

red_rxn = balance_base(red_rxn)
ox_rxn = balance_base(ox_rxn)

''' 
# NH3 + ClO¯ ---> N2H4 + Cl¯
red_rxn = {'reactant': [Molecule('Cl1O1', 'Cl', -1)], 'product': [Molecule('Cl1', 'Cl', -1)]}
ox_rxn = {'reactant': [Molecule('N1H3', 'N', 0)], 'product': [Molecule('N2H4', 'N', 0)]}

print_rxn(red_rxn)
print_rxn(ox_rxn, '\n')

red_rxn = balance_base(red_rxn)
ox_rxn = balance_base(ox_rxn) 
'''

print_rxn(red_rxn)
print_rxn(ox_rxn, '\n')

(red_rxn, ox_rxn) = balance_electron(red_rxn, ox_rxn)

print_rxn(red_rxn)
print_rxn(ox_rxn, '\n')

reaction = merge_rxn(red_rxn, ox_rxn)

print_rxn(reaction)
