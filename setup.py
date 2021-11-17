from lib.half_cell_reaction import balance_electron, balance_medium
from lib.molecule_identifier import Reaction


def main():
    # Zn + Cu2+ ---> Zn2+ + Cu
    reaction = Reaction('(1)Zn1[0] + (1)Cu1[+2]', '(1)Zn1[+2] + (1)Cu1[0]')

    # As2S5(s) + NO3¯(aq) ---> H3AsO4(aq) + HSO4¯(aq) + NO2(g)
    # reaction = Reaction('(1)As2S5[0] + (1)N1O3[-1]', '(1)H3As1O4[0] + (1)H1S1O4[-1] + (1)N1O2[0]')

    # ClO3¯ + SO2 ---> SO42¯ + Cl¯
    # reaction = Reaction('(1)Cl1O3[-1] + (1)S1O2[0]', '(1)S1O4[-2] + (1)Cl1[-1]')

    # P4 ---> H2PO2 + PH3
    # reaction = Reaction('(1)P4[0]', '(1)H2P1O2[0] + (1)P1H3[0]')

    # Cl2 ---> ClO- + Cl-
    # reaction = Reaction('(1)Cl2[0]', '(1)Cl1O1[-1] + (1)Cl1[-1]')

    # H2O2 ---> H2O + O2
    # reaction = Reaction('(1)H2O2[0]', '(1)H2O1[0] + (1)O2[0]')

    # NH3 + ClO¯ ---> N2H4 + Cl¯
    # reaction = Reaction('(1)N1H3[0] + (1)Cl1O1[-1]', '(1)N2H4[0] + (1)Cl1[-1]')
    reaction.print_rxn('Initial: ')

    (red_rxn, ox_rxn) = reaction.split_rxn()
    red_rxn.print_rxn('Reduction: ')
    ox_rxn.print_rxn('Oxidation: ')

    red_rxn = balance_medium(red_rxn, 'acid')
    red_rxn.print_rxn('Reduction After Medium Balance: ')
    ox_rxn = balance_medium(ox_rxn, 'acid')
    ox_rxn.print_rxn('Oxidation After Medium Balance: ')

    (red_rxn, ox_rxn) = balance_electron(red_rxn, ox_rxn)
    red_rxn.print_rxn('Reduction After Balance Electron: ')
    ox_rxn.print_rxn('Oxidation After Balance Electron: ')

    reaction = red_rxn.merge_rxn(ox_rxn)
    reaction.print_rxn('Final: ')


if __name__ == "__main__":
    main()
