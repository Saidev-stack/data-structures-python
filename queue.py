from stack import create_stack
from stack import restore_stack
from stack import display_list
# Queue functions block
def create_queue():
    '''
    Create a queue

    Returns:
    --------
    list
        A list representing a queue.
    '''

    queue = []
    stack = create_stack()
    restore_stack(queue, stack)
    return queue

def _enqueue(queue, item):
    """
    Internal function helper used by enqueue().
    """

    return [item] + queue

def enqueue(queue):
    '''
    Enqueue a new element in the queue.

    Parameters:
    -----------
    queue : list
        The queue
    
    Returns:
    --------
    list
        The queue with the new element added.
    '''

    item = input("Enter the new element to enqueue : ")
    return _enqueue(queue, item)

def dequeue(queue):
    """
    Dequeue an element from the stack.

    Parameters:
    -----------
    queue : list
        The queue.

    Returns:
    --------
    list
        The queue after the front element has been removed.
    """

    return queue[:-1]

def peek(queue):
    """
    Peek the front element of the queue.

    Parameters:
    -----------
    queue : list
        The queue.

    Returns:
    --------
    Any
        This function displays the front element's of the queue without removing it
    """

    print("The front of the queue is :", queue[-1])

def is_empty(queue):
    '''
    Check if the queue is empty or not.

    Parameters:
    -----------
    queue : list
        The queue

    Returns:
    --------
    bool
        True if the queue is empty, otherwise False.
    '''

    if len(queue) == 0:
        print("The queue is empty")
    else:
        print("The queue isn't empty")

def display_queue(queue):
    '''
    Display the queue

    Parameters:
    -----------
    queue : list
        The queue
    
    Returns:
        This function displays the queue in the console.
    '''

    print('Rear =>' + display_list(queue)[2:] + ' <= Front')