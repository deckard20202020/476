import queue
import heapq
import numpy as np
import math

from shapely.geometry import Polygon

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

    node = (1,2)

    newDistance = 0

    for i in range(len(min_heap)):
        if node == min_heap[i][1][0]:
             # gives me the entry in the heap
            # entry = min_heap[i]
            firstItem = newDistance
            secondItem = (node, newDistance)
            min_heap[i] = (firstItem, secondItem)
            heapq.heapify(min_heap)

    a = "is your heap sorted???"

    while min_heap:
        entry = heapq.heappop((min_heap))
        node = entry[1]
        node1 = node[0]
        print(node1)
        # print(heapq.heappop(min_heap))

def add_tuples(x, u):
    print(tuple(x + y for x, y in zip(x, u)))

def testingMatrix():
    mat1 = ([1, 6, 5], [3, 4, 8], [2, 12, 3])
    mat2 = ([3, 4, 6], [5, 6, 7], [6, 56, 7])
    res = np.dot(mat1, mat2)
    return res

def testingTan():
    a = math.pi/6
    print("This is the sin of theta")
    print(math.sin(a))
    print("This is the cos of theta")
    print(math.cos(a))


def buildTranslationMatrix(theta, x_t, y_t):

    matrix = ([math.cos(theta), -(math.sin(theta)), x_t],
              [math.sin(theta), math.cos(theta), y_t],
              [0, 0, 1])

    return matrix

def testingPolygon():

    # linkPositions = [[[-11.015777053157588, -0.8078712243462735], [0.9823952887191079, -1.0173001015936747], [1.0173001015936747, 0.9823952887191079], [-10.98087224028302, 1.191824165966509]], [[1.0173001015936745, 0.9823952887191092], [-10.98087224028302, 1.191824165966509], [-11.015777053157587, -0.8078712243462736], [0.9823952887191094, -1.0173001015936733]]]

    linkPositions = [[-1, 11], [1, 11], [1, 13], [-1, 13]]
    linkPositions = [[-1, 10], [1, 10], [1,12], [-1,12]]
    p1 = Polygon(linkPositions)
    obstacle = [[-1, 11], [1, 11], [1, 13], [-1, 13]]
    pO = Polygon(obstacle)

    doTheyIntersect = p1.intersects(pO)
    print(doTheyIntersect)

if __name__ == '__main__':
    # print_numbers_with_queue()
    # print_numbers_with_stack()
    # print_numbers_min_heap()
    # print_min_heap_with_distance()
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

    # matrix = testingMatrix()
    # print(matrix)

    # testingTan()
    # print()
    # matrix = buildTranslationMatrix(math.pi/6, 2, 3)
    # print(matrix)

    testingPolygon()


