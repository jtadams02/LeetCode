class Solution:
    def tribonacci(self, n: int) -> int:
        # Both solutions work and are good!
        # Smart solution below
        if n==0:
            return 0
        if n==1 or n==2:
            return 1

        o = 0
        tw = 1
        th = 1
        r = 0
        # All this solution does is slowly incrememnt the values of Tn,Tn+1,Tn+2 to equal Tn+3
        # Since we have base values up to Tn=2, we start with Tn=3, which is 0+1+2
        # And then we slowly inc our vals

        for i in range(3,n+1):
            r = o+tw+th # Current trib value
            # Tn = Tn-3 + Tn-2 + Tn-1
            # The Trib slowly get increased, so all we need to do is 
            # increase the values
            o = tw # If Tn-3 = 0, the next Tn-3 will be the previous Tn-2, so we set Tn-3 to Tn-2
            tw = th # Same Logic here, Tn-2 for Tn+1 will be equal to Tn-1
            th = r # And again Tn-1 can just be set to the previous Trib

        return r
        # Memoization Solution Below
        m = {
            0 : 0,
            1 : 1,
            2 : 1
        }
        def trib(num,m):
            if num in m:
                return m[num]
            else:
                ans = trib(num-3,m) +  trib(num-2,m) + trib(num-1,m) 
                m[num] = ans
                return ans

        return trib(n,m)
    

