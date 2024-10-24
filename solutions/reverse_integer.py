class Solution(object):
    def reverse(self, x):
        X_S= str(x)
        if X_S[0]=="-":
            si=False
        else:
            si=True


        if si==False:

            inv_S=X_S[::-1]
            inv_S=inv_S[:-1]
            inv= -1 * int(inv_S)
        else:
            inv_S=X_S[::-1]
            inv=int(inv_S)

        if inv<-2**31 or inv> (2**31) -1:
            return 0
        else:
            return inv

        """
        :type x: int
        :rtype: int
        """
