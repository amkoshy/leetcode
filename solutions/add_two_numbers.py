#Add two numbers stored as linked lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def ssum( one,two,buf):
    temp_sum = one + two +buf
    if temp_sum>9:
        en = temp_sum -10
        fac = 1
    else:
        en = temp_sum
        fac = 0
    return fac,en
class Solution:

    def insert(self,l, val):       
        while l.next!=None:
            l=l.next
        l.next =ListNode(val)
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ListNode(0)

        a_flag = True
        b_flag = True
        buf,en=0,0
        while a_flag or b_flag or buf>0:
            if a_flag:      
                one = l1.val 
                if l1.next!=None:
                    l1= l1.next                
                else:
                    a_flag = False
            else:
                one =0
            if b_flag:      
                two = l2.val 
                if l2.next!=None:
                    l2= l2.next                
                else:
                    b_flag = False
            else:
                two=0
            
            
            self.insert(a,ssum(one,two,buf)[1] )
            buf = ssum(one,two,buf)[0]
           

        
        return a.next
            
