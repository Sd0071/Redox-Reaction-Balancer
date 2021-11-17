<p align="center">
  <img alt="redox-reaction-logo" src="./assets/Icon.svg" width="256" height="256" />
</p>

# Redox Reaction Balancer

A python project to Balance any Redox Reaction

## **Get Started**

The setup.py is the entry point of the project.

First you need to create a reaction by using Reaction Class. In Reaction Class you need to add two parameters, reactants and products as a string.

The parameters should be formatted like this

**'Molecule_1 + Molecule_2 + ...', 'Molecule_3 + Molecule_4 + ..'**

- Like for CuSO4 + Zn → Cu + ZnSO4 You have to write "'(1)Cu1S1O4[0] + (1)Zn1[0]', '(1)Cu1[0] + (1)Zn1S1O4[0]'"

And the Molecules should be formatted like this

**(Number of Molecules)Atom_1_Symbol_Number Atom_2_Symbol_Number ...[Total Charge]**

- Like for Zinc chloride [ZnCl₂] You have to write "(1)Zn1Cl2[0]"
- Like for Water [H₂O] You have to write "(1)H2O1[0]"
- Like for Hydron [H+] You have to write "(1)H1[+1]"

### **Print Reaction**

To print the reaction you have to use **print_rxn()** method on Reaction class. Simply using **print_rxn()** with no parameter will just print the reaction. There are two optional parameters called **before**, **after** where you can input some string which be printed before and after respectively.

### **Split Reaction**

To split the reaction you have to use **split_rxn()** method on Reaction class. **split_rxn()** will split the reaction into **Reduction Reaction** and **Oxidation Reaction** and returns two Reaction object in a tuple.

### **Balancing in a Medium**

To get the balanced reaction you have to use a function called **balance_medium()**. Which takes two parameter called **reaction** and **medium**. **reaction** is a Reaction Object and **medium** is a string which could be 'acid' or 'base'. This function will return the balanced reaction in the given medium.

### **Balance the Electrons**

To balance the electron you have to use a function called **balance_electron()**. Which takes two parameter called **red_rxn** and **ox_rxn**. It balances the electron and returns the two balanced reaction in a tuple.

### **Merge the Reaction**

To get the final balanced reaction you have to use a method called **merge_rxn()** on Reaction class. You can use the method on either the Reduction Reaction or Oxidation Reaction and you provide the other reaction as parameter. It will merge the reaction and perform cancellation on both side if it is possible, and return the merge reaction.
