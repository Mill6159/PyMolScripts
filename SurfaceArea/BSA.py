# Imports

import pymol
import numpy as np

def BSA( dom1, dom2 ):
    '''
DESCRIPTION

    YYY 

    dom1: The first domain
    dom2: The second domain

    Simply calculates the buried surface area as:

    (The accessible surface area of domain 1 + the accessible surface area of domain 2) - 
    (the accessible surface area of domain 1 and 2, if treating them like a single domain)

    Where I'm taking the absolute value BUT it should always be positive.
    '''

    d1 = cmd.select ('dom1',dom1)
    d2 = cmd.select ('dom2',dom2)

    A_ASA = cmd.get_area (dom1)
    print('Surface area of the first domain (Å^2):',A_ASA)
    B_ASA = cmd.get_area (dom2)
    print('Surface area of the second domain (Å^2):',B_ASA)

    dom12 = cmd.select ('dom12', 'dom1:dom2')

    AB_ASA = cmd.get_area ('dom12')
    print('Surface area of the two domains combined (Å^2):',AB_ASA)

    BSA = np.absolute((A_ASA + B_ASA) - AB_ASA)

    print('The buried surface area between the two domains is (Å^2):',BSA)

    cmd.delete('dom1')
    cmd.delete('dom2')
    cmd.delete('dom12')

    return BSA

cmd.extend( "BSA", BSA );