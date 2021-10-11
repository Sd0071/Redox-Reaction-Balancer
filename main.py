import half_cell_reaction as hcr

# Example #3: Br¯ + MnO4¯ ---> MnO2 + BrO3¯
reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                 'product': {'central_atom': 1, 'oxygen': 2, 'hydrogen': 0, 'charge': 0}}
oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': -1},
                 'product': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 0, 'charge': -1}}


reduction_rxn = hcr.balance_acid(reduction_rxn)
oxidation_rxn = hcr.balance_acid(oxidation_rxn)

(reduction_rxn, oxidation_rxn) = hcr.balance_electron(reduction_rxn, oxidation_rxn)

print(reduction_rxn)
print(oxidation_rxn)
