from half_cell_reaction import balance_acid, balance_base, balance_electron
from molecule_identifier import Reaction


# ClO3¯ + SO2 ---> SO42¯ + Cl¯
# reaction = Reaction('(1)Cl1O3[-1] + (1)S1O2[0]', '(1)S1O4[-2] + (1)Cl1[-1]')

# Special Case: P4 ---> H2PO2 + PH3
# reaction = Reaction('(1)P4[0]', '(1)H2P1O2[0] + (1)P1H3[0]')

# Cl2 ---> ClO- + Cl-
# reaction = Reaction('(1)Cl2[0]', '(1)Cl1O1[-1] + (1)Cl1[-1]')

# H2O2 ---> H2O + O2
# reaction = Reaction('(1)H2O2[0]', '(1)H2O1[0] + (1)O2[0]')

# NH3 + ClO¯ ---> N2H4 + Cl¯
reaction = Reaction('(1)N1H3[0] + (1)Cl1O1[-1]', '(1)N2H4[0] + (1)Cl1[-1]')
reaction.print_rxn('Initial: ')

(red_rxn, ox_rxn) = reaction.split_rxn()
red_rxn.print_rxn('Reduction: ')
ox_rxn.print_rxn('Oxidation: ')

""" red_rxn = balance_acid(red_rxn)
red_rxn.print_rxn('Reduction After Balance Acid: ')
ox_rxn = balance_acid(ox_rxn)
ox_rxn.print_rxn('Oxidation After Balance Acid: ') """

red_rxn = balance_base(red_rxn)
red_rxn.print_rxn('Reduction After Balance Base: ')
ox_rxn = balance_base(ox_rxn)
ox_rxn.print_rxn('Oxidation After Balance Base: ')

(red_rxn, ox_rxn) = balance_electron(red_rxn, ox_rxn)
red_rxn.print_rxn('Reduction After Balance Electron: ')
ox_rxn.print_rxn('Oxidation After Balance Electron: ')

reaction = red_rxn.merge_rxn(ox_rxn)
reaction.print_rxn('Final: ')
