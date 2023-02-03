import queue
import heapq

def print_numbers_with_queue():
    q = queue.Queue()

    for i in range(1, 11):
        q.put(i)

    while not q.empty():
        print(q.get())

def print_numbers_with_stack():
    stack = []

    for i in range(10, 0, -1):
        stack.append(i)

    while stack:
        print(stack.pop())

def print_numbers_min_heap():
    min_heap = []

    heapq.heappush(min_heap, 10)
    heapq.heappush(min_heap, 5)
    heapq.heappush(min_heap, 9)
    heapq.heappush(min_heap, 4)
    heapq.heappush(min_heap, 8)
    heapq.heappush(min_heap, 3)
    heapq.heappush(min_heap, 7)
    heapq.heappush(min_heap, 2)
    heapq.heappush(min_heap, 6)
    heapq.heappush(min_heap, 1)


    while min_heap:
        print(heapq.heappop(min_heap))

if __name__ == '__main__':
    print_numbers_with_queue()
    print_numbers_with_stack()
    print_numbers_min_heap()
