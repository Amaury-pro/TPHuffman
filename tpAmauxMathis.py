class Node:
    def __init__(self, l=None, r=None, i=0, p=0):
        self.left = l
        self.right = r
        self.prob = p
        self.key = i


# Sort following the buble sort
def sort(proba):
    for i in range(len(proba)-1, 0, -1):
        j = i
        while proba[j] > proba[j-1]:
            proba[j-1], proba[j] = proba[j], proba[j-1]
            j += 1
    return proba

def huffman_sort(proba):
    proba = sort(proba)
    resultats = [proba.copy()]
    tree = Node(p=1)
    print(proba)
    while len(proba) > 1:
        proba = sort(proba)
        proba[-2] = proba[-1] + proba[-2]
        proba.pop()
        print(proba)
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