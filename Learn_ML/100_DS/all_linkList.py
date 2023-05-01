'''
There are three common types of Linked List.

Singly Linked List
Doubly Linked List
Circular Linked List
'''


####################################
        # Single Linked List #
####################################

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def give_me_a_value(self):
        return random.randint(1, 999)

    def create_list_with_zero_node(self):
        self.linked_list = LinkedList()    
        self.print_list(linked_list)
        return linked_list

    def create_list_with_signle_node(self):
        random_value = self.give_me_a_value()
        node = Node(random_value)
        linked_list = LinkedList()
        linked_list.head = node
        self.print_list(linked_list)
        return linked_list

    def create_random_list(self):
        random_value = self.give_me_a_value()
        node = Node(random_value)
        linked_list = LinkedList()
        linked_list.head = node

        for i in range(2):
            random_value = self.give_me_a_value()
            new_node = Node(random_value)
            node.next = new_node
            node = new_node

        self.print_list(linked_list)
        return linked_list

    def print_list(self, linked_list):
        data_list = []
        node = linked_list.head
        while node:
            data_list.append(node.data)
            node = node.next
        print("LinkedList = ", data_list, "Len = ", len(data_list))

    def lenght_list(self, linked_list):
        list_len = 0
        node = linked_list.head
        while node:
            node = node.next
            list_len += 1
        print("Len = ", list_len)
        return list_len

    def insert_node(self, linked_list=None, pos=None, random_value=0):
        new_node = Node(random_value)

        if linked_list.head is None:
            # at top
            node = Node(random_value)
            linked_list.head = node

        elif pos is None:
            # at end
            node = linked_list.head
            pointer = linked_list.head
            while node:
                pointer = node
                node = node.next
            pointer.next = new_node

        elif pos == 1:
            # at 1st
            node = linked_list.head
            linked_list.head = new_node
            new_node.next = node

        else:
            # any position
            node = linked_list.head
            pointer = linked_list.head
            count = 1
            while node:
                if count == pos:
                    pointer.next = new_node
                    new_node.next = node
                pointer = node
                node = node.next
                count += 1
        
        self.print_list(linked_list)

    def delete_node(self, linked_list, pos=None):
        if pos is None:
            node = linked_list.head
            list_len = self.lenght_list(linked_list)
            previous_node = node
            count = 0
            while node:
                count = count + 1
                if list_len == count:
                    previous_node.next = None
                previous_node = node
                node = node.next
            del node
            self.print_list(linked_list)

        elif pos == 1:
            node = linked_list.head
            next_node = node.next
            linked_list.head = next_node
            del node
            self.print_list(linked_list)

        else:
            node = linked_list.head
            previous_node = node
            count = 0
            while node:
                count = count + 1
                if count == pos:
                    previous_node.next = node.next
                    del node
                    self.print_list(linked_list)
                    return
                previous_node = node
                node = node.next


    def search(self, linked_list, value):
        node = linked_list.head
        while node:
            if node.data == value:
                print("yes found")
                return
            node = node.next
        print("not found")


    def reverse_list(self, linked_list):
        '''
            1 -> 2-> 3-> 4 -> null
            4 -> 3 -> 2 -> 1 -> null
        '''
        current_node = linked_list.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            next_node.next = current_node
            previous_node = current_node
            current_node = next_node

        linked_list.head = previous_node
        self.print_list(linked_list)





linked_list = LinkedList()
linked_list = linked_list.create_random_list()
# linked_list.insert_node(linked_list=linked_list, random_value=500)
# linked_list.insert_node(linked_list=linked_list, pos=1, random_value=700)
# linked_list.insert_node(linked_list=linked_list, pos=2, random_value=800)
# linked_list.delete_node(linked_list=linked_list, pos=1)
# linked_list.delete_node(linked_list=linked_list, pos=2)
# linked_list.delete_node(linked_list=linked_list)
# linked_list.search(linked_list=linked_list, value=500)
linked_list.reverse_list(linked_list)


'''
Linked List Complexity
Time Complexity

 	    Worst case	Average Case
Search	    O(n)	O(n)
Insert	    O(1)	O(1)
Deletion	O(1)	O(1)


Space Complexity: O(n)
'''




####################################
        # Double Linked List #
####################################

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_double_list(self):
        new_list = LinkedList()
        return new_list
    
    def insert_first_node(self):
        new_list = self.create_double_list()
        random_val = random.randint(10, 99)
        node = Node(random_val)
        new_list.head = node
        new_list.tail = node
        return new_list
    
    def create_random_double_list(self):
        new_list = self.create_double_list()
        random_val = random.randint(10, 99)
        node = Node(random_val)
        new_list.head = node
        new_list.tail = node

        for i in range(4):
            random_val = random.randint(10, 99)
            new_node = Node(random_val)
            node.next = new_node
            new_node.prev = node
            new_list.tail = new_node
            node = new_node

        return new_list
    
    def print_list(self, new_list):
        node = new_list.head
        l = []
        while node:
            l.append(node.data)
            node = node.next
        print(l)
    
    def print_list_way2(self, new_list):
        start_node = new_list.head
        end_node = new_list.tail
        l = []
        while start_node != end_node:
            l.append(start_node.data)
            start_node = start_node.next
        l.append(start_node.data)
        print(l)


        
linked_list = LinkedList()
new_list = linked_list.create_random_double_list()
linked_list.print_list(new_list)
linked_list.print_list_way2(new_list)




####################################
        # Circular Linked List #
####################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_random_circular_list(self):
        value = random.randint(1, 999)
        node = Node(value)
        linked_list = LinkedList()
        linked_list.head = node
        linked_list.tail = node
        node.next = linked_list.head

        for i in range(2):
            value = random.randint(1, 999)
            new_node = Node(value)
            node.next = new_node
            new_node.next = linked_list.head
            linked_list.tail = new_node
            node = new_node

        return linked_list

    def print_circular_list(self, linked_list):
        start_node = linked_list.head
        end_node = linked_list.tail
        l = []
        while start_node != end_node:
            l.append(start_node.data)
            start_node = start_node.next
        l.append(start_node.data)
        print(l)


linked_list = LinkedList()
new_list = linked_list.create_random_circular_list()
linked_list.print_circular_list(new_list)
