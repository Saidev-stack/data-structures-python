# Linear linked list functions block
def create_node(node_address, data, next_node_address):
    '''
    Create a node

    Parameters:
    -----------
    node_address : int
        The address of the node

    data : Any
        The data " information " to be hold in the node

    next_node_address : int
        The address of the next node

    Returns:
    --------
    list
        Node implemented of list contains the node address, the data and the next node address resp.
    '''
    return [node_address, data, next_node_address]

def create_linked_list():
    """
    Create a linear linked list.

    Returns:
    --------
    list
        A list of lists representing a linear linked list, where each inner list represents a node.
"""
    ll = []
    answer = 'yes'
    N_add = 0

    while answer == 'yes':
        your_data = input("Enter your data/information to stock it in the node : ")
        ll.append(create_node(N_add, your_data, N_add + 1))
        N_add += 1
        answer = input("Enter 'yes' to add another node : ").lower()
    
    type_ll_choice = int(input("Choose the type of your likend list, 1 for Singly and 2 for Circular => "))
    
    while type_ll_choice not in [1, 2]:
        type_ll_choice = int(input("Invalid choice, Choose the type of your likend list, 1 for Singly and 2 for Circular => "))
    
    if type_ll_choice == 1 :
        ll[-1][2] = None
    else:
        ll[-1][2] = 0
    
    return ll

def update_address(ll):
    """
    Update the addresses of all nodes in a linear linked list.

    Parameters:
    -----------
    ll : list
        The linear linked list.

    Returns:
    --------
    list
        The updated linear linked list.
    """
    
    for e in ll:
        e[0] += 1
        if e[-1] == None:
            return ll
        e[-1] += 1
    
    return ll

def _inseration_linked_list(ll, data):
    """
    Internal function helper used by inseration_linked_list().
    """

    print("Insertion menu : \n 1 - In the front \n 2 - In the end \n 3 - In the middle")
    
    inser_in = int(input("To insert a new element specify its place, Would you enter : "))
    
    if inser_in == 1:
        ll = [create_node(ll[0][0] - 1, data, ll[0][0])] + ll
    elif inser_in == 2:
        if ll[-1][-1] == None:
            ll[-1][-1] = ll[-1][0] + 1
            ll = ll + [create_node(ll[-1][-1], data, None)]
        else:
            ll = ll + [create_node(ll[-1][-1], data, ll[0][0])]
    elif inser_in == 3:
        position = int(input("To insert your element in the middle, we need to specify its position : "))
        if position > len(ll):
            print("Impossible to add the new element, position out of range")
        else:
            ll = ll[:position] + [create_node(ll[position - 1][-1], data, ll[position][0] + 1)] + update_address(ll[position:])
    
    return ll

def inseration_linked_list(ll):
    """
    Insert a new element into the linked list.

    Parameters:
    -----------
    ll : list
        The linked list.

    Returns:
    --------
    list
        The linked list with the new element inserted.
    """
    
    data = input("Enter your data to be hold : ")
    return _inseration_linked_list(ll, data)

def display_linked_list(ll):
    """
    Display the linear linked list.

    Parameters:
    -----------
    ll : list
        The linear linked list.

    Returns:
    --------
    None
        This function displays the linear linked list in the console.
    """
    
    is_circular = ll[0][0] == ll[-1][-1]
    
    for node in ll:
            print(f"[{node[1]}] --> ", end="")
    if is_circular:
        print("Back to start")
    else:
        print("None")   

def _delete_node(ll, position):
    """
    Internal function helper used by delete_node().
    """
    
    if position >= len(ll):
        print("Out of range!")
    else:
        ll = update_address(ll[:position]) + ll[position + 1:]

        if ll[-1][-1] is not None:
            ll[-1][-1] = ll[0][0]
    
    return ll

def delete_node(ll):
    '''
    Delete a node from the linear linked list

    Parameters:
    -----------
    ll : list
        The linear linked list
    Returns:
    --------
    list
        The linked list with the node deleted.
    '''
    
    position = int(input("Enter the position of the node to be deleted : "))
    return _delete_node(ll, position)

def _search_in_linked_list(ll, data):
    """
    Internal function helper used by search_in_linked_list().
    """

    return any(node[1] == data for node in ll)

def search_in_linked_list(ll):
    """
    Search for a node in the linear linked list.

    Parameters:
    -----------
    ll : list
        The linear linked list.

    Returns:
    --------
    bool
        True if the data is found, otherwise False.
    """

    data = input("Enter you data : ")

    if _search_in_linked_list(ll, data):
        print(data, "is in the Linear linked list.")
    else:
        print(data, "isn't in the Linear linked list.")

def _find_node_by_data(ll, data):
    """
    Internal function helper used by find_node_by_data().
    """

    for node in ll:
        if node[1] == data:
            return node
    
    return None

def find_node_by_data(ll):
    '''
    Find and display a node using its data
    
    Parameters:
    -----------
    ll : list
        The linear linked list

    Returns:
    --------
    list
        The node holding the data
    '''

    data = input("Enter your data : ")
    print(_find_node_by_data(ll, data))