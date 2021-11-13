import numpy as np
from molecule_identifier import Molecule


def balance_acid(reaction):
    (reactant, product) = (reaction['reactant'], reaction['product'])
    # Balancing Central Atom Start
    lcm = np.lcm(reactant[0].get_central_atom(), product[0].get_central_atom())
    multiplier = {'reactant': int(lcm / reactant[0].get_central_atom()), 'product': int(lcm / product[0].get_central_atom())}

    for i in range(len(reactant)):
        reactant[i].coff *= multiplier['reactant']
        product[i].coff *= multiplier['product']

    # Balancing Central Atom End
    # print(reactant, product)

    # Balancing Oxygen Atom Start
    water_added = sum(elem.get_atom('O') for elem in reactant) - sum(elem.get_atom('O') for elem in product)
    # print(water_added)
    if water_added < 0:
        reactant.append(Molecule('H2O1', 0, abs(water_added)))
    elif water_added > 0:
        product.append(Molecule('H2O1', 0, abs(water_added)))
    # Balancing Oxygen Atom End
    # print(reactant, product)

    # Balancing Hydrogen Atom Start
    hydrogen_added = sum(elem.get_atom('H') for elem in reactant) - sum(elem.get_atom('H') for elem in product)
    # print(hydrogen_added)
    if hydrogen_added < 0:
        reactant.append(Molecule('H1', +1, abs(hydrogen_added)))
    elif hydrogen_added > 0:
        product.append(Molecule('H1', +1, abs(hydrogen_added)))
    # Balancing Oxygen Atom End
    # print(reactant, product)

    return {'reactant': reactant, 'product': product}


def balance_base(reaction):
    (reactant, product) = (reaction['reactant'], reaction['product'])
    # Balancing Central Atom Start
    lcm = np.lcm(reactant[0].get_central_atom(), product[0].get_central_atom())
    multiplier = {'reactant': int(lcm / reactant[0].get_central_atom()), 'product': int(lcm / product[0].get_central_atom())}

    for i in range(len(reactant)):
        reactant[i].coff *= multiplier['reactant']
        product[i].coff *= multiplier['product']

    # Balancing Central Atom End
    # print(reactant, product)

    # Balancing Oxygen Atom Start
    water_added = sum(elem.get_atom('O') for elem in reactant) - sum(elem.get_atom('O') for elem in product)
    # print(water_added)
    if water_added < 0:
        reactant.append(Molecule('H2O1', 0, abs(water_added)))
    elif water_added > 0:
        product.append(Molecule('H2O1', 0, abs(water_added)))
    # Balancing Oxygen Atom End
    # print(reactant, product)

    # Balancing Hydrogen Atom Start
    water_added = sum(elem.get_atom('H') for elem in reactant) - sum(elem.get_atom('H') for elem in product)
    # print(water_added)
    if water_added < 0:
        reactant.append(Molecule('H2O1', 0, abs(water_added)))
    elif water_added > 0:
        product.append(Molecule('H2O1', 0, abs(water_added)))
    # Balancing Oxygen Atom End
    # print(reactant, product)

    hydroxide_added = water_added
    # print(hydroxide_added)
    # Coverting to base medium
    if hydroxide_added < 0:
        product.append(Molecule('O1H1', -1, abs(hydroxide_added)))
    elif hydroxide_added > 0:
        reactant.append(Molecule('O1H1', -1, abs(hydroxide_added)))

    # print(reactant, product)
    return {'reactant': reactant, 'product': product}


def balance_electron(red_rxn, ox_rxn):
    reduction_transferred_electron = abs(sum(elem.get_charge() for elem in red_rxn['reactant']) - sum(elem.get_charge() for elem in red_rxn['product']))
    oxidation_transferred_electron = abs(sum(elem.get_charge() for elem in ox_rxn['product']) - sum(elem.get_charge() for elem in ox_rxn['reactant']))

    # print(reduction_transferred_electron, oxidation_transferred_electron)
    total_transferred_electron = np.lcm(reduction_transferred_electron, oxidation_transferred_electron)
    multiplier = {'red': int(total_transferred_electron / reduction_transferred_electron), 'ox': int(total_transferred_electron / oxidation_transferred_electron)}

    for i in range(len(red_rxn['reactant'])):
        red_rxn['reactant'][i].coff *= multiplier['red']

    for i in range(len(red_rxn['product'])):
        red_rxn['product'][i].coff *= multiplier['red']

    for i in range(len(ox_rxn['reactant'])):
        ox_rxn['reactant'][i].coff *= multiplier['ox']

    for i in range(len(ox_rxn['product'])):
        ox_rxn['product'][i].coff *= multiplier['ox']

    # print(red_rxn)
    # print(ox_rxn)
    return (red_rxn, ox_rxn)
