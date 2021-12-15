class Node:
    def __init__(self, l=None, r=None, i=0, p=0):
        self.left = l
        self.right = r
        self.prob = p
        self.key = i


# Sort following the buble sort
def sort(proba):
    # Go throw every cases from the last one to the second one
    for i in range(len(proba)-1, 0, -1):
        for j in range(i):  # Go thrwo every cases from the first one to the one before proba[]
            if proba[j] > proba[j+1]:  # Sort pairs
                # exchange if needed
                proba[j], proba[j+1] = proba[j+1], proba[j]

    for i in proba:
        if min > proba[i]:
            min = proba[i]
    return proba, min


"""
def huffman_sort(proba):
    proba = sort(proba)
    resultats = [proba]
    tree = Node(p=1)
    i = 0
    while len(proba) > 1:
        i += 1
        proba = sort(proba)
        proba[-2] = proba[-1] + proba[-2]
        proba.pop()
        resultats[i] = proba

    for i in range(len(tableau), 0, -1):
        tree.right = Node(p=tableau[i][-1])
        tree.left = Node(p=tableau[i][-2])

    return tree
"""


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
                node = node.left
            elif c == '1': # cas on va à droite
                if node.right == None: # cas le noeud suivant existe déjà
                    node.right = Node()
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