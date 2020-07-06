from heapq import heappush, heappop

heap = []
item_lookup = set()

def push(val):
    heappush(heap, val)
    item_lookup.add(val)

def discard(val):
    item_lookup.discard(val)

def print_min():
    while heap[0] not in item_lookup:
        heappop(heap)
    print(heap[0])

cmds = {
    1: push,
    2: discard,
    3: print_min
}

n = int(input())

for _ in range(n):
    data = list(map(int, input().split()))
    cmds[data[0]](*data[1:])