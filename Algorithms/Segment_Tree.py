# CODE: To implement range_sum and query Operations in a Segment tree
# Time Complexities:
# creation: O(N)
# range_sum: O(log(N))
# update: O(log(N))


from math import log2, ceil


class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.array_size = len(A)
        height = ceil(log2(self.array_size + 1))
        size = (1 << height + 1) - 1
        self.segment_tree = [0] * size
        self.__construct()
    
    def __repr__(self):
        return f"{self.segment_tree}"
    
    def __construct(self, left=None, right=None, index=0) -> int:
        if left is None: left = 0
        if right is None: right = self.array_size - 1
        
        if left == right:  # Reached Root Node
            self.segment_tree[index] = self.array[left]
        else:
            mid = (left + right) // 2
            left_node = self.__construct(left, mid, 2 * index + 1)  # Splitting the array
            right_node = self.__construct(mid + 1, right, 2 * index + 2)
            self.segment_tree[index] = left_node + right_node
        return self.segment_tree[index]
    
    def __update(self, pos: int, difference: int, index=0, left=None, right=None) -> None:
        if left is None: left = 0
        if right is None: right = self.array_size - 1
        if left > pos or right < pos:
            return
        
        self.segment_tree[index] += difference
        if left != right:
            mid = (left + right) // 2
            self.__update(pos, difference, 2 * index + 1, left, mid)
            self.__update(pos, difference, 2 * index + 2, mid + 1, right)
    
    def range_sum(self, lower_range: int, upper_range: int, index=0, left=None, right=None) -> int:
        if left is None: left = 0
        if right is None: right = self.array_size - 1
        if lower_range <= left and upper_range >= right:  # CASE 1: Total Overlapping Case
            return self.segment_tree[index]
        
        if right < lower_range or left > upper_range:  # CASE 2: No Overlap
            return 0
        
        # CASE 3: Partial Overlapping
        mid = (left + right) // 2
        left_node = self.range_sum(lower_range, upper_range, 2 * index + 1, left, mid)  # Splitting the array
        right_node = self.range_sum(lower_range, upper_range, 2 * index + 2, mid + 1, right)
        return left_node + right_node
    
    def update(self, pos: int, value: int) -> None:
        difference = value - self.array[pos]
        self.array[pos] = value
        self.__update(pos, difference)


if __name__ == '__main__':
    A = [*range(1, 11)]
    seg_tree = SegmentTree(A)
    print(seg_tree.range_sum(0, 4))
    print(seg_tree)
    seg_tree.update(0, 9)
    print(seg_tree)
    print(A)
