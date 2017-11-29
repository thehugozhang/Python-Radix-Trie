#   Written in Python 3.6.2 in IDLE
#   Platform: macOS Sierra
#
#   This file is the runner class of the radix.py file
#   Problem 6 MIT Primes
#
#   The test data I used for this class was:
#
#   DNA1 = "GTCTCTAAGA"
#   DNA2 = "GTGAAGCGCA"
#   DNA3 = "GACCTGGACG"
#   DNA4 = "GACTACACCA"
#   DNA5 = "ACTGTACTGT"
#   DNA6 = "TGTGAACCCG"
#   DNA7 = "GACCCAGTTT"
#   DNA8 = "GGACGATTCA"
#   DNA9 = "CGGATCGGAT"
#
#   However, I successfully tested the code with over 50 different
#   randomly generated DNA strands to verify it's functionality.
#
#   Since I started my application a little late, I did not have time
#   implement a proper UI so please bear with the unpolished text-based UI.
#
#   INSTRUCTIONS FOR RUNNING
#
#   To see the functionality of this class, run the file and follow the instructions in the shell.
#
#   If you choose option 1 or 2:
#   The code will first add the strings that you chose to the radix tree
#   Then it will print the entire tree
#   Then it will print the number of nodes in the tree
#   Then it will print the total number of strings in the tree
#   Then it will print the strings in alphabetical order
#   Then it will print all the nodes and their corresponding prefixes
#   Then it will search the tree for the strings and verify they are apart of the tree
#   Then it remove strings from the tree
#   Then it will reprint the new updated tree, updated number of nodes, and updated number of strings.
#
#   Choose option 3 to enter your own DNA strands and test each function seperately.
#
#   Cheers.

from Radix import *
from random import choice
import os

def random():
    """Add five randomly generated DNA strands to the radix tree"""

    print("This is a demonstration of the functionality of radix.py using randomly generated DNA strands.")
    print("")
    
    radix = Radix()
    
    randDNA1 = generateRandomDNASequence(10)
    randDNA2 = generateRandomDNASequence(10)
    randDNA3 = generateRandomDNASequence(10)
    randDNA4 = generateRandomDNASequence(10)
    randDNA5 = generateRandomDNASequence(10)
    
    print(randDNA5)
    print(randDNA4)
    print(randDNA3)
    print(randDNA2)
    print(randDNA1)

    radix.addString( randDNA1 , radix.root , randDNA1)
    radix.addString( randDNA2 , radix.root , randDNA2)
    radix.addString( randDNA3 , radix.root , randDNA3)
    radix.addString( randDNA4 , radix.root , randDNA4)
    radix.addString( randDNA5 , radix.root , randDNA5)

    print("")
    
    radix.printTree()
    
    print("")
    
    radix.listWordsAlphabetically()
    
    print("")
    
    print("All the nodes in the tree are printed below with their corresponding prefix.")
    radix.listAllNodes(radix.root, "")
    
    print("")
    
    radix.search(randDNA1 , radix.root , "" , randDNA1)
    radix.search(randDNA2 , radix.root , "" , randDNA2)
    radix.search(randDNA3 , radix.root , "" , randDNA3)
    radix.search(randDNA4 , radix.root , "" , randDNA4)
    radix.search(randDNA5 , radix.root , "" , randDNA5)
    
    print("")
    
    radix.delete(randDNA1, radix.root , randDNA1, "", radix.root, False)
    radix.delete(randDNA2, radix.root , randDNA2, "", radix.root, False)
    
    print("")
    
    radix.printAll()
    
