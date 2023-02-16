"""
-------------------------------------------------------
Utilities
-------------------------------------------------------
Author:  Matthew McCulley
ID:      210804290
Email:   mccu4290@mylaurier.ca
__updated__ = '2022-01-18'
-------------------------------------------------------
"""

#imports
from copy import deepcopy
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    empty = lst.is_empty()
    print(f"Is the list empty? {empty}")
    value = source.pop(0)
    lst.append(value)
    print()
    print(f"""Appending:
{value}""")
    i = 0
    value = source.pop(0)
    lst.insert(i, value)
    print(f"""Replacing that object with the object coming after it. So now the list should be 
{value}""")
    empty = lst.is_empty()
    print(f"Is the list empty {empty}")
    count = lst.count(value)
    print(f"""The count of
{value} 
in the list is {count}""")
    i = lst.index(value)
    print(f"""The index of 
{value}
is {i}""")
    find = lst.find(value)
    print(f"""Find the copy of 
{value}
Copy:
{find}""")
    minimum = lst.min()
    maximum = lst.max()
    print(f"""The minimum in the list is 
{minimum}
and the max is
{maximum}""")
    removed = lst.remove(value)
    print(f"""Removing
{removed}""")
    empty = lst.is_empty()
    print(f"So the list empty: {empty}")
    first = lst[0]
    print(f"""So now the first and only object in the list should be
{first}""")
    return
def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source != []:
        value = source.pop(0)
        llist.append(value)
        
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0
    n = len(llist)
    while i < n:
        value = llist.pop(0)
        target.append(value) 
        i += 1  
          
    return
def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    FIRST = 0
    while source != []:
        element = source.pop(FIRST)
        pq.insert(element)
    
    return 
        

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not pq.is_empty():
        element = pq.remove()
        target.append(element)
    
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    empty = pq.is_empty()
    print(f"Is the priority queue empty? {empty}")
    print()
    for value in a:
        print(f"""Inserting the element of highest priority:
{value}""")
        pq.insert(value)
    print()
    empty = pq.is_empty()
    n = len(pq)
    print(f"What is the length of the priority queue? {n}")
    print(f"Is the priority queue empty now? {empty}")
    print()
    while not pq.is_empty():
        peek = pq.peek()
        print(f"""What is the peek? 
{peek}""")
        removed = pq.remove()
        print(f"""So this following removed item should be the same as the one just peeked: 
{removed}""")
    empty = pq.is_empty()
    print()
    print(f"And now the queue should be empty: {empty}")
    
    return

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    n = len(source)
    i = 0
    while i < n:
        queue.insert(deepcopy(source.pop(0)))
        i += 1
        
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not queue.is_empty():
        value = queue.remove()
        target.append(value)
        
    return 

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
    is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    empty = q.is_empty()
    print(f"Is the queue empty? {empty}")
    print()
    for value in a:
        print(f"Inserting: {value}")
        q.insert(value)
    print()
    empty = q.is_empty()
    n = len(q)
    print(f"What is the length of the queue? {n}")
    print(f"Is the queue empty now? {empty}")
    print()
    while not q.is_empty():
        peek = q.peek()
        print(f"What is the peek? {peek}")
        removed = q.remove()
        print(f"So this following remove item should be the same a peek: {removed}")
    empty = q.is_empty()
    print()
    print(f"And now the queue should be empty: {empty}")
    

    return

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = len(source)
    while i > 0:
        stack.push(deepcopy(source.pop()))
        i -= 1
        
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        top = deepcopy(stack.pop())
        target.insert(0,top)

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    
    stack = Stack()
    array_to_stack(stack, source)
    b = stack.is_empty()
    print(f"Is empty? {b}")
    peek = stack.peek()
    print(f"Peek: {peek}")
    popped = stack.pop()
    print(f"Popped: {popped}")
    stack.push(popped)
    pushed = stack.peek()
    stack.push(popped)
    print(f"Pushing the popped object back onto the stack: {pushed}")
    
    