#   Written in Python 3.6.2 in IDLE
#   Platform: macOS Sierra
#
#   This file contains the implementation of a radix tree
#   Problem 6 MIT Primes
#
#   To see the functionality of this class, run the main.py file.
#   All the instructions and test data are in the Main.py file.
#
#   This class contains all the code behind the radix tree.

from collections import defaultdict

class Radix():
    def __init__(self):
        self.root = defaultdict()
        self.allStrings = []
        self.totalNodes = 0
        
    def addString(self, string, radix, entireString):
        """Adds words to tree"""
        current = radix
        newNode = ""
        traverseString = string
        wordsToBeSplit = []
        flag = 0
        entireString = entireString

        if entireString not in self.allStrings:
            self.allStrings.append(entireString)
        
        if len(current) == 0:
            #Add first DNA sequence
            current[string] = "_end"
        else:
            for k, v in current.copy().items():
                #comparing first two strings until gets initial newNode value
                if k[0] == string[0]:
                    if newNode == "":
                        for char in k:
                            #If reached end of string before end of key, must already be prefix of key and no need for action
                            if traverseString == "":
                                break
                            #else reached end of key before end of string meaning must traverse to children
                            for letter in traverseString:
                                if letter == char:
                                    newNode = newNode + char
                                    traverseString = traverseString[1:]
                                    flag = 0
                                    if k not in wordsToBeSplit:
                                        wordsToBeSplit.append(k)
                                    break
                                else:
                                    traverseString = traverseString[1:]
                                    flag = 1
                                    break
                            if flag == 1:
                                break
                    #compares newNode value to prefixes of remaining strings
                    else:
                        nextNode = ""
                        finalNode = ""
                        traverseString = string
                        flag = 0
                        #gets longest prefix between next to strings
                        for char in k:
                            for letter in traverseString:
                                if letter == char:
                                    nextNode = nextNode + char
                                    traverseString = traverseString[1:]
                                    flag = 0
                                    if k not in wordsToBeSplit:
                                        wordsToBeSplit.append(k)
                                    break
                                else:
                                    traverseString = traverseString[1:]
                                    flag = 1
                                    break
                            if flag == 1:
                                break
                        #compares current prefix to new prefix and cuts it for both
                        for char in newNode:
                            for letter in nextNode:
                                if char == letter:
                                    finalNode = finalNode + char
                                    nextNode = nextNode[1:]
                                    break
                                else:
                                    nextNode = nextNode[1:]
                                    break
                        newNode = finalNode
            if newNode != "":
                try:
                    #If key has prefix already, add to children dict directly and compare the children for matches
                    if type(current[newNode]) == dict:
                        self.addString( string[len(newNode):], current[newNode], entireString)
                #if prefix does not exist in dictionary yet                       
                except KeyError:
                    #Adds string minus prefix to the dictionary
                    newDic = {string[len(newNode):] : "_end"}
                    for newKey in wordsToBeSplit:
                        #Adds prefix with words ending as new key to child dictionary
                        newDic[newKey[len(newNode):]] = current[newKey]
                        #get rid of key with _end and change to new dic
                        current.pop(newKey, None)
                    current.setdefault(newNode, newDic)
                except:
                    print("I got another exception, but I should re-raise.")
                    raise                
            #if no prefix add entire node 
            else:
                current.setdefault(string, "_end")

    def delete(self, string, radix, entireWord, lastKey, lastDic, isVerified):
        """Removes string from tree by removing last child node of string"""
        current = radix
        lastDic = lastDic
        matches = False
        entireWord = entireWord
        lastKey = lastKey
        verified = isVerified
        
        if string in self.allStrings:
            self.allStrings.remove(string)
            verified = True

        if verified:          
            #Will only remove strings that were added by the user, not partial strings
            for k, v in current.copy().items():
                for keyCharacter, stringCharacter in zip(k, string):
                    #compares strings character by character
                    if keyCharacter == stringCharacter:
                        matches = True
                    else:
                        matches = False
                        break
                if matches:
                    #Continue traversal with recursion
                    if type(v) == dict:
                        self.delete(string[len(k):], v, entireWord, k, current, verified)
                        return
                    elif v == '_end':
                    #If reaches last child node, remove it
                        current.pop(k, None)
                        #If no more child nodes, delete key
                        if not bool(lastDic.get(lastKey)):
                            #dictionary is empty
                            lastDic.pop(lastKey, None)
                        print("The string '" + entireWord + "' has been removed from the radix tree.")
        else:
            print("Please only try and delete strings added by the user.")
                        
    def search(self, string, radix, total, entireWord):
        """Returns True if the word is in the trie."""
        current = radix
        matches = False
        totalWord = total
        #saves string and allows string to be directly manipulated
        entireWord = entireWord
        
        for k, v in current.items():
            for keyCharacter, stringCharacter in zip(k, string):
                #compares strings character by character
                if keyCharacter == stringCharacter:
                    totalWord = totalWord + keyCharacter
                    matches = True
                else:
                    matches = False
                    break
            if matches:
                
                if entireWord == totalWord:
                    print("The string '" + totalWord + "' exists in the radix tree.")
                    return True
                else:
                    #Continue traversal with recursion
                    if type(v) == dict:
                        self.search(string[len(k):], v, totalWord, entireWord)
                        return
                    elif v == "_end":
                    #If reaches end of tree before end of word, word is not included in tree
                        print("The string '" + entireWord + "' does NOT exist in the radix tree.")
                        return False
        #Word does not match any keys -> takes a different path and is not included in tree
        print("The string '" + entireWord + "' does NOT exist in the radix tree.")
        return False

    def totalStringCount(self):
        """Returns total amount of user added strings"""
        return len(self.allStrings)

    def totalNodeCount(self, radix):
        """Returns total amount of nodes"""
        current = radix
        for k, v in current.items():
            self.totalNodes += 1
            if type(v) == dict:
                self.totalNodeCount(v)
        return self.totalNodes

    def listWordsAlphabetically(self):
        """Lists all user added words in alphabetical order"""
        alphabetical = sorted(self.allStrings, key = str.lower)
        print("The user-added strings in alphabetical order are:")
        for string in alphabetical:
            print(string)

    def listAllNodes(self, radix, lastKey):
        """List all nodes and the prefix they correspond to"""
        current = radix
        for k, v in current.items():
            if type(v) == str:
                if lastKey == "":
                    print("Node: " + k + "; Prefix: None")
                else:
                    print("Node: " + k + "; Prefix: " + lastKey)
            elif type(v) == dict:
                if lastKey == "":
                    print("Node: " + k + "; Prefix: None")
                else:
                    print("Node: " + k + "; Prefix: " + lastKey)
                self.listAllNodes(v, k)
                
    def printTree(self):
        """Prints the entire dictionary"""
        print("The radix tree is: " + str(dict(self.root)) + ".")

    def printNodeCount(self):
        """Prints the node count"""
        self.totalNodes = 0
        print("There are a total of " + str(self.totalNodeCount(self.root)) + " node(s) in the radix tree.")

    def printStringCount(self):
        """Prints the string count"""
        print("There are a total of " + str(self.totalStringCount()) + " string(s) in the radix tree. However, this only includes all the strings added by the user. It does not account for all the different possible prefixes.")

    def printAll(self):
        """Prints everything"""
        self.totalNodes = 0
        
        print("The radix tree is: " + str(dict(self.root)) + ".")
        print("")
        print("There are a total of " + str(self.totalNodeCount(self.root)) + " node(s) in the radix tree.")
        print("")
        print("There are a total of " + str(self.totalStringCount()) + " string(s) in the radix tree. However, this only includes all the strings added by the user. It does not account for all the different possible prefixes.")

