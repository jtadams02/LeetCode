class Solution:
    def arraySign(self, nums: List[int]) -> int:

        # So this is literally just asking us to make a product of all the items in the array
        # This is so simple

        product = None

        for x in nums:
            if product == None:
                product = x
            else:
                product *= x
        
        def signFunc(p):
            # Just say what it is ig
            if p > 0:
                return 1
            elif p == 0:
                return 0
            else:
                return -1
    
        return signFunc(product)