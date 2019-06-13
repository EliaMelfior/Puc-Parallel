import math
import multiprocessing as mp
from timeit import default_timer as timer
from datetime import timedelta

class Number:
    prime = False
    number = 0
    serialTime = 0
    parallelTime = 0

    def __init__(self):
        self.menu()

    def clearScreen(self):
        print ('\n' * 100)

    def menu(self):
        task = 0

        while (task != '2'):
            if (self.prime):
                print ('The number:', self.number, 'is prime.')
            else:
                print ('The number:', self.number, 'is not prime.')

            print ('It took this ammount of time to check the primality using the serial function: \n', self.serialTime, )
            print ('It took this ammount of time to check the primality using the parallel function: \n', self.parallelTime, '\n')

            print ('1 - Initialize a number')
            print ('2 - Finish the program', '\n')
            task = input('Choose an option: ')

            if (task == '1'):
                self.clearScreen()
                number = input('Write the number that will be selected: \n \n')
                self.number = int(number, 10)
                self.primalityTest(parallel = True)
                self.primalityTest(parallel = False)

    def primalityTest(self, parallel):
        startingTime = timer()

        if (parallel == True):
            print('Checking if the number', self.number ,'is prime, using parallelization.', '\n')
            self.prime = self.isPrime(self.eratosthenesSieveParallel)
            endingTime = timer()
            self.parallelTime = timedelta(seconds=endingTime - startingTime)

        else:
            print('Checking if the number', self.number ,'is prime, using serialization.', '\n')
            self.prime = self.isPrime(self.eratosthenesSieve)
            endingTime = timer()
            self.serialTime = timedelta(seconds=endingTime - startingTime)


    def isPrime(self, sieveFunction):
        # Grab the highest number to check
        highestNumberToCheck = math.floor(math.sqrt(self.number))

        if self.number == 1:
            return False

        if self.number in [2, 3]:
            return True

        # Creates the list
        numberList = list(range(2, highestNumberToCheck + 1))

        primesToCheck = sieveFunction(numberList, highestNumberToCheck)

        for prime in primesToCheck:
            if (self.number % prime == 0):
                return False

        return True

    def checkNumber(self, params):
        numberToCheck, localNumberList = params
        for number in localNumberList:
            if (number % numberToCheck == 0) and (number != numberToCheck):
                localNumberList.remove(number)

        return localNumberList

    def eratosthenesSieve(self, numberList, highestNumberToCheck):
        localNumberList = numberList

        numberIndex = 0

        # Grabs the first number
        numbertoCheck = localNumberList[numberIndex]

        while numbertoCheck <= highestNumberToCheck:

            if (len(localNumberList) <= numberIndex):
                break

            numbertoCheck = localNumberList[numberIndex]

            self.checkNumber([numbertoCheck, localNumberList])

            numberIndex += 1

        return localNumberList

    def eratosthenesSieveParallel(self, numberList, highestNumberToCheck):
        localNumberList = numberList

        numberIndex = 0

        pool = mp.Pool(mp.cpu_count())

        # Grabs the first number
        numbertoCheck = localNumberList[numberIndex]

        while numbertoCheck <= highestNumberToCheck:

            if (len(localNumberList) <= numberIndex):
                break

            numbertoCheck = localNumberList[numberIndex]

            listLength = len(localNumberList)
            chunkSize = listLength // 4

            splitList1 = localNumberList[:chunkSize]
            splitList2 = localNumberList[chunkSize:chunkSize * 2]
            splitList3 = localNumberList[chunkSize * 2:chunkSize * 3]
            splitList4 = localNumberList[chunkSize * 3:]

            numbersToCheck = [numbertoCheck, numbertoCheck, numbertoCheck, numbertoCheck]
            dataToCheck = [splitList1, splitList2, splitList3, splitList4]

            localNumberList1, localNumberList2, localNumberList3, localNumberList4 = pool.map(self.checkNumber,
                                                                                              zip(numbersToCheck,
                                                                                                  dataToCheck))
            localNumberList1.extend(localNumberList2)
            localNumberList1.extend(localNumberList3)
            localNumberList1.extend(localNumberList4)
            localNumberList = localNumberList1

            numberIndex += 1

        return localNumberList


if __name__ == '__main__':
    #prime numbers to Test - 1033 / 1000081 / 1000000087 / 10000000097 / 100000000069
    number = Number()
