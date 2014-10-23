#!/usr/bin/env python
import copy

import os, sys, math, random, time

from particles import Particle
from particles import ParticleContainer

from bonds import Bond
from bonds import BondContainer

from structureContainer import StructureContainer

def main():
    
    """
    This test shows how the setPtclPos method works to externally set all particle
    positions from a list
    """
    print "************************************************************************************"
    print " This test shows how the setPtclPos method works to externally set all particle "
    print " positions from a list"
    print "************************************************************************************ \n"

    p1 = Particle( [0.2, 1.3,  33.0], "Si", 2.0, 1.23)
    p2 = Particle( [5.0, 2.3, -22.1], "C",  1.0, 2.34)
    p3 = Particle( [5.0, 2.3, -20.1], "C",  1.0, 2.34)
    p4 = Particle( [0.0, 2.3, -20.1], "C",  1.0, 2.34)

    b1 = Bond( 1, 2, 1.233, "hooke")
    b2 = Bond( 2, 3, 0.500, "hooke")
    b3 = Bond( 3, 4, 2.301, "hooke")
    b4 = Bond( 1, 3, 0.828, "hooke")

    atoms1 = ParticleContainer()
    atoms1.put(p1)
    atoms1.put(p2)
    atoms1.put(p3)
    atoms1.put(p4)

    bonds = BondContainer()
    bonds.put(b1)
    bonds.put(b2)
    bonds.put(b3)
    bonds.put(b4)

    del p1, p2, p3, p4, b1, b2, b3, b4
    polymer1 = StructureContainer(atoms1, bonds)
    del atoms1, bonds
    polymer1.setBoxLengths([ [-3.0, 100], [-5, 23.0], [34.3, 100.1] ])

    print "Initial state of structure before reset ", polymer1

    newPtclPos = [
     [1, 0.111, 0.222, 0.333],
     [2, 0.222, 0.333, 0.444],
     [4, 0.444, 0.555, 0.666]
    ]

    print "new positions = ", newPtclPos

    polymer1.setPtclPositions(newPtclPos)

    ptclPosList = polymer1.getPtclPositions()

    print "new positions from structure = ", ptclPosList
    print " "
    print "After position reset/get ", polymer1

if __name__ == '__main__':
    main()
