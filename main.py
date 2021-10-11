import numpy as np
import half_cell_reaction as hcr

# Acid Reaction
reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1}, 'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': 2}}
oxidation_rxn = {'reagent': {'central_atom': 2, 'oxygen': 4, 'hydrogen': 0, 'charge': -2}, 'product': {'central_atom': 1, 'oxygen': 2, 'hydrogen': 0, 'charge': 0}}

# reduction_rxn = {'reagent':{'central_atom':1,'oxygen':4,'hydrogen':0,'charge':-1}, 'product':{'central_atom':1,'oxygen':0,'hydrogen':0,'charge':2}}
# oxidation_rxn = {'reagent':{'central_atom':1,'oxygen':0,'hydrogen':0,'charge':-1}, 'product':{'central_atom':2,'oxygen':0,'hydrogen':0,'charge':0}}

# reduction_rxn = {'reagent':{'central_atom':1,'oxygen':0,'hydrogen':0,'charge':+2}, 'product':{'central_atom':1,'oxygen':0,'hydrogen':0,'charge':0}}
# oxidation_rxn = {'reagent':{'central_atom':1,'oxygen':0,'hydrogen':0,'charge':0}, 'product':{'central_atom':1,'oxygen':0,'hydrogen':0,'charge':+2}}

# reduction_rxn = {'reagent':{'central_atom':4,'oxygen':0,'hydrogen':0,'charge':0}, 'product':{'central_atom' :1,'oxygen':0,'hydrogen':3,'charge':0}}
# oxidation_rxn = {'reagent':{'central_atom':4,'oxygen':0,'hydrogen':0,'charge':0}, 'product':{'central_atom':1,'oxygen':2,'hydrogen':2,'charge':-1}}

# Zn + NO3(-) ---> Zn(2+) + NO2
reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': 0}, 'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}
oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 0, 'charge': -1}, 'product': {'central_atom': 1, 'oxygen': 2, 'hydrogen': 0, 'charge': 0}}


reduction_rxn = hcr.balance_acid(reduction_rxn)
oxidation_rxn = hcr.balance_acid(oxidation_rxn)

reduction_transferred_electron = abs(int(reduction_rxn['reagent']['charge'] - reduction_rxn['product']['charge']))
oxidation_transferred_electron = abs(int(oxidation_rxn['product']['charge'] - oxidation_rxn['reagent']['charge']))

# print(reduction_transferred_electron)
# print(oxidation_transferred_electron)

total_transferred_electron = np.lcm(reduction_transferred_electron, oxidation_transferred_electron)

for i in reduction_rxn['reagent']:
    reduction_multiplier = total_transferred_electron / reduction_transferred_electron
    reduction_rxn['reagent'][i] *= reduction_multiplier
    reduction_rxn['product'][i] *= reduction_multiplier

    oxidation_multiplier = total_transferred_electron / oxidation_transferred_electron
    oxidation_rxn['reagent'][i] *= oxidation_multiplier
    oxidation_rxn['product'][i] *= oxidation_multiplier

print(reduction_rxn)
print(oxidation_rxn)
