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

def print_min_heap_with_distance():
    min_heap = []

    tuples = [((1, 2), 100), ((3, 4), 5), ((5, 6), 1), ((7, 8), 8), ((9, 10), 4)]
    # for t in tuples:
    #     heapq.heappush(min_heap, t)

    for t in tuples:
        heapq.heappush(min_heap, (t[1], t))

    while min_heap:
        print(heapq.heappop(min_heap))

def add_tuples(x, u):
    print(tuple(x + y for x, y in zip(x, u)))

if __name__ == '__main__':
    # print_numbers_with_queue()
    # print_numbers_with_stack()
    # print_numbers_min_heap()
    print_min_heap_with_distance()
    # t1 = (1,2)
    # t2 = (1, 2)
    # t3 = (1, 2, 3)
    # t4 = (1, 2, 3)
    # add_tuples(t1, t2)
    # add_tuples(t3, t4)

    # q = queue.Queue();
    # q.put((1,1))
    # q.put((1,2))
    # q.put((1,3))
    # while not q.empty():
    #     print(q.get())
    #
    # print()
    #
    # s = queue.LifoQueue()
    # s.put((2,1))
    # s.put((2, 2))
    # s.put((2, 3))
    # while not s.empty():
    #     print(s.get())
    #
    # print()
    #
    # pq = queue.PriorityQueue()
    # pq.put(3)
    # pq.put(2)
    # pq.put(1)
    # while not pq.empty():
    #     print(pq.get())


