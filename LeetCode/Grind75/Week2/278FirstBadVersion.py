# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # We could do a binary search approach
        left = 0
        right = n

        while left <= right:

            mid = (right+left) // 2
            # print(f"Mid: {mid}")
            m_val = isBadVersion(mid)
           # m_val_plus = isBadVersion(mid+1)
            m_val_neg = isBadVersion(mid-1)
            if m_val and not m_val_neg:
                return mid
            elif not m_val:
                # We need to go right
                left = mid+1
            elif m_val:
                # We need to go left
                right = mid-1
        