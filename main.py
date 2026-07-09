import linear_linked_list
import stack
import queue
import tree
import menu

dict_create = {
    1 : linear_linked_list.create_linked_list,
    2 : stack.create_stack,
    3 : queue.create_queue,
    4 : tree.create_tree,
    5 : tree.create_binary_tree,
    6 : tree.create_binary_search_tree
}

dict_linked_list = {
    1 : linear_linked_list.display_linked_list,
    2 : linear_linked_list.inseration_linked_list,
    3 : linear_linked_list.delete_node,
    4 : linear_linked_list.search_in_linked_list,
    5 : linear_linked_list.find_node_by_data
}

dict_stack = {
    1 : stack.display_stack,
    2 : stack.push,
    3 : stack.pop_from_stack
}

dict_queue = {
    1 : queue.display_queue,
    2 : queue.enqueue,
    3 : queue.dequeue,
    4 : queue.peek,
    5 : queue.is_empty
}

dict_tree  = {
    1 : tree.display_tree,
    2 : tree.search_in_tree,
    3 : tree.depth,
    4 : tree.height_tree,
    5 : tree.count_tree_nodes,
    6 : tree.count_feuille
}

dict_binary_tree  = {
    1 : tree.display_binary_tree,
    2 : tree.search_in_tree,
    3 : tree.depth,
    4 : tree.height_tree,
    5 : tree.count_tree_nodes,
    6 : tree.count_feuille,
    7 : tree.check_BST
}

dict_BST  = {
    1 : tree.display_binary_tree,
    2 : tree.search_in_tree,
    3 : tree.depth,
    4 : tree.height_tree,
    5 : tree.count_tree_nodes,
    6 : tree.count_feuille,
    7 : tree.insert_in_BST
}

dict_ds_dicts = {
    1 : dict_linked_list,
    2 : dict_stack,
    3 : dict_queue,
    4 : dict_tree,
    5 : dict_binary_tree,
    6 : dict_BST
}

dict_menu = {
    1 : menu.linear_linked_list_operations,
    2 : menu.stack_opertaions,
    3 : menu.queue_opertaions,
    4 : menu.tree_opertaions,
    5 : menu.binary_tree_opertaions,
    6 : menu.binary_search_tree_opertaions
}

answer = 'yes'

while answer.lower() == 'yes':
    menu.menu()
    while True:
        try :
            choice = int(input("Would you please enter the DS number to be create : "))   
            
            if choice in dict_create:
                break
            else:
                print("Invlaide choice!")

        except ValueError:
            print("Invalide input!")
        
    ds = dict_create[choice]()

    dict_menu[choice]()

    while True:
        try :
            choice2 = int(input("Would you please entre the operation number : "))
            
            if choice2 in dict_ds_dicts[choice]:
                break
            else:
                print("Invalide choice!")
            
        except ValueError:
            print("Invalide input!")

    dict_ds_dicts[choice][choice2](ds)
    answer2 = input("Do you want to execute another operation ? (yes/non) : ")
    while answer2.lower() == 'yes':
        dict_menu[choice]()
        while True:
            try :
                choice2 = int(input("Would you please entre the operation number : "))
            
                if choice2 in dict_ds_dicts[choice]:
                    break
                else:
                    print("Invalide choice!")
            
            except ValueError:
                print("Invalide input!")

        ds2 = dict_ds_dicts[choice][choice2](ds)

        if type(ds2) is list:# TODO : improve the way modified data structures are detected 
            ds = ds2
        
        answer2 = input("Do you want to execute another operation ? (yes/non) : ")

    #choice = int(input("Would you please entre the DS number to be create : "))

    answer = input("Would you continue ? (yes/no) : ")
