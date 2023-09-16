# from https://www.educative.io/answers/how-to-implement-a-queue-in-python
# implementing a queue using a List

if __name__ == '__main__':

    q = []
    q.append(4)
    q.append(8)
    q.append(12)
    q.append(17)
    print("Initial Queue is:", q)
    print("The first item in the queue is: ", q.pop(0))
    print("The next item in the queue is:  ", q.pop(0))
    print("The next item in the queue is:  ", q.pop(0))

    print("After Removing the first 3 elements, the queue is now:", q)