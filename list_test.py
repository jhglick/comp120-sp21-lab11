# File: list_test.py
# Date: April 13, 2021
# Author: Dr. Glick
# Description: Code to test remove, __eq__, and
#        inorder methods of the LinkedList class.

from list_linked import LinkedList

def linked_list_test():
    """ Test remove, equals, and inorder methods """

    # Create a linked list
    l = LinkedList()
    
    # Append some values
    for i in range(10):
        l.append(i)

    print("Testing remove on a longer list\n")
    print(f"list is {str(l)}\n")
    print("Remove the value that is at the front of the list")
    l.remove(0)
    print(f"Your list after remove 0 is {str(l)}")
    if str(l) == "[1, 2, 3, 4, 5, 6, 7, 8, 9]":
        print("Correct")
    else:
        print(f"Incorrect.  SHould be [1, 2, 3, 4, 5, 6, 7, 8, 9]")

    print("\nRemove a value from the middle of the list")
    l.remove(6)
    print(f"Your list after remove 6 is {str(l)}")
    if str(l) == "[1, 2, 3, 4, 5, 7, 8, 9]":
        print("Correct")
    else:
        print(f"Incorrect.  SHould be [1, 2, 3, 4, 5, 7, 8, 9]")

    print("\nRemove a value from the end of the list")
    l.remove(9)
    print(f"Your list after remove 9 is {str(l)}")
    if str(l) == "[1, 2, 3, 4, 5, 7, 8]":
        print("Correct")
    else:
        print(f"Incorrect.  SHould be [1, 2, 3, 4, 5, 7, 8]")
    if l.back.item != 8:
        print("The back pointer of your list was not updated correctly")

    print("\nTry to remove a value not in the list")
    try:
        l.remove(20)
        print("Your method did not correctly raise a ValueError")
    except ValueError:
        print("Correctly raised value error")
        if str(l) != "[1, 2, 3, 4, 5, 7, 8]":
            print(f"Your list value of {str(l)} is incorrect.")
            print("[1, 2, 3, 4, 5, 7, 8]")

    print("\nTesting on remove last item in list")
    l = LinkedList()
    l.append(1)
    l.remove(1)
    if str(l) == "[]":
        if l.front == None and l.back == None:
            print("Correct")
        else:
            print("You front or back reference is incorrect after removing last item")
    else:
        print("Incorrectly removed last element in list")
        print(f"Your list is {str(l)}, and it should be []")


    print("\nTesting __eq__ method")
    print("\nTest equality of two lists references that refer to the same list in memory")
    l1 = LinkedList()
    l2 = l1
    l1.append(1)
    l1.append(2)
    print(f"List is {str(l1)}")
    if l1 == l2:
        print("Correct")
    else:
        print("Incorrect.   You should have reported True")

    print("\nTest equality of two lists that are different objects but equivalent")
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(8):
        l1.append(i)
        l2.append(i)
    print(f"List is {str(l1)}")
    if l1 == l2:
        print("Correct")
    else:
        print("Incorrect.   You should have reported True")

    print("\nTest equality of two lists that are empty and equivalent")
    l1 = LinkedList()
    l2 = LinkedList()
    print(f"List is {str(l1)}")
    if l1 == l2:
        print("Correct")
    else:
        print("Incorrect.   You should have reported True")

    print("\nTest equality of two lists that are different only in length")
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(8):
        l1.append(i)
        l2.append(i)
    l2.append(9)
    print(f"List 1 is {str(l1)}")
    print(f"List 2 is {str(l2)}")
    if l1 != l2:
        print("Correct")
    else:
        print("Incorrect.   You should have reported False")

    print("\nTest equality of two lists that are different in last item")
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(8):
        l1.append(i)
        l2.append(i)
    l1.append(10)
    l2.append(9)
    print(f"List 1 is {str(l1)}")
    print(f"List 2 is {str(l2)}")
    if l1 != l2:
        print("Correct")
    else:
        print("Incorrect.   You should have reported False")

    print("\nTest equality of two lists that are different in a middle item")
    l1 = LinkedList()
    l2 = LinkedList()
    for i in range(4):
        l1.append(i)
        l2.append(i)
    l1.append(20)
    l2.append(25)
    for i in range(3):
        l1.append(i)
        l2.append(i)
    print(f"List 1 is {str(l1)}")
    print(f"List 2 is {str(l2)}")
    if l1 != l2:
        print("Correct")
    else:
        print("Incorrect.   You should have reported False")

    print("\nTesting inorder method")
    print("\nTest inorder with empty list")
    l = LinkedList()
    if l.inorder():
        print("Correct")
    else:
        print("Incorrect.  Should report True")

    print("\nTest inorder with list containing a single item")
    l = LinkedList()
    l.append(5)
    if l.inorder():
        print("Correct")
    else:
        print("Incorrect.  Should report True")

    print("\nTest inorder with list with a longer ordered list")
    l = LinkedList()
    for i in range(10):
        l.append(i)
    if l.inorder():
        print("Correct")
    else:
        print("Incorrect.  Should report True")

    print("\nTest inorder with list with a list that is not ordered.")
    print("With unordered items at the beginning")
    l = LinkedList()
    l.append(5)
    for i in range(10):
        l.append(i)
    if not l.inorder():
        print("Correct")
    else:
        print("Incorrect.  Should report False")

    print("\nTest inorder with list with a list that is not ordered.")
    print("With unordered items at the end")
    l = LinkedList()
    for i in range(10):
        l.append(i)
    l.append(3)
    if not l.inorder():
        print("Correct")
    else:
        print("Incorrect.  Should report False")

    print("\nTest inorder with list with a list that is not ordered.")
    print("With unordered items in the middle")
    l = LinkedList()
    for i in range(5):
        l.append(i)
    l.append(-4)
    for i in range(5, 10):
        l.append(i)
    if not l.inorder():
        print("Correct")
    else:
        print("Incorrect.  Should report False")

if __name__ == "__main__":
    linked_list_test()