class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head

def merge_sorted_linked_lists(head1, head2):
    dummy = Node()
    tail = dummy
    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    tail.next = head1 or head2
    return dummy.next

def insertion_sort_linked_list(head):
    dummy = Node()
    current = head
    while current:
        prev = dummy
        next_node = current.next
        while prev.next and prev.next.data < current.data:
            prev = prev.next
        current.next = prev.next
        prev.next = current
        current = next_node
    return dummy.next

# Створення початкового списку (1, 6, 4, 2, 3, 5)
head = Node(1)
head.next = Node(6)
head.next.next = Node(4)
head.next.next.next = Node(2)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(5)

print("Початковий список:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Реверсування однозв'язного списку
head = reverse_linked_list(head)
print("\nРезультат реверсування:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Сортування списку
head = insertion_sort_linked_list(head)
print("\nРезультат сортування:")
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Створення другого відсортованого списку (7, 8, 9)
head2 = Node(7)
head2.next = Node(8)
head2.next.next = Node(9)

# Об'єднання двох відсортованих списків
merged_head = merge_sorted_linked_lists(head, head2)
print("\nРезультат об'єднання відсортованих списків:")
current = merged_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
