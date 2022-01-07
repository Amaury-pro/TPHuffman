import numpy as np
import matplotlib.pyplot as plt
import math as m
import PIL as pil

class Node:
    def __init__(self, l=None, r=None, i=0, p=0):
        self.left = l
        self.right = r
        self.prob = p
        self.key = i

def huffman_sort(proba):
    proba = sorted(proba,reverse = True)
    resultats = [proba.copy()]
    tree = Node(p=1)
    while len(proba) > 1:
        proba = sorted(proba,reverse = True)
        proba[-2] = proba[-1] + proba[-2]
        proba.pop()
        resultats.append(proba.copy())
    currentNode = tree
    for i in range(len(resultats)-2, -1,-1):
        currentNode.right = Node(p=resultats[i][-1])
        currentNode.left = Node(p=resultats[i][-2])
        currentNode = currentNode.right
    return tree



def is_leaf(n):
    return n.right == None and n.left == None


def is_node(n):
    return n.right or n.left


L = []
i = 0


def get_cwd(tree):
    L = []
    create_liste_cwd(tree, L, tree, "")
    return L

def huffman_code(proba):
    tree = huffman_sort(proba)
    cwd = get_cwd(tree)
    somme = 0
    for w in cwd:
        somme += len(w)
    
    return (somme/len(cwd),cwd)

def create_liste_cwd(tree, L, node, s):
    if node == None:  # cas d'arbre null
        return None
    elif is_leaf(node):  # cas feuille
        return L

    if not (node.left == None):  # cas il a un enfant à gauche
        if is_leaf(node.left):  # soit c'est une feuille
            L.append(s+'0')
        else :  # soit c'est un noeud
            create_liste_cwd(tree, L, node.left, s+'0')

    if not (node.right == None):  # cas il a un enfant à droite
        if is_leaf(node.right):  # soit c'est une feuille
            L.append(s+'1')
        else:  # soit c'est un noeud
            create_liste_cwd(tree, L, node.right, s+'1')

def huffman_tree2(ListCwd):
    if len(ListCwd) == 0:
        return None
    tree = Node()
    create_tree(ListCwd, tree)
    return tree


def create_tree(ListCwd, tree):
    for s in ListCwd :
        node = tree
        for c in s :
            if c == '0': # cas on va à gauche
                if node.left == None: # cas le noeud suivant existe pas
                    node.left = Node()
                    node.left.key = 0
                node = node.left
            elif c == '1': # cas on va à droite
                if node.right == None: # cas le noeud suivant existe déjà
                    node.right = Node()
                    node.right.key = 1
                node = node.right


##Tree tests##
arbre_tree = Node(l=Node(),r=Node(l=Node(),r=Node(l=Node(),r=Node())))
arbre_P = Node(l=Node(l=Node(r=Node()), r=Node()),r=Node(r=Node(l=Node())))
arbre_empty = None
arbre_empty_2 = Node()
####

L = get_cwd(arbre_P)
print(L)
tree = huffman_tree2(L)
L = get_cwd(tree)
print(L)

def cwd_detect(tree,seq):
    list_dec = []
    i = 0
    j = 0
    racine = tree
    compteur = 0
    for k in seq:
        k = int(k)
        
        if (k == 0):
            if (tree.left != None):
                i = i+1
                tree = tree.left
            else:
                tree = racine
                list_dec.append(seq[j:i])
                j = i
                i = i+1
        elif (k == 1):
            if(tree.right != None):
                i = i+1
                tree = tree.right
            else:
                tree = racine
                list_dec.append(seq[j:i])
                j = i
                i = i+1      
        compteur += 1
    return list_dec

def get_proba_and_symb(seq):
    dict = {}
    for n in seq:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get, reverse=True)
    
    for w in sorted_keys:
        sorted_dict[w] = dict[w]
    proba = []
    symb = []
    for k,v in sorted_dict.items():
        proba.append(v/len(seq))
        symb.append(k)
    return (proba,symb)

def get_key_char(symb, char):
    i = 0
    for k in symb:
        if k == char:
            return i
        i += 1

def get_seqencoded_from_seq(seq, cwd, symb):
    encoded_seq = ""
    for c in seq:
        i = get_key_char(symb,c)
        encoded_seq += str(cwd[i])
    return encoded_seq

def huffman_decode(seq, symb, cwd):
    i = 0
    tree = huffman_tree2(cwd)
    
    list_i = cwd_detect(tree, seq)
    while i < len(list_i):
        c = symb[get_key_char(seq,list_i[i])]
        print(c)
        i = i+1
        return 0


def test_hufffman_algo(seq):
    proba, symb = get_proba_and_symb(seq)
    cwd = huffman_code(proba)[1]
    print("Le message ' "+seq+" 'une fois encodé donne : \n")
    encoded_message = get_seqencoded_from_seq(seq,cwd,symb)
    print(encoded_message)
    print(cwd)
    print(symb)

test_hufffman_algo("Bonjour")


def calc_entropie(histo):
    s=0
    n = len(histo)
    for i in range(0,n):
        if(histo[i] > 0):
            s += histo[i]*m.log10(histo[i])
    return -s
