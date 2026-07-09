# Stack functions block
def create_stack():
    '''
    Create a stack

    Returns:
    --------
    list
        A list representing a stack.
    '''
    answer = 'yes'
    stack = []
    
    while answer == 'yes':
        element = input("Enter the new element : ")
        stack.append(element)
        answer = input("Enter 'yes' to continue your implementation => ")
    
    return stack

def restore_stack(s1, s2):
    """
    Internal function helper used by _puch() and _pop_from_stack().
    """

    while(s2 != []):
        e = s2.pop()
        s1.append(e)

def _push(stack, element, position):
    """
    Internal function helper used by push().
    """
    
    if position > len(stack):
        print("Out of range!")
    else:
        stack2 = []
        i = 0

        while(i < position):
            ele = stack.pop()
            stack2.append(ele)
            i += 1

        stack.append(element)
        restore_stack(stack, stack2)
    
    return stack

def push(stack):
    '''
    Push a new element in the stack.

    Parameters:
    -----------
    stack : list
        The stack
    
    Returns:
    --------
    list
        The stack with the new element pushed.
    '''
    
    element = input("Enter the new element : ")
    position = int(input("Enter its position : "))
    return _push(stack, element, position)

def _pop_from_stack(stack, position):
    """
    Internal function helper used by pop_from_stack().
    """

    if position >= len(stack):
        print("Out of range!")
    else:
        stack2 = []
        i = 0

        while(i < position):
            ele = stack.pop()
            stack2.append(ele)
            i += 1
        
        stack.pop()
        restore_stack(stack, stack2)
    
    return stack

def pop_from_stack(stack):
    """
    Pop an element from the stack.

    Parameters:
    -----------
    stack : list
        The stack.

    Returns:
    --------
    list
        The stack after the top element has been popped.
    """

    position = int(input("Enter the position of the element to pop : "))
    return _pop_from_stack(stack, position)

def display_list(stack):
    """
    Internal fonction helper used by dispaly fonctions.
    """

    if len(stack) == 1:
        return '||  ' + str(stack[0]) + '\t'
    else:
        return display_list(stack[:-1]) + display_list([stack[-1]])

def display_stack(stack):
    '''
    Display the stack

    Parameters:
    -----------
    stack : list
        The stack
    
    Returns:
        This function displays the stack in the console.
    '''

    print(display_list(stack) + ' <= Top')