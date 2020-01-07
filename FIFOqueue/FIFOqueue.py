#Python program to print the FIFO queue
import queue
q = queue.Queue()

#insert items at the end of the queue 
y=int(input("Enter the queue: "))
for x in range(y):
    q.put(str(x))

#remove items from the head of the queue 
while not q.empty():
    print(q.get(), end=" ")
print()
