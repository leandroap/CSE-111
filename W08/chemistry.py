# File: chemistry.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson08/prove.html

from formula import parse_formula

# Function to print some decorative elements
def print_elements(option): 
    break_line = "\n*****************************************************\n"
    header       = "* Welcome to Prove Milestone: Molar mass calculator *"
    footer       = "*                  Thank you! Bye.                  *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")

def make_periodic_table():
    periodic_table_dict = {
        # symbol: [name, atomic_mass"]
        "Ac" : ["Actinium",	227],
        "Ag" : ["Silver",	107.8682],
        "Al" : ["Aluminum",	26.9815386],
        "Ar" : ["Argon",	39.948],
        "As" : ["Arsenic",	74.9216],
        "At" : ["Astatine",	210],
        "Au" : ["Gold",	196.966569],
        "B" : ["Boron",	10.811],
        "Ba" : ["Barium",	137.327],
        "Be" : ["Beryllium",	9.012182],
        "Bi" : ["Bismuth",	208.9804],
        "Br" : ["Bromine",	79.904],
        "C" : ["Carbon",	12.0107],
        "Ca" : ["Calcium",	40.078],
        "Cd" : ["Cadmium",	112.411],
        "Ce" : ["Cerium",	140.116],
        "Cl" : ["Chlorine",	35.453],
        "Co" : ["Cobalt",	58.933195],
        "Cr" : ["Chromium",	51.9961],
        "Cs" : ["Cesium",	132.9054519],
        "Cu" : ["Copper",	63.546],
        "Dy" : ["Dysprosium",	162.5],
        "Er" : ["Erbium",	167.259],
        "Eu" : ["Europium",	151.964],
        "F" : ["Fluorine",	18.9984032],
        "Fe" : ["Iron",	55.845],
        "Fr" : ["Francium",	223],
        "Ga" : ["Gallium",	69.723],
        "Gd" : ["Gadolinium",	157.25],
        "Ge" : ["Germanium",	72.64],
        "H" : ["Hydrogen",	1.00794],
        "He" : ["Helium",	4.002602],
        "Hf" : ["Hafnium",	178.49],
        "Hg" : ["Mercury",	200.59],
        "Ho" : ["Holmium",	164.93032],
        "I" : ["Iodine",	126.90447],
        "In" : ["Indium",	114.818],
        "Ir" : ["Iridium",	192.217],
        "K" : ["Potassium",	39.0983],
        "Kr" : ["Krypton",	83.798],
        "La" : ["Lanthanum",	138.90547],
        "Li" : ["Lithium",	6.941],
        "Lu" : ["Lutetium",	174.9668],
        "Mg" : ["Magnesium",	24.305],
        "Mn" : ["Manganese",	54.938045],
        "Mo" : ["Molybdenum",	95.96],
        "N" : ["Nitrogen",	14.0067],
        "Na" : ["Sodium",	22.98976928],
        "Nb" : ["Niobium",	92.90638],
        "Nd" : ["Neodymium",	144.242],
        "Ne" : ["Neon",	20.1797],
        "Ni" : ["Nickel",	58.6934],
        "Np" : ["Neptunium",	237],
        "O" : ["Oxygen",	15.9994],
        "Os" : ["Osmium",	190.23],
        "P" : ["Phosphorus",	30.973762],
        "Pa" : ["Protactinium",	231.03588],
        "Pb" : ["Lead",	207.2],
        "Pd" : ["Palladium",	106.42],
        "Pm" : ["Promethium",	145],
        "Po" : ["Polonium",	209],
        "Pr" : ["Praseodymium",	140.90765],
        "Pt" : ["Platinum",	195.084],
        "Pu" : ["Plutonium",	244],
        "Ra" : ["Radium",	226],
        "Rb" : ["Rubidium",	85.4678],
        "Re" : ["Rhenium",	186.207],
        "Rh" : ["Rhodium",	102.9055],
        "Rn" : ["Radon",	222],
        "Ru" : ["Ruthenium",	101.07],
        "S" : ["Sulfur",	32.065],
        "Sb" : ["Antimony",	121.76],
        "Sc" : ["Scandium",	44.955912],
        "Se" : ["Selenium",	78.96],
        "Si" : ["Silicon",	28.0855],
        "Sm" : ["Samarium",	150.36],
        "Sn" : ["Tin",	118.71],
        "Sr" : ["Strontium",	87.62],
        "Ta" : ["Tantalum",	180.94788],
        "Tb" : ["Terbium",	158.92535],
        "Tc" : ["Technetium",	98],
        "Te" : ["Tellurium",	127.6],
        "Th" : ["Thorium",	232.03806],
        "Ti" : ["Titanium",	47.867],
        "Tl" : ["Thallium",	204.3833],
        "Tm" : ["Thulium",	168.93421],
        "U" : ["Uranium",	238.02891],
        "V" : ["Vanadium",	50.9415],
        "W" : ["Tungsten",	183.84],
        "Xe" : ["Xenon",	131.293],
        "Y" : ["Yttrium",	88.90585],
        "Yb" : ["Ytterbium",	173.054],
        "Zn" : ["Zinc",	65.38],
        "Zr" : ["Zirconium",	91.224]
    }

    return periodic_table_dict

