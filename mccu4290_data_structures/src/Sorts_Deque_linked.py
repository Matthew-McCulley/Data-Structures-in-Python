"""
-------------------------------------------------------
Linked versions of various sorts. Implemented on linked Deques.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2021-04-09"
-------------------------------------------------------
"""
from math import log
from Deque_linked import Deque


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times 
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def gnome_sort(a):
        """
        -------------------------------------------------------
        Sorts a Deque using the Gnome Sort algorithm.
        Use: gnome_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked structure of comparable elements (Deque)
        Returns:
            None
        -------------------------------------------------------
        """
        gnome = a._front
        while gnome is not None:
            if gnome._prev is not None and gnome._value < gnome._prev._value:
                a._swap(gnome, gnome._prev)
            else:
                gnome = gnome._next       
        return

    # Sort Utilities
    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"
            
                        
        if r._prev is l:
            temp = r._next
            if l._prev is not None:
                l._prev._next = r 
            r._prev = l._prev
            r._next = l 
            l._prev = r 
            l._next = temp
            if l._next is not None:
                l._next._prev = l
        elif l._prev is r:
            temp = l._next
            if r._prev is not None:
                r._prev._next = l
            l._prev = r._prev
            l._next = r
            r._prev = l
            r._next = temp
            if l._next is not None:
                r._next._prev = r
        else:
            l_temp_prev = l._prev 
            l_temp_next = l._next 
                       
            l._prev = r._prev  
            l._next = r._next 
                     
            r._prev = l_temp_prev 
            r._next = l_temp_next 
                    
            if r._prev is None:
                self._front = r 
            else:
                r._prev._next = r
            if r._next is None: 
                self._rear = r
            else:
                r._next._prev = r
            if l._prev is None:
                self._front = l 
            else:
                l._prev._next = l 
            if l._next is None:
                self._rear = l
            else:
                l._next._prev = l
            
        return
    @staticmethod
    def sort_test(a):
        """
        -------------------------------------------------------
        Determines whether a linked deque is sorted or not.
        Use: sort_test(a)
        -------------------------------------------------------
        Parameters:
            a - a linked deque of comparable elements (?)
        Returns:
            is_sorted - True if contents of a are sorted, False otherwise.
        -------------------------------------------------------
        """
        is_sorted = True
        # Test forward links
        current = a._front

        while is_sorted and current is not None and \
                current._next is not None:

            if current._value <= current._next._value:
                current = current._next
            else:
                is_sorted = False
        # Test reverse links
        current = a._rear

        while is_sorted and current is not None and \
                current._prev is not None:

            if current._value >= current._prev._value:
                current = current._prev
            else:
                is_sorted = False

        return is_sorted
