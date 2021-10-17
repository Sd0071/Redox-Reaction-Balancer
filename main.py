import half_cell_reaction as hcr

# 2: H2S + NO3¯ ---> S8 + NO
reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 0, 'charge': -1},
                 'product': {'central_atom': 1, 'oxygen': 1, 'hydrogen': 0, 'charge': 0}}
oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 2, 'charge': 0},
                 'product': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 0, 'charge': 0}}

reduction_rxn = hcr.balance_acid(reduction_rxn)
oxidation_rxn = hcr.balance_acid(oxidation_rxn)

print(reduction_rxn)
print(oxidation_rxn, '\n')

(reduction_rxn, oxidation_rxn) = hcr.balance_electron(reduction_rxn, oxidation_rxn)

# TODO: Finalizing the equation

print(reduction_rxn)
print(oxidation_rxn, '\n')