def demo():
    """Add the test data to the radix tree"""
    
    print("This is a demonstration of the functionality of radix.py using the test data in the header.")
    print("")
    
    radix = Radix()
    
    DNA1 = "GTCTCTAAGA"
    DNA2 = "GTGAAGCGCA"
    DNA3 = "GACCTGGACG"
    DNA4 = "GACTACACCA"
    DNA5 = "ACTGTACTGT"
    DNA6 = "TGTGAACCCG"
    DNA7 = "GACCCAGTTT"
    DNA8 = "GGACGATTCA"
    DNA9 = "CGGATCGGAT"
    
    radix.addString( DNA1 , radix.root , DNA1)
    radix.addString( DNA2 , radix.root , DNA2)
    radix.addString( DNA3 , radix.root , DNA3)
    radix.addString( DNA4 , radix.root , DNA4)
    radix.addString( DNA5 , radix.root , DNA5)
    radix.addString( DNA6 , radix.root , DNA6)
    radix.addString( DNA7 , radix.root , DNA7)
    radix.addString( DNA8 , radix.root , DNA8)
    radix.addString( DNA9 , radix.root , DNA9)

    radix.printTree()
    
    print("")
    
    radix.listWordsAlphabetically()
    
    print("")
    
    print("All the nodes in the tree are printed below with their corresponding prefix.")
    radix.listAllNodes(radix.root, "")
    
    print("")
    
    radix.search(DNA1 , radix.root , "" , DNA1)
    radix.search(DNA2 , radix.root , "" , DNA2)
    radix.search(DNA3 , radix.root , "" , DNA3)
    radix.search(DNA4 , radix.root , "" , DNA4)
    radix.search(DNA5 , radix.root , "" , DNA5)
    radix.search(DNA6 , radix.root , "" , DNA6)
    radix.search(DNA7 , radix.root , "" , DNA7)
    radix.search(DNA8 , radix.root , "" , DNA8)
    radix.search(DNA9 , radix.root , "" , DNA9)
    radix.search("GTCTC" , radix.root , "" , "GTCTC")
    
    print("")
    
    radix.delete(DNA1, radix.root , DNA1, "", radix.root, False)
    radix.delete(DNA2, radix.root , DNA2, "", radix.root, False)
    
    print("")
    
    radix.printAll()


def generateRandomDNASequence(length):
    """Generate random DNA strand of length given"""
    
    DNA = "" 
    for count in range(length):
        DNA += choice("ACGT")
    return DNA

if __name__ == '__main__':
    while True:
        print("Welcome to my radix tree implementation!")
        print("")
        print("1. Demonstration of functionality of radix tree using test data.")
        print("2. Demonstration of functionality of radix tree using randomly generated.")
        print("3. Demonstration of functionality of radix tree using user-entered data.")
        print("")
        option = input("Please enter one of the option numbers below and hit enter to continue: ")

        if option == "1":
            
            print("")
            demo()
            
        elif option  == "2":
            
            print("")
            random()
            
        elif option == "3":
            radix = Radix()
            
            print("")
            numberOfStrings = int(input("How many DNA strings would you like to add? "))
            for x in range(numberOfStrings):
                print("")
                DNA = input("Enter the DNA strand you would like to add to the tree: ")
                radix.addString(DNA.upper(), radix.root, DNA.upper())
                
            print("")
            print("Now that you have added the strings to the tree, what would you like to do?")
                
            while True:
                
                print("")
                print("1. Add another string to the tree.")
                print("2. Delete a string from the tree.")
                print("3. Search the tree for a string.")
                print("4. Print the total amount of strings.")
                print("5. Print the total amount of nodes.")
                print("6. Print all the strings in alphabetical order.")
                print("7. Print all the nodes in the tree and their corresponding prefixes.")
                print("8. Print the entire tree.")
                print("9. Exit")
                print("")
                option = input("Please enter one of the option numbers below and hit enter to continue: ")
                print("")
                
                if option == "1":
                    DNA = input("Enter the DNA strand you would like to add to the tree: ")
                    radix.addString(DNA.upper(), radix.root, DNA.upper())
                elif option == "2":
                    DNA = input("Enter the DNA strand you would like to delete from the tree: ")
                    print("")
                    radix.delete(DNA.upper(), radix.root, DNA.upper(), "", radix.root, False)
                elif option == "3":
                    DNA = input("Enter the DNA strand you would like to search for in the tree: ")
                    print("")
                    radix.search(DNA.upper() , radix.root , "" , DNA.upper())
                elif option == "4":
                    radix.printStringCount()
                elif option == "5":
                    radix.printNodeCount()
                elif option == "6":
                    radix.listWordsAlphabetically()
                elif option == "7":
                    radix.listAllNodes(radix.root, "")
                elif option == "8":
                    radix.printTree()
                elif option == "9":
                    break
                else:
                    print("Sorry, the option you chose is invalid.")
                
                                  
        else:
            
            print("")
            print("Sorry, the option you chose is invalid. Please enter either 1, 2, or 3.")

        print("")
        
        again = input("Would you like to run it again? Y or N? ")
        
        if again.upper() == "Y":
            print("")
            continue
        elif again.upper() == "N":
            print("")
            print("I hope you enjoyed my radix tree implementation. Cheers!")
            break
        else:
            print("")
            print("Sorry, the option you chose is invalid. I hope you enjoyed my radix tree implementation. Cheers!")
            break
        

