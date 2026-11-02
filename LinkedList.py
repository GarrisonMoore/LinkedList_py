from typing import Any

class Node:
    """
    Creates a node
    """
    def __init__(self, data:Any):
        self.data = data # data stored in a node
        self.next = None # pointer, next node in the linked list

    def __repr__(self):
        return self.data

class LinkedList:
    """
    Creates a custom linked list
    """
    def __init__(self, nodes=None):
        # Head is the start of the linked list
        self.head = None

        # tail is the end of the linked list, needs to be 'None'
        self.tail = None

    def __repr__(self):
        result = ""

        # If no head, assign "None"
        if not self.head:
            result = "None"

        # If there is a head, results should display nodes and edges
        else:
            current_node = self.head
            while current_node is not None:
                result += f"{current_node.data} -> "
                current_node = current_node.next
            result += "None"

        return result

    def append_before(self, node_to_add:Node) -> None:
        """
        Appends a node to the start of the linked list
        """
        # Check if node_to_add is anything other than a node or a child of a node
        if not isinstance(node_to_add, Node):
            # make a node out of data and proceed
            data_to_add = node_to_add
            node_to_add = Node(data_to_add)

        # if there is no head, add one
        if not self.head:
            self.head = node_to_add
        else:
            # Point the new node to the current start of the list
            node_to_add.next = self.head
            # Reassign header pointer to the new node
            self.head = node_to_add

    def append_after(self, node_to_add:Node):
        """
        Appends a node to the end of a linked list
        """
        # Check if node_to_add is anything other than a node or a child of a node
        if not isinstance(node_to_add, Node):
            # make a node out of data and proceed
            data_to_add = node_to_add
            node_to_add = Node(data_to_add)

        # if there is no head, add one
        if not self.head:
            self.head = node_to_add

        else:
            # find the tail
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next
            tail = current_node
            # make the node to add come after the tail
            tail.next = node_to_add

    def pop_before(self):
        """
        Removes an element from the start of the linked list
        """
        if not self.head:
            return None

        # Point the node to remove to the head of the list
        node_to_remove = self.head

        # assign the current head to the value of the next node??
        self.head = self.head.next

        return node_to_remove

    def pop_after(self):
        """
        Removes an element from the end of the linked list
        """
        if not self.head:
            return None

        else:
            # find the tail
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            node_to_remove = current_node

            self.tail = self.tail.next

        return node_to_remove

    def return_data(self, node):
        """
        Return data of a node
        """
        return node.data



# Create a node and put some data in it
node_a = Node("A")
node_b = Node("B")

llist = LinkedList()
print(llist)

llist.append_after(node_a)
print(llist)

llist.append_after(node_b)
print(llist)

for c in "CDEFGHIJKLPMOPQRSTUVWXYZ":
    llist.append_after(Node(c))
print(llist)

llist.append_before(Node(1))
print(llist)

llist.pop_before()
print(llist)

llist.pop_after()
print(llist)
