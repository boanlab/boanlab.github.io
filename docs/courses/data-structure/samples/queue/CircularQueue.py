class CircularQueue:

    def __init__(self,size):
        self.queue = list(0 for i in range(size))  ## 큐 사이즈 지정
        self.front = 0
        self.rear = 0
        self.size = size


    def printQueue(self):

        if self.isEmpty():
            print("큐가 비었습니다.")
            return

        else:

            i = self.front

            while True:

                i = (i+1) % self.size
                print(self.queue[i], end =" ")

                if(i==self.rear) or (i==self.front):
                    break
            print("\n")



    def isEmpty(self) -> bool : ## boolean 타입

        if self.front == self.rear:
            return True
        else:
            return False


    def isFull(self) -> bool:  ## boolean 타입

        if self.front == ((self.rear+1) % self.size):
            return True
        else:
            return False



    def enqueue(self, value):

        if self.isFull():
            print("큐가 가득찼습니다.")
            return
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):

        if self.isEmpty():
            print("큐가 비었습니다.")
            return

        else:
            self.front = (self.front + 1) % self.size
            result = self.queue[self.front]
            return result


if __name__ == '__main__':

    cirQueue = CircularQueue(5)

    cirQueue.printQueue() ## empty

    cirQueue.enqueue(1)         ## 1
    cirQueue.printQueue()

    cirQueue.enqueue(2)
    cirQueue.printQueue()       ## 1 2

    cirQueue.enqueue(3)
    cirQueue.printQueue()       ## 1 2 3

    cirQueue.enqueue(4)
    cirQueue.printQueue()       ## 1 2 3 4

    cirQueue.enqueue(5)
    cirQueue.printQueue()       ## full

    cirQueue.dequeue()
    cirQueue.printQueue()       ## 2 3 4

    cirQueue.dequeue()
    cirQueue.printQueue()       ## 3 4
