from half_cell_reaction import balance_acid, balance_base, balance_electron
from molecule_identifier import Reaction


# ClO3¯ + SO2 ---> SO42¯ + Cl¯
# reaction = {'reactant': [Molecule('Cl1O3', -1),Molecule('S1O2', 0)],
#             'product': [Molecule('S1O4', -2), Molecule('Cl1', -1)]}
reaction = Reaction('(1)Cl1O3[-1] + (1)S1O2[0]', '(1)S1O4[-2] + (1)Cl1[-1]')

# Special Case: P4 ---> H2PO2 + PH3
# reaction = {'reactant': [Molecule('P4', 0)],
#             'product': [Molecule('P1H3', 0),Molecule('H2P1O2', -1)]}

# Cl2 ---> ClO- + Cl-
# reaction = {'reactant': [Molecule('Cl2', 0), Molecule('Cl2', 0)],
#             'product': [Molecule('Cl1', -1), Molecule('Cl1O1', -1)]}

# H2O2 ---> H2O + O2
# reaction = {'reactant': [Molecule('H2O2', 0), Molecule('H2O2', 0)],
#             'product': [Molecule('H2O1', 0), Molecule('O2', 0)]}

reaction.print_rxn()

(red_rxn, ox_rxn) = reaction.split_rxn()
red_rxn.print_rxn()
ox_rxn.print_rxn()

red_rxn = balance_acid(red_rxn)
ox_rxn = balance_acid(ox_rxn)
red_rxn.print_rxn()
ox_rxn.print_rxn()

# NH3 + ClO¯ ---> N2H4 + Cl¯
""" reaction = Reaction('(1)Cl1O1[-1] + (1)N1H3[0]', '(1)Cl1[-1] + (1)N2H4[0]')
reaction.print_rxn()

(red_rxn, ox_rxn) = reaction.split_rxn()
red_rxn.print_rxn()
ox_rxn.print_rxn()

red_rxn = balance_base(red_rxn)
ox_rxn = balance_base(ox_rxn)
red_rxn.print_rxn()
ox_rxn.print_rxn() """

(red_rxn, ox_rxn) = balance_electron(red_rxn, ox_rxn)
red_rxn.print_rxn()
ox_rxn.print_rxn()

reaction.merge_rxn(red_rxn, ox_rxn)
reaction.print_rxn()
