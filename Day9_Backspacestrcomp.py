class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l=0
        temphead=head
        while head:
            l+=1
            head=head.next
        if l%2==0:
            mid=int(l/2)+1
        else:
            mid= int((l+1)/2)
        i=1
        
        while temphead:
            #print(temphead.val,i,mid)
            if i==mid:
                return temphead
            else:
                i+=1
                #print(temphead.val,i)
                temphead=temphead.next
            
            
        
