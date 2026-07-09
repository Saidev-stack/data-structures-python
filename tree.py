# Trees' functions block
def create_binary_tree():
    '''
    Create a binary tree

    Returns:
    --------
    list
        A list representing a binary tree.
    '''

    root = input("Enter the Root value : ")    
    tree = [root, None, None]

    left = input(f"Does {root} have a left child? yes/non => ").lower()
    if left == 'yes':
        tree[1] = create_binary_tree() #adding a left or right child is adding a new Tree, that's why we recall our function
    
    right = input(f"Does {root} have a right child? yes/non => ").lower()
    if right == 'yes':
        tree[-1] = create_binary_tree()
    
    return tree

def _create_binary_search_tree(root, bourne_inf, bourne_sup):
    """
    Internal fonction helper used by create_binary_search_tree().
    """

    tree = [root, None, None]

    left = input(f"Does {root} have a left child? yes/non => ").lower()

    if left == 'yes':
        lc_root = int(input("Enter its value : "))
        rep = 'yes'

        while (lc_root >= root or (bourne_inf >= lc_root if bourne_inf is not None else False)) and rep == 'yes':
            rep = input("Invalide input, do you want to try again? yes/non => " ).lower()
            
            if rep == 'yes':
                lc_root = int(input("Enter its value : "))
        
        if lc_root < tree[0]:
            left_child = _create_binary_search_tree(lc_root, bourne_inf, root)
            tree[1] = left_child
    
    right = input(f"Does {root} have a right child? yes/non => ").lower()
    
    if right == 'yes':
        rc_root = int(input("Entre its value : "))
        rep = 'yes'

        while (rc_root <= root or (bourne_sup <= rc_root if bourne_sup is not None else False)) and rep == 'yes':
            rep = input("Invalide input, do you want to try again? yes/non => " ).lower()
            
            if rep == 'yes':
                rc_root = int(input("Enter its value : "))
        
        if rc_root > tree[0]:
            right_child = _create_binary_search_tree(rc_root, root, bourne_sup)
            tree[-1] = right_child
    
    return tree

def _display_binary_tree(tree, level):
    """
    Internal fonction helper used by display_binary_tree().
    """

    if tree is None:
        return ['None']
    elif tree[1:] == [None, None]:
        return [str(tree[0])]
    else:
        list1 = [str(tree[0])]
        list1 += ['|' + (level - 1) * "    "] + ['|-----' + e if i == 0 else '|      ' + e for i, e in enumerate(_display_binary_tree(tree[1], level + 1))]
        list1 += ['|' + (level - 1) * "    "] + ['|_____' + e if i == 0 else '      ' + e for i, e in enumerate(_display_binary_tree(tree[2], level + 1))]
        return list1

def display_binary_tree(tree):
    '''
    Display the binary tree

    Parameters:
    -----------
    tree : list
        The binary tree
    
    Returns:
        This function displays the binary tree in the console.
    '''

    string = _display_binary_tree(tree, 1)
    print("\n".join(string))

def tree_tool(root, nb_children):
    """
    Internal fonction helper used by trees' functions.
    """

    return [root] + [None] * nb_children

def _create_tree(nb_children):
    """
    Internal fonction helper used by create_tree().
    """

    root = input("Enter the Root value : ")    
    tree = tree_tool(root, nb_children)

    for i in range(nb_children):
        child = input(f"Does {root} have a number {i + 1} child? yes/non => ").lower()
        if child == 'yes':
            tree[i + 1] = _create_tree(nb_children)
    
    return tree


def _display_tree(tree, level):
    """
    Internal recursive helper used by display_tree().
    """

    if tree is None:
        return ['None']
    elif tree[1:] == [None, None]:# tree_tool(tree[0], len(tree))
        return [str(tree[0])]
    else:
        list1 = [str(tree[0])]

        for j in range(1, len(tree) - 1):
            list1 += ['|' + (level - 1) * "    "] + ['|-----' + e if i == 0 else '|      ' + e for i, e in enumerate(_display_tree(tree[j], level + 1))]
        
        list1 += ['|' + (level - 1) * "    "] + ['|_____' + e if i == 0 else '      ' + e for i, e in enumerate(_display_tree(tree[-1], level + 1))]
        
        return list1
    
def display_tree(tree):
    '''
    Display the tree

    Parameters:
    -----------
    tree : list
        The tree
    
    Returns:
        This function displays the tree in the console.
    '''

    string = _display_tree(tree, 1)
    print("\n".join(string))
  
def _search_in_binary_search_tree(tree, node):
    """
    Internal fonction helper used by search_in_binary_search_tree().
    """

    if tree is None:
        return False
    else:
        if node == tree[0]:
            return True
        elif node < tree[0]:
            return _search_in_binary_search_tree(tree[1], node)
        else:
            return _search_in_binary_search_tree(tree[2], node)

def search_in_binary_search_tree(tree):
    """
    Search for a node in the tree.

    Parameters:
    -----------
    ll : list
        The binary search tree.

    Returns:
    --------
    bool
        True if the node is found, otherwise False.
    """

    node = int(input("Enter your node : "))
    
    if _search_in_binary_search_tree(tree, node):
        print(node, "is in the tree.")
    else:
        print(node, "isn't in the tree.")
        
