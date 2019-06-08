import math
import threading
from multiprocessing import Process, Pool
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta


def checkNumber(numberToCheck, localNumberList):
    for number in localNumberList:
        if (number % numberToCheck == 0) and (number != numberToCheck):
            localNumberList.remove(number)

def eratosthenesSieveParallel(numberList, highestNumberToCheck):
    localNumberList = numberList

    numberIndex = 0

    # Grabs the first number
    numbertoCheck = localNumberList[numberIndex]

    while numbertoCheck <= highestNumberToCheck:

        if (len(localNumberList) <= numberIndex):
            break

        numbertoCheck = localNumberList[numberIndex]
        numbertoCheck2 = localNumberList[numberIndex]
        numbertoCheck3 = localNumberList[numberIndex]
        numbertoCheck4 = localNumberList[numberIndex]

        listLength = len(localNumberList)
        chunkSize = listLength // 4

        splitList1 = localNumberList[:chunkSize]
        splitList2 = localNumberList[chunkSize:chunkSize * 2]
        splitList3 = localNumberList[chunkSize * 2:chunkSize * 3]
        splitList4 = localNumberList[chunkSize * 3:]

        thread1 = threading.Thread(target=checkNumber, args=[numbertoCheck, splitList1])
        thread2 = threading.Thread(target=checkNumber, args=[numbertoCheck2, splitList2])
        thread3 = threading.Thread(target=checkNumber, args=[numbertoCheck3, splitList3])
        thread4 = threading.Thread(target=checkNumber, args=[numbertoCheck4, splitList4])

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()

        localNumberList = splitList1 + splitList2 + splitList3 + splitList4

        numberIndex += 1

    return localNumberList


def eratosthenesSieve(numberList, highestNumberToCheck):
    localNumberList = numberList

    numberIndex = 0

    # Grabs the first number
    numbertoCheck = localNumberList[numberIndex]

    while numbertoCheck <= highestNumberToCheck:

        if (len(localNumberList) <= numberIndex):
            break

        numbertoCheck = localNumberList[numberIndex]

        checkNumber(numbertoCheck, localNumberList)

        numberIndex += 1

    return localNumberList


def isPrime(number, sieveFunction):
    startingTime = timer()

    # Grab the highest number to check
    highestNumberToCheck = math.floor(math.sqrt(number))

    if number == 1:
        return False

    if number in [2, 3]:
        return True

    # Creates the list
    numberList = list(range(2, highestNumberToCheck + 1))

    primesToCheck = sieveFunction(numberList, highestNumberToCheck)

    endingTime = timer()
    print('It took this ammount of time:', timedelta(seconds=endingTime - startingTime))

    for prime in primesToCheck:
        if (number % prime == 0):
            return False

    return True



if __name__ == '__main__':
    isPrime(1000000087, eratosthenesSieveParallel)

