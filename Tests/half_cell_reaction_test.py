import unittest
import half_cell_reaction as hcr


class TestBalanceAcidic(unittest.TestCase):
    # 1: ClO3¯ + SO2 ---> SO42¯ + Cl¯
    def test_1(self):
        # Reduction Half Reaction
        # ClO(3-) ---> Cl-
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': -1}}
        # 6H+ + ClO(3-) + 6e- ---> Cl- + 3H2O
        output_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 6, 'charge': 5},
                                'product': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 6, 'charge': -1}}

        self.assertDictEqual(hcr.balance_acid(input_reduction_rxn), output_reduction_rxn, 'Reduction in acidic medium')

        # Oxidation Half Reaction
        # SO2 ---> SO4(2-)
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 2, 'hydrogen': 0, 'charge': 0},
                               'product': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -2}}
        # 2H2O + SO2(+1) ---> SO4(2-) + 4H+ + e-
        # every thing divided by 3
        output_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 4, 'charge': 0},
                                'product': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 4, 'charge': +2}}

        self.assertDictEqual(hcr.balance_acid(input_oxidation_rxn), output_oxidation_rxn, 'Oxidation in acidic medium')

    # 2: H2S + NO3¯ ---> S8 + NO
    def test_2(self):
        # Reduction Half Reaction
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 1, 'hydrogen': 0, 'charge': 0}}
        # output_reduction_rxn['reagent'] = +4
        output_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 4, 'charge': +3},
                                'product': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 4, 'charge': 0}}

        self.assertDictEqual(hcr.balance_acid(input_reduction_rxn), output_reduction_rxn, 'Reduction in acidic medium')

        # Oxidation Half Reaction
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 2, 'charge': 0},
                               'product': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 0, 'charge': 0}}
        output_oxidation_rxn = {'reagent': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 16, 'charge': 0},
                                'product': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 16, 'charge': +16}}

        self.assertDictEqual(hcr.balance_acid(input_oxidation_rxn), output_oxidation_rxn, 'Oxidation in acidic medium')

    # 3: MnO4¯ + H2S ---> Mn2+ + S8
    def test_3(self):
        # Reduction Half Reaction
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}
        output_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 8, 'charge': +7},
                                'product': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 8, 'charge': +2}}

        self.assertDictEqual(hcr.balance_acid(input_reduction_rxn), output_reduction_rxn, 'Reduction in acidic medium')

        # Oxidation Half Reaction
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 2, 'charge': 0},
                               'product': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 0, 'charge': 0}}
        output_oxidation_rxn = {'reagent': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 16, 'charge': 0},
                                'product': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 16, 'charge': +16}}

        self.assertDictEqual(hcr.balance_acid(input_oxidation_rxn), output_oxidation_rxn, 'Oxidation in acidic medium')


""" class TestBalanceBasic(unittest.TestCase):
    # Example #1: ClO3¯ + SO2 ---> SO42¯ + Cl¯
    def test_1(self):
        # Reduction Half Reaction
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': 2}}
        output_reduction_rxn = {'reagent': {'central_atom': 1.0, 'oxygen': 4.0, 'hydrogen': 8.0, 'charge': 7.0},
                                'product': {'central_atom': 1.0, 'oxygen': 4.0, 'hydrogen': 8.0, 'charge': 2.0}}

        self.assertDictEqual(hcr.balance_base(input_reduction_rxn), output_reduction_rxn, 'Reduction in basic medium')

        # Oxidation Half Reaction
        input_oxidation_rxn = {'reagent': {'central_atom': 2, 'oxygen': 4, 'hydrogen': 0, 'charge': -2},
                               'product': {'central_atom': 1, 'oxygen': 2, 'hydrogen': 0, 'charge': 0}}
        output_oxidation_rxn = {'reagent': {'central_atom': 2.0, 'oxygen': 4.0, 'hydrogen': 0.0, 'charge': -2.0},
                                'product': {'central_atom': 2.0, 'oxygen': 4.0, 'hydrogen': 0.0, 'charge': 0.0}}

        self.assertDictEqual(hcr.balance_base(input_oxidation_rxn), output_oxidation_rxn, 'Oxidation in basic medium')
 """