def _search_in_tree(tree, node):
    """
    Internal fonction helper used by search_in_tree().
    """

    if tree is None:
        return False
    else:
        if node == tree[0]:
            return True
        else:
            for i in range(1, len(tree)):
                if _search_in_tree(tree[i], node):
                    return True
    return False

def search_in_tree(tree):
    """
    Search for a node in the tree.

    Parameters:
    -----------
    ll : list
        The tree.

    Returns:
    --------
    bool
        True if the node is found, otherwise False.
    """

    node = input("Enter your node : ")

    if _search_in_tree(tree, node):
        print(node, "is in the tree.")
    else:
        print(node, "isn't in the tree.")

def _count_tree_nodes(tree):
    """
    Internal fonction helper used by count_tree_nodes().
    """

    nb_nodes = 0

    if tree is None:
        return nb_nodes
    else:
        nb_nodes += 1
        for i in range(1, len(tree)):
            nb_nodes += _count_tree_nodes(tree[i])

    return nb_nodes

def count_tree_nodes(tree):
    '''
    Count the nodes of the tree.

    Parameteres:
    ------------
    tree : list
        The tree
    
    Returns:
    --------
    int
        The number of nodes in the tree.
    '''

    print("The nombre of node in the tree is :", _count_tree_nodes(tree))

def _height_tree(tree):
    """
    Internal fonction helper used by height_tree().
    """

    height = 0
    heights = []

    if tree is not None:
        if tree == tree_tool(tree[0], len(tree[1:])):
            return height + 1
        else:
            height += 1           
            for i in range(1, len(tree)):
                heights.append(_height_tree(tree[i]))
            height += max(heights)
            return height
    else:
        return height

def height_tree(tree):
    '''
    Find the height of the tree.

    Parameters:
    -----------
    tree : list
        The tree

    Returns:
    int
        The height of the tree
    '''

    print("The height of the tree is :", _height_tree(tree))

def _count_feuille(tree):
    """
    Internal fonction helper used by count_feuille().
    """

    feuille = 0
    feuilles = 0

    if tree is not None:
        if all(e is None for e in tree[1:]):
            return feuille + 1
        else:
            #feuille += 1
            for i in range(1, len(tree)):
                feuilles += _count_feuille(tree[i])
            return feuille + feuilles
    else:
        return feuille

def count_feuille(tree):
    '''
    Count leaves of the tree.

    Parameters:
    -----------
    tree : list
        The tree

    Returns:
    --------
    int
        The numbre of tree leaves'
    '''

    print("The nombre of leaves in the tree is :", _count_feuille(tree))

def _check_BST(tree, borne_inf, borne_sup):
    """
    Internal fonction helper used by check_BST().
    """

    left = True
    right = True

    if tree is not None:
        if tree[1] is not None:
            if tree[1][0] >= tree[0] or (tree[1][0] <= borne_inf if borne_inf is not None else False):
                return False
            else:
                left = _check_BST(tree[1], borne_inf, tree[0])
            
        if tree[2] is not None:
            if tree[2][0] <= tree[0] or (tree[2][0] >= borne_sup if borne_sup is not None else False):
                return False
            else:
                right = _check_BST(tree[2], tree[0], borne_sup)
    else:
        return True
    
    return left and right

def check_BST(tree):
    """
    Check for a node in the binary search tree.

    Parameters:
    -----------
    ll : list
        The binary search tree.

    Returns:
    --------
    bool
        True if the tree is a BST, otherwise False.
    """

    if _check_BST(tree, None, None):
        print("It is a Binary Search Tree.")
    else:
        print("It is not a Binary Search Tree.")

def _depth(tree, node):
    """
    Internal fonction helper used by depth().
    """

    if tree is None:
        return None

    if tree[0] == node:
        return 0
    
    for i in range(1, len(tree)):
        result = _depth(tree[i], node)
        if result is not None:
            return 1 + result

def depth(tree):
    '''
    Find the depth of a node in the tree.

    Parameters:
    -----------
    tree : list
        The tree
    
    Returns:
    --------
    int
        The depth of the node in the tree
    '''

    node = input("Enter the node : ")
    print("The depth of", node, "in the tree is :", _depth(tree, node))

def _insert_in_BST(tree, node):
    """
    Internal fonction helper used by insert_in_BST().
    """

    if tree is not None:
        if node == tree[0]:
            return tree
        elif node < tree[0]:
            tree[1] = _insert_in_BST(tree[1], node)
        else:
            tree[2] = _insert_in_BST(tree[2], node)
        
        return tree
    else:
        return [node, None, None]

def insert_in_BST(tree):
    '''
    Insert a new element in the binary search tree.

    Parameters:
    -----------
    tree : list
        The tree

    Returns:
    list
        The binary search tree with the new element inserted.
    '''

    node = int(input("Entre the node : "))
    return _insert_in_BST(tree, node)

def create_tree():
    '''
    Create a tree

    Returns:
    --------
    list
        A list representing a tree.
    '''

    nb_children = int(input("Enter the number of the tree children : "))
    return _create_tree(nb_children)

def create_binary_search_tree():
    '''
    Create a binary search tree

    Returns:
    --------
    list
        A list representing a binary search tree.
    '''
    
    root = int(input("Enter your tree root : "))
    return _create_binary_search_tree(root, None, None)