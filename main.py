from molecule_identifier import Molecule, print_rxn
from half_cell_reaction import balance_acid, balance_base, balance_electron

# ClO3¯ + SO2 ---> SO42¯ + Cl¯
red_rxn = {'reactant': [Molecule('Cl1O3', 'Cl', -1)], 'product': [Molecule('Cl1', 'Cl', -1)]}
ox_rxn = {'reactant': [Molecule('S1O2', 'S', 0)], 'product': [Molecule('S1O4', 'S', -2)]}

print_rxn(red_rxn)
print_rxn(ox_rxn, '\n')

red_rxn = balance_acid(red_rxn)
ox_rxn = balance_acid(ox_rxn)

""" 
# NH3 + ClO¯ ---> N2H4 + Cl¯
red_rxn = {'reactant': [Molecule('Cl1O1', 'Cl', -1)], 'product': [Molecule('Cl1', 'Cl', -1)]}
ox_rxn = {'reactant': [Molecule('N1H3', 'N', 0)], 'product': [Molecule('N2H4', 'N', 0)]}

print_rxn(red_rxn)
print_rxn(ox_rxn, '\n')

red_rxn = balance_base(red_rxn)
ox_rxn = balance_base(ox_rxn) 
"""

print_rxn(red_rxn)
print_rxn(ox_rxn, '\n')

(red_rxn, ox_rxn) = balance_electron(red_rxn, ox_rxn)

print_rxn(red_rxn)
print_rxn(ox_rxn, '\n')

# TODO: Cancellation
