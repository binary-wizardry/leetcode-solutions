class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pointer1 = pointer2 = 0
        merge = []
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            id1, num1 = nums1[pointer1]
            id2, num2 = nums2[pointer2]
            if id1 == id2:
                merge.append([id1, num1 + num2])
                pointer1 += 1
                pointer2 += 1
            elif id2 > id1:
                merge.append([id1, num1])
                pointer1 += 1
            else:
                merge.append([id2, num2])
                pointer2 += 1
        if pointer1 == len(nums1):
            merge += nums2[pointer2:]
        else:
            merge += nums1[pointer1:]
        return merge
