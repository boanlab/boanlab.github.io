class queueArray:

    def __init__(self,size):
        self.queue = list(0 for i in range(size)) ## 큐 사이즈 지정
        self.front = -1
        self.rear = -1
        self.size = size

    def printQueue(self):

        for i in range(0,self.size):
            if (i<=self.front) or (i > self.rear):
                print(" ")
            else:
                print(self.queue[i], end=' ')

        print("\n")


    def isEmpty(self):

        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):

        if self.rear == (self.size - 1):
            return True
        else :
             return False

    def enqueue(self,value):
        if self.isFull():
            print("큐가 가득찼습니다.")
            return
        else:
            self.rear = self.rear + 1
            self.queue[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("큐가 비었습니다.")
            return

        else:
            self.front = self.front + 1
            result = self.queue[self.front]
            return result


if __name__ == '__main__':

    queue = queueArray(5)

    queue.enqueue(1)
    queue.printQueue()  ## 1

    queue.enqueue(2)
    queue.printQueue()  ## 1 2

    queue.enqueue(3)
    queue.printQueue()  ## 1 2 3

    queue.enqueue(4)
    queue.printQueue()  ## 1 2 3 4

    queue.enqueue(5)
    queue.printQueue()  ## 1 2 3 4 5

    queue.enqueue(6)
    queue.printQueue()  ## full

    queue.dequeue()
    queue.printQueue()  ## 2 3 4 5

