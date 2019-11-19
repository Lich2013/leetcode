PREV, NEXT, KEY, RESULT = 0, 1, 2, 3
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.root = []
        self.root[:] = [self.root, self.root, None, None]
        self.hash_table = {}
        self.size = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_table:
            return -1
        node = self.hash_table[key]
        self._move_to_front(node)
        return node[RESULT]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash_table:
            node = self.hash_table[key]
            node[RESULT] = value
            self._move_to_front(node)
            return
        
        self.size += 1
        if self.size > self.capacity:
            self.root[KEY] = key
            self.root[RESULT] = value
            self.hash_table[key] = self.root
            self.root = self.root[NEXT]
            del self.hash_table[self.root[KEY]]
            return
        
        node = [None, None, key, value]
        self._insert_to_front(node)
        self.hash_table[key] = node
        
        
    def _move_to_front(self, node):
        self._delete_node(node)
        self._insert_to_front(node)
    
    
    def _insert_to_front(self, node):
        node[NEXT] = self.root
        node[PREV] = self.root[PREV]
        node[NEXT][PREV] = node
        node[PREV][NEXT] = node
    
    
    def _delete_node(self, node):
        node[PREV][NEXT] = node[NEXT]
        node[NEXT][PREV] = node[PREV]

    