def make_periodic_table_with_protons():
    periodic_table_dict = {
        # symbol: [name, atomic_mass, atomic_number]
        "Ac" : ["Actinium", 227, 89],
        "Ag" : ["Silver",   107.8682, 47],
        "Al" : ["Aluminum", 26.9815386, 13],
        "Ar" : ["Argon",    39.948, 18],
        "As" : ["Arsenic",  74.9216, 33],
        "At" : ["Astatine", 210, 85],
        "Au" : ["Gold", 196.966569, 79],
        "B" : ["Boron", 10.811, 5],
        "Ba" : ["Barium",   137.327, 56],
        "Be" : ["Beryllium",    9.012182, 4],
        "Bi" : ["Bismuth",  208.9804, 83],
        "Br" : ["Bromine",  79.904, 35],
        "C" : ["Carbon",    12.0107, 6],
        "Ca" : ["Calcium",  40.078, 20],
        "Cd" : ["Cadmium",  112.411, 48],
        "Ce" : ["Cerium",   140.116, 58],
        "Cl" : ["Chlorine", 35.453, 17],
        "Co" : ["Cobalt",   58.933195, 27],
        "Cr" : ["Chromium", 51.9961, 24],
        "Cs" : ["Cesium",   132.9054519, 55],
        "Cu" : ["Copper",   63.546, 29],
        "Dy" : ["Dysprosium",   162.5, 66],
        "Er" : ["Erbium",   167.259, 68],
        "Eu" : ["Europium", 151.964, 63],
        "F" : ["Fluorine",  18.9984032, 9],
        "Fe" : ["Iron", 55.845, 26],
        "Fr" : ["Francium", 223, 87],
        "Ga" : ["Gallium",  69.723, 31],
        "Gd" : ["Gadolinium",   157.25, 64],
        "Ge" : ["Germanium",    72.64, 32],
        "H" : ["Hydrogen",  1.00794, 1],
        "He" : ["Helium",   4.002602, 2],
        "Hf" : ["Hafnium",  178.49, 72],
        "Hg" : ["Mercury",  200.59, 80],
        "Ho" : ["Holmium",  164.93032, 67],
        "I" : ["Iodine",    126.90447, 53],
        "In" : ["Indium",   114.818, 49],
        "Ir" : ["Iridium",  192.217, 77],
        "K" : ["Potassium", 39.0983, 19],
        "Kr" : ["Krypton",  83.798, 36],
        "La" : ["Lanthanum", 138.90547, 57],
        "Li" : ["Lithium",  6.941, 3],
        "Lu" : ["Lutetium", 174.9668, 71],
        "Mg" : ["Magnesium",    24.305, 12],
        "Mn" : ["Manganese",    54.938045, 25],
        "Mo" : ["Molybdenum",   95.96, 42],
        "N" : ["Nitrogen",  14.0067, 7],
        "Na" : ["Sodium",   22.98976928, 11],
        "Nb" : ["Niobium",  92.90638, 41],
        "Nd" : ["Neodymium",    144.242, 60],
        "Ne" : ["Neon", 20.1797, 10],
        "Ni" : ["Nickel",   58.6934, 28],
        "Np" : ["Neptunium",    237, 93],
        "O" : ["Oxygen",    15.9994, 8],
        "Os" : ["Osmium",   190.23, 76],
        "P" : ["Phosphorus",    30.973762, 15],
        "Pa" : ["Protactinium", 231.03588, 91],
        "Pb" : ["Lead", 207.2, 82],
        "Pd" : ["Palladium",    106.42, 46],
        "Pm" : ["Promethium",   145, 61],
        "Po" : ["Polonium", 209, 84],
        "Pr" : ["Praseodymium", 140.90765, 59],
        "Pt" : ["Platinum", 195.084, 78],
        "Pu" : ["Plutonium",    244, 94],
        "Ra" : ["Radium",   226, 88],
        "Rb" : ["Rubidium", 85.4678, 37],
        "Re" : ["Rhenium",  186.207, 75],
        "Rh" : ["Rhodium",  102.9055, 45],
        "Rn" : ["Radon",    222, 86],
        "Ru" : ["Ruthenium",    101.07, 44],
        "S" : ["Sulfur",    32.065, 16],
        "Sb" : ["Antimony", 121.76, 51],
        "Sc" : ["Scandium", 44.955912, 21],
        "Se" : ["Selenium", 78.96, 34],
        "Si" : ["Silicon",  28.0855, 14],
        "Sm" : ["Samarium", 150.36, 62],
        "Sn" : ["Tin",  118.71, 50],
        "Sr" : ["Strontium",    87.62, 38],
        "Ta" : ["Tantalum", 180.94788, 73],
        "Tb" : ["Terbium",  158.92535, 65],
        "Tc" : ["Technetium",   98, 43],
        "Te" : ["Tellurium",    127.6, 52],
        "Th" : ["Thorium",  232.03806, 90],
        "Ti" : ["Titanium", 47.867, 22],
        "Tl" : ["Thallium", 204.3833, 81],
        "Tm" : ["Thulium",  168.93421, 69],
        "U" : ["Uranium",  238.02891, 92],
        "V" : ["Vanadium", 50.9415, 23],
        "W" : ["Tungsten", 183.84, 74],
        "Xe" : ["Xenon",    131.293, 54],
        "Yb" : ["Ytterbium", 173.045, 70],
        "Y" : ["Yttrium",   88.90595, 39],
        "Zn" : ["Zinc", 65.38, 30],
        "Zr" : ["Zirconium", 91.224, 40]
    }

    return periodic_table_dict

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    
    total_molar_mass = 0

    for inner_list in symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        symbol = inner_list[SYMBOL_INDEX]
        atoms_quantity = inner_list[QUANTITY_INDEX]
        
        # Get the atomic mass for the symbol from the dictionary.
        element = periodic_table_dict[symbol]
        atomic_mass = element[ATOMIC_MASS_INDEX]

        # Multiply the atomic mass by the quantity.
        product = atomic_mass * atoms_quantity

        # Add the product into the total molar mass.
        total_molar_mass += product

    # Return the total molar mass.
    return total_molar_mass

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".

    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    compound_name = "unknown compound"

    if formula in known_molecules_dict:
        compound_name = known_molecules_dict[formula]

    return compound_name

