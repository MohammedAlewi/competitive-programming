class LinkedListNode:
    def __init__(self,val):
        self.val=val
        self.next = None

def has_cycle(head):
    seen = set()

    while head!= None:
        if head in seen:
            return True
        seen.add(head)
        head=head.next
        
    return False


def main():
    head = LinkedListNode(12);
    head.next= LinkedListNode(13)
    head.next.next=head

    return has_cycle(head)

if __name__ == "__main__":
    main()
