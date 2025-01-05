# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
    def addTwoNumbers(self, l1, l2):
        dummy_linked_list = ListNode()
        carry = 0
        current = dummy_linked_list
        while(l1 != None or l2 != None or carry == 1):
            addition = 0
            addition = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if (addition > 9):
                addition = addition - 10
                carry = 1
            else:
                carry = 0
            # print(f"addition is",addition)
            # print(f"carry is",carry)
            current.next = ListNode(addition)
            current = current.next 
            # print(current.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None   
        return dummy_linked_list.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        

        Node=ListNode()
        s=l1.val+l2.val
        if s>=10:
            carry=1
            s=s%10
        print(s)
        Node.val=s
        l1=l1.next
        l2=l2.next

        start=Node
        while l1 and l2:
            s=l1.val+l2.val+carry
            if s>=10:
                carry=1
                s=s%10
            else:
                carry=0
            Node.next=ListNode(s)
            Node=Node.next
            l1=l1.next
            l2=l2.next

        
        while l1:
            s=l1.val
            if carry:
                s=l1.val+carry
                if s>=10:
                    carry=1
                    s=s%10
                else:
                    carry=0
            Node.next=ListNode(s)
            Node=Node.next
            l1=l1.next

        while l2:
            s=l2.val
            if carry:
                s=l2.val+carry
                if s>=10:
                    carry=1
                    s=s%10
                else:
                    carry=0
            
            Node.next=ListNode(s)
            Node=Node.next
            l2=l2.next
            
        if carry:
            Node.next=ListNode(1)

        return start














        # num1=0
        # num2=0
        # count=0
        # while l1:
        #     num1+=(l1.val*(10**count))
        #     l1=l1.next
        #     count+=1

        # count=0
        # while l2:
        #     num2+=l2.val*(10**count)
        #     l2=l2.next
        #     count+=1

        # sums=str(num1+num2)
        # print(sums)
        # s=num1+num2
        # arr=[]

        # for i in range(len(sums)):
        #     dif=s%10**(i+1)
        #     s-=dif

        #     arr.append(int(dif/(10**i)))

        # head=ListNode(arr[0])
        # temp=head
        # for i in range(1,len(arr)):
        #     head.next=ListNode(arr[i])
        #     head=head.next
        # return temp
            


