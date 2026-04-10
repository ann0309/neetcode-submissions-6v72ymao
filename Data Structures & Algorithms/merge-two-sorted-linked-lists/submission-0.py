# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #corner case
        #其中一個是空的
        if not list1: #list1為空
            return list2
        elif not list2: 
            return list1
        else:
            pass

        #dummy_res 是結果array的head, 但是是個空的 是個假的 想像它是一個掛勾而已
        # curr是用來移動的ptr
        #curr是多少 dummy 就會是多少
        dummy_res=curr=ListNode() #用來接我的output
       
        # dummy_res.val=2
        # curr.val=3
        # print(dummy_res.val,curr.val)

        while list1 and list2 :
            if list1.val<=list2.val: #list1 比list2的值大
                curr.next=list1
                list1=list1.next
                curr=curr.next
            elif list1.val>=list2.val:
                curr.next=list2
                list2=list2.next
                curr=curr.next
        
        # 以下把剛剛的都洗掉了
        if list1: 
            curr.next=list1
        if list2: #list2還有東西
            curr.next=list2
        return dummy_res.next



