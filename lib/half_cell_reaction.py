import numpy as np
from .molecule_identifier import Reaction


def balance_medium(reaction: Reaction, medium: str):
    # Balancing Central Atom Start
    lcm = np.lcm(reaction.get_side('reactant')[0].get_central_atom(), reaction.get_side('product')[0].get_central_atom())
    multiplier = {'reactant': int(lcm / reaction.get_side('reactant')[0].get_central_atom()), 'product': int(lcm / reaction.get_side('product')[0].get_central_atom())}

    for molecule in reaction.reactants:
        reaction.reactants[molecule].coff *= multiplier['reactant']
    for molecule in reaction.products:
        reaction.products[molecule].coff *= multiplier['product']
    # Balancing Central Atom End
    # print(reactant, product)

    # Balancing Oxygen Atom Start
    water_added = sum(molecule.get_atom('O') for molecule in reaction.get_side('reactant')) - sum(elem.get_atom('O') for elem in reaction.get_side('product'))
    # print(water_added)
    reaction.add_molecule('H2O1', 0, -water_added)
    # Balancing Oxygen Atom End
    # print(reactant, product)

    if medium == 'acid':
        # Balancing Hydrogen Atom Start
        hydrogen_added = sum(molecule.get_atom('H') for molecule in reaction.get_side('reactant')) - sum(elem.get_atom('H') for elem in reaction.get_side('product'))
        # print(hydrogen_added)
        reaction.add_molecule('H1', +1, -hydrogen_added)
        # Balancing Oxygen Atom End
        # print(reactant, product)
    else:
        # Balancing Hydrogen Atom Start
        water_added = sum(molecule.get_atom('H') for molecule in reaction.get_side('reactant')) - sum(elem.get_atom('H') for elem in reaction.get_side('product'))
        # print(water_added)
        reaction.add_molecule('H2O1', 0, -water_added)
        # Balancing Hydrogen Atom End
        # print(reactant, product)

        # Coverting to base medium
        hydroxide_added = water_added
        # print(hydroxide_added)
        reaction.add_molecule('O1H1', -1, hydroxide_added)
        # print(reactant, product)

    return reaction


def balance_electron(red_rxn: Reaction, ox_rxn: Reaction):
    reduction_transferred_electron = abs(sum(molecule.get_charge() for molecule in red_rxn.get_side('reactant')) - sum(elem.get_charge() for elem in red_rxn.get_side('product')))
    oxidation_transferred_electron = abs(sum(molecule.get_charge() for molecule in ox_rxn.get_side('product')) - sum(elem.get_charge() for elem in ox_rxn.get_side('reactant')))

    # print(reduction_transferred_electron, oxidation_transferred_electron)
    total_transferred_electron = np.lcm(reduction_transferred_electron, oxidation_transferred_electron)
    multiplier = {'red': int(total_transferred_electron / reduction_transferred_electron), 'ox': int(total_transferred_electron / oxidation_transferred_electron)}

    for molecule in red_rxn.reactants:
        red_rxn.reactants[molecule].coff *= multiplier['red']

    for molecule in red_rxn.products:
        red_rxn.products[molecule].coff *= multiplier['red']

    for molecule in ox_rxn.reactants:
        ox_rxn.reactants[molecule].coff *= multiplier['red']

    for molecule in ox_rxn.products:
        ox_rxn.products[molecule].coff *= multiplier['red']

    # print(red_rxn)
    # print(ox_rxn)
    return (red_rxn, ox_rxn)
