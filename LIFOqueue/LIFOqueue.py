#Python program to print the LIFO queue
import queue
q = queue.LifoQueue()

#insert items at the head of the queue 
y=int(input("Enter the queue: "))
for x in range(y):
    q.put(str(x))

#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print()

