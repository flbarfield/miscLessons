'''Useful and/or necessary classes and methods relevant to Singly
Linked lists
'''

class Node:
    '''Key features of every node'''
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    '''Possible features of a LinkedList'''
    def __init__(self):
        self.head = None

    def print_list(self):
        '''Prints every node's data until it runs into None'''
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        '''Appends element to the end of LinkedLists'''
        new_node = Node(data)
        # handles if  there's no head present
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        # moves node to node until None is encountered
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        '''Prepends element to the beginning of a LinkedList,
        making a new node and assigning it as the head, and pointing
        to the next node
        '''
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        '''Places node after a defined previous node'''
        # check if node to be inserted after is in linked list or not. If not,
        # we return, otherwise the new_node is created
        if not prev_node:
            print('Previous node does not exist.')
            return
        new_node = Node(data)
        #sets pointer of new node to what prev node was pointing to
        new_node.next = prev_node.next
        #sets pointer of prev node to new node
        prev_node.next = new_node

    def delete_node(self, key):
        '''deletes node based on Key argument'''
        # declaring starting point of linked List
        cur_node = self.head
        # handling case if head is deleted
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            #deletes the cur_node
            cur_node = None
            return
        prev = None
        # runs to the end of the linked list OR stops if key is found
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        # implies key did not match any of the data of the current node,
        # and there's no need to delete.
        if cur_node is None:
            return
        # sets previous pointer to going-to-be-deleted node's pointer
        prev.next = cur_node.next
        # deletes node
        cur_node = None

    def delete_node_pos(self, pos):
        '''Deletes node based on position argument'''
        # checks if linked list is empty or not
        if self.head:
            cur_node = self.head
            if pos == 0:
                # declares the next node the head, and then deletes itself with None
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 0
            # increments count until it equals pos
            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.next
                count += 1

            # position was never found after traversing list
            if cur_node is None:
                return

            # moves pointer from the prev node from the currently selected node, and
            # affixes it to the next node, before it finally deletes itself.
            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        '''Counts through nodes and increments one for every node'''
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        '''Calls itself as it increments for each node'''
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key1, key2):
        '''Swaps node position pased on given keys'''
        if key1 == key2:
            return

        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def reverse_iterative(self):
        '''Basically flips each pointer to the opposite direction within the linked list
        '''
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # This refers to the last node in the linked list
        self.head = prev

    def reverse_recursive(self):
        '''Recursively flips each point to the opposite direction within a linked list
        '''

        def _reverse_recursive(cur, prev):
            '''When the end of the linked list and cur is None, prev is returned'''
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        '''Merging 2 lists, sorted. Key here is having three
            pointers: p, q, and s..."llist" represents the second linked 
            list.

            s will take the place of p or q depending on which list has
            the lesser value, and then push p or q along their respective lists.
        '''
        p = self.head
        q = llist.head
        s = None

        # this checks to make sure that neither list is empty.
        if not p:
            return q
        if not q:
            return p

        # comparing data the nodes are pointing to, setting pointers between \
        # the two lists if both lists have elements
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        # this runs the loop until q or p becomes none, and then continues
        # down p or q adding futher pointers?
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        '''loop through list once, keeping track of data held
        at each of the nodes. A hash table (or Python dictionary)
        is used to keep track of the encountered data elements.
        '''
        cur = self.head
        prev = None
        dup_values = {}

        while cur:
            if cur.data in dup_values:
                # Remove Node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n, method):
        '''Nth is is the inputted number from the last'''
        # method #1
        if method == 1:
            total_len = self.len_iterative()

            cur = self.head
            while cur:
                if total_len == n:
                    print(cur.data)
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None:
                return
        # method #2
        elif method == 2:
            p = self.head
            q = self.head

            if n > 0:
                count = 0
                while q:
                    count += 1
                    if count >= n:
                        break
                    q = q.next

                if not q:
                    print(str(n) + ' is greater than the number of nodes in list.')
                    return

                while p and q.next:
                    p = p.next
                    q = q.next
                return p.data
            # unnecessary, but keeping in for learning purpose
            # else:
            #     return None

    def count_occurances_iterative(self, data):
        '''counts occurances of duplicate values'''
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, node, data):
        '''counts occurances of duplicates recursively'''
        # wait, I think this is also unnecessary but I'll keep it in
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        #unnessary, but keeping in for the learning process.
        # else:
        #     return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        '''rotates list given an input of k'''
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None
