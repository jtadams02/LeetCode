class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = n

        # Edge Case when the length is 1:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                count -= 1
                flowerbed[0] = 1
        else:
            for i in range(0,len(flowerbed)):
                prev = i - 1
                succ = i + 1

                # Check if there exists both a prev and succ

                if prev >= 0 and succ < len(flowerbed):
                    if flowerbed[i] != 1 and flowerbed[prev] != 1 and flowerbed[succ] != 1:
                        flowerbed[i] = 1
                        count -= 1
                elif prev >= 0:
                    if flowerbed[i] != 1 and flowerbed[prev] != 1:
                        flowerbed[i] = 1
                        count -= 1
                
                elif succ < len(flowerbed):
                    if flowerbed[i] != 1 and flowerbed[succ] != 1:
                        flowerbed[i] = 1
                        count -= 1
        
        if count <= 0:
            return True
        else:
            return False