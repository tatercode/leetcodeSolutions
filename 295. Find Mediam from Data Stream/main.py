import heapq

# Small Heap is the max heap
# Large heap is the min heap


class MedianFinder:
    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        if self.largeHeap and num > self.largeHeap[0]:
            heapq.heappush(self.largeHeap, num)
        else:
            heapq.heappush(self.smallHeap, -1 * num)

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            add = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, add)
        elif len(self.largeHeap) > len(self.smallHeap) + 1:
            add = heapq.heappop(self.largeHeap) 
            heapq.heappush(self.smallHeap, -1*add)

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            return (-1*self.smallHeap[0] + self.largeHeap[0]) / 2.0
        elif len(self.smallHeap) > len(self.largeHeap):
            return -1*self.smallHeap[0]
        else:
            return self.largeHeap[0]

def main():
    sol = MedianFinder()
    sol.addNum(1)
    sol.addNum(2)
    ans = []
    ans.append(sol.findMedian())
    sol.addNum(3)
    ans.append(sol.findMedian())
    print(ans)

if __name__ == "__main__":
    main()
