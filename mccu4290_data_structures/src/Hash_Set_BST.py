"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew McCulley
ID:      210804290
Email:   mccu4290@mylaurier.ca
__updated__ = '2022-03-23'
-------------------------------------------------------
"""
# Imports
# Use any appropriate data structure here.
from BST_linked import BST

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameter:
            capacity - size of initial table in Hash Set  (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._capacity = capacity
        self._table = []
        self._count = 0

        # Define the empty table.
        for _ in range(self._capacity):
            self._table.append(BST())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """

        h = hash(key)
        slot_location = h % self._capacity
        slot = self._table[slot_location]
        return slot


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """

        l = self._find_slot(key)
        return key in l


    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(value) 
        inserted = slot.insert(value)
        if inserted:
            self._count += 1
        if self._count/self._capacity > self._LOAD_FACTOR:
            self._rehash()
        return

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns a copy of the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        value = None 
        slot = self._find_slot(key)
        if key in slot:
            value = slot.remove(key)
            self._count -= 1
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Creates a new larger table in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        
        """
        beginning_capacity = self._capacity
        self._capacity = 2 * self._capacity + 1
        for _ in range(beginning_capacity, self._capacity):
            self._table.append(List())
        
        for slot in self._table:
            for item in slot:
                value = self.remove(item) 
                self.insert(value)
        """
        
        new_table = [] 
        count = 0
        for _ in range(2*self._capacity+1):
            new_table.append(BST()) 
        
        for slot in self._table:
            for element in slot:
                value = self.remove(element)
                if value is not None:
                    h = hash(value)
                    slot_location = h % len(new_table)
                    slot = new_table[slot_location]
                    if value not in slot:
                        slot.insert(value)
                        count += 1
        self._capacity = 2*self._capacity+1
        self._table = new_table 
        return
    
    


    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same values
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """

        # your code here


    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        capacity = self._capacity
        print(f"{capacity} slots")
        print()
        print(SEP)
        print(SEP)
        slot_number = 0
        for slot in self._table:
            print(f"Slot {slot_number}")
            print()
            for item in slot:
                print(item)
                print()
            slot_number += 1


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slot. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item