def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total number of protons of all
        the elements in symbol_quantity_list.
    """
    total_number_protons = 0

    for inner_list in symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        symbol = inner_list[SYMBOL_INDEX]
        atoms_quantity = inner_list[QUANTITY_INDEX]
        
        # Get the atomic number for the symbol from the dictionary.
        element = periodic_table_dict[symbol]
        atomic_number = element[ATOMIC_NUMBER_INDEX]

        # Multiply the atomic number by the quantity.
        product = atomic_number * atoms_quantity

        # Add the product into the total of protons.
        total_number_protons += product

    # Return the total molar mass.
    return total_number_protons

def main():

    print_elements("header")
    
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }

    # Get a chemical formula for a molecule from the user.
    molecular_formula = input("Enter the molecular formula of the sample: ") #Ex.: C6H6
    
    # Get the mass of a chemical sample in grams from the user.
    sample_mass = float(input("Enter the mass in grams of the sample: ")) #Ex.: 25.04

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table = make_periodic_table()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(molecular_formula, periodic_table)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Compute the number of moles in the sample.
    moles = sample_mass / molar_mass
    
    # Call get_formula_name function and
    # get the compound name
    compound_name = get_formula_name(molecular_formula, known_molecules_dict)
    print(f"\nThis sample of {compound_name.capitalize()} has:")

    # Print the molar mass.
    print(f"- {molar_mass} grams/mole")

    # Print the number of moles.
    print(f"- {moles:.5f} moles")

    # Call the sum_protons function
    # and print the number of protons
    total_protons = sum_protons(symbol_quantity_list, make_periodic_table_with_protons())
    print(f"- {total_protons} protons")

    print_elements("footer")

# If this file was executed like this: > python chemistry.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()