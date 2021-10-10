import numpy as np

def balance_acid(reagent,product):
    # Balancing Central Atom START
    lcm = np.lcm(reagent['central_atom'], product['central_atom'])
    multiplier = [lcm / reagent['central_atom'], lcm / product['central_atom']]

    for i in reagent:
        reagent[i]=reagent[i]*multiplier[0]
        product[i]=product[i]*multiplier[1]

    # Balancing Central Atom END
    # print(reagent,product)

    #Balancing Oxygen Atom Start
    water_added= reagent['oxygen'] - product['oxygen']
    # print(water_added)
    oxygen_added=abs(water_added)
    hydrogen_added=abs(water_added)*2
    if water_added<0:
        reagent['oxygen']+=oxygen_added
        reagent['hydrogen']+=hydrogen_added
    else:
        product['oxygen']+=oxygen_added
        product['hydrogen']+=hydrogen_added

    #Balancing Oxygen Atom End
    # print(reagent,product)

    #Balancing Hydrogen Atom Start
    hydrogen_ion_added= reagent['hydrogen']-product['hydrogen']
    # print(hydrogen_ion_added)
    hydrogen_added=abs(hydrogen_ion_added)
    charge_added=abs(hydrogen_ion_added)
    if hydrogen_ion_added<0:
        reagent['hydrogen']+=hydrogen_added
        reagent['charge']+=charge_added
    else:
        product['hydrogen']+=hydrogen_added
        product['charge']+=charge_added

    #Balancing Oxygen Atom End
    # print(reagent,product)
    return (reagent,product)

def balance_base(reagent,product):

    # Balancing Central Atom START
    # reagent={'central_atom':1,'oxygen':1,'hydrogen':0,'charge':-1}
    # product= {'central_atom':1,'oxygen':0,'hydrogen':0,'charge':-1}
    lcm = np.lcm(reagent['central_atom'], product['central_atom'])
    multiplier = [lcm / reagent['central_atom'], lcm / product['central_atom']]

    for i in reagent:
        reagent[i]=reagent[i]*multiplier[0]
        product[i]=product[i]*multiplier[1]

    #Balancing Oxygen Atom Start
    water_added= reagent['oxygen'] - product['oxygen']
    # print(water_added)
    oxygen_added=abs(water_added)
    hydrogen_added=abs(water_added)*2
    if water_added<0:
        reagent['oxygen']+=oxygen_added
        reagent['hydrogen']+=hydrogen_added
    else:
        product['oxygen']+=oxygen_added
        product['hydrogen']+=hydrogen_added

    #Balancing Oxygen Atom End
    # print(reagent,product)

    #Balancing Hydrogen Atom Start
    hydrogen_ion_added= reagent['hydrogen']-product['hydrogen']
    # print(hydrogen_ion_added)
    hydrogen_added=abs(hydrogen_ion_added)
    charge_added=abs(hydrogen_ion_added)
    if hydrogen_ion_added<0:
        reagent['hydrogen']+=hydrogen_added
        reagent['charge']+=charge_added
    else:
        product['hydrogen']+=hydrogen_added
        product['charge']+=charge_added

    #Balancing Hydrogen Atom End

    #coverting to base media
    hydroxide_ion_added = abs(hydrogen_ion_added) 

    reagent['oxygen']+=hydroxide_ion_added
    reagent['hydrogen']+=hydroxide_ion_added
    reagent['charge']-=hydroxide_ion_added

    product['oxygen']+=hydroxide_ion_added
    product['hydrogen']+=hydroxide_ion_added
    product['charge']-=hydroxide_ion_added

    print(reagent,product)

    return (reagent,product)
