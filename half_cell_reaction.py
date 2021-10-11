import numpy as np


def balance_acid(reaction):
    (reagent, product) = (reaction['reagent'], reaction['product'])
    # Balancing Central Atom Start
    lcm = np.lcm(reagent['central_atom'], product['central_atom'])
    multiplier = [lcm / reagent['central_atom'], lcm / product['central_atom']]

    for i in reagent:
        reagent[i] = int(reagent[i] * multiplier[0])
        product[i] = int(product[i] * multiplier[1])
    # Balancing Central Atom End
    # print(reagent,product)

    # Balancing Oxygen Atom Start
    water_added = reagent['oxygen'] - product['oxygen']
    # print(water_added)
    oxygen_added = abs(water_added)
    hydrogen_added = abs(water_added)*2
    if water_added < 0:
        reagent['oxygen'] += oxygen_added
        reagent['hydrogen'] += hydrogen_added
    else:
        product['oxygen'] += oxygen_added
        product['hydrogen'] += hydrogen_added
    # Balancing Oxygen Atom End
    # print(reagent,product)

    # Balancing Hydrogen Atom Start
    hydrogen_ion_added = reagent['hydrogen'] - product['hydrogen']
    # print(hydrogen_ion_added)
    hydrogen_added = abs(hydrogen_ion_added)
    charge_added = abs(hydrogen_ion_added)
    if hydrogen_ion_added < 0:
        reagent['hydrogen'] += hydrogen_added
        reagent['charge'] += charge_added
    else:
        product['hydrogen'] += hydrogen_added
        product['charge'] += charge_added
    # Balancing Oxygen Atom End
    # print(reagent,product)

    return {'reagent': reagent, 'product': product}


def balance_base(reaction):
    (reagent, product) = (reaction['reagent'], reaction['product'])
    # Balancing Central Atom Start
    lcm = np.lcm(reagent['central_atom'], product['central_atom'])
    multiplier = [lcm / reagent['central_atom'], lcm / product['central_atom']]

    for i in reagent:
        reagent[i] = int(reagent[i] * multiplier[0])
        product[i] = int(product[i] * multiplier[1])
    # Balancing Central Atom End

    # Balancing Oxygen Atom Start
    water_added = reagent['oxygen'] - product['oxygen']
    # print(water_added)
    oxygen_added = abs(water_added)
    hydrogen_added = abs(water_added) * 2
    if water_added < 0:
        reagent['oxygen'] += oxygen_added
        reagent['hydrogen'] += hydrogen_added
    else:
        product['oxygen'] += oxygen_added
        product['hydrogen'] += hydrogen_added
    # Balancing Oxygen Atom End
    # print(reagent,product)

    # Balancing Hydrogen Atom Start
    hydrogen_ion_added = reagent['hydrogen'] - product['hydrogen']
    # print(hydrogen_ion_added)
    hydrogen_added = abs(hydrogen_ion_added)
    charge_added = abs(hydrogen_ion_added)

    if hydrogen_ion_added < 0:
        reagent['hydrogen'] += hydrogen_added
        reagent['charge'] += charge_added
    else:
        product['hydrogen'] += hydrogen_added
        product['charge'] += charge_added
    # Balancing Hydrogen Atom End
    # print(reagent,product)

    # Coverting to base medium
    hydroxide_ion_added = abs(hydrogen_ion_added)

    reagent['oxygen'] += hydroxide_ion_added
    reagent['hydrogen'] += hydroxide_ion_added
    reagent['charge'] -= hydroxide_ion_added

    product['oxygen'] += hydroxide_ion_added
    product['hydrogen'] += hydroxide_ion_added
    product['charge'] -= hydroxide_ion_added

    # print(reagent,product)
    return {'reagent': reagent, 'product': product}


def balance_electron(reduction_rxn, oxidation_rxn):
    reduction_transferred_electron = abs(reduction_rxn['reagent']['charge'] - reduction_rxn['product']['charge'])
    oxidation_transferred_electron = abs(oxidation_rxn['product']['charge'] - oxidation_rxn['reagent']['charge'])

    # print(reduction_transferred_electron, oxidation_transferred_electron)
    total_transferred_electron = np.lcm(reduction_transferred_electron, oxidation_transferred_electron)

    for i in reduction_rxn['reagent']:
        reduction_multiplier = int(total_transferred_electron / reduction_transferred_electron)
        reduction_rxn['reagent'][i] *= reduction_multiplier
        reduction_rxn['product'][i] *= reduction_multiplier

        oxidation_multiplier = int(total_transferred_electron / oxidation_transferred_electron)
        oxidation_rxn['reagent'][i] *= oxidation_multiplier
        oxidation_rxn['product'][i] *= oxidation_multiplier

    # print(reduction_rxn)
    # print(oxidation_rxn)
    return (reduction_rxn, oxidation_rxn)
