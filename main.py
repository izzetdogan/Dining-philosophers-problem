from threading import Thread, Lock
import random
import time
import os
from math import *


class DiningPhilosophers:
    def __init__(self, number_of_philosophers, meal_size=9):
        self.meals = [meal_size for _ in range(number_of_philosophers)]
        self.chopsticks = [Lock() for _ in range(number_of_philosophers)]
        self.status = ['  T  ' for _ in range(number_of_philosophers)]
        self.chopstick_holders = ['     ' for _ in range(number_of_philosophers)]
        self.count=0
    def philosopher(self, i):
        j = (i+1) % 5
        while self.meals[i] > 0:
            self.status[i] = ' T'
            time.sleep(random.random())
            self.status[i] = '-T'
            if not self.chopsticks[i].locked():
                self.chopsticks[i].acquire()
                self.chopstick_holders[i] = ' /   '
                time.sleep(random.random())
                if not self.chopsticks[j].locked():
                    self.chopsticks[j].acquire()
                    self.chopstick_holders[i] = ' / \\ '
                    self.status[i] = '-E-'
                    time.sleep(random.random())
                    self.meals[i] -= 1
                    self.chopsticks[j].release()
                    self.chopstick_holders[i] = '     '
                    self.chopsticks[i].release()
                    self.chopstick_holders[i] = '     '
                    self.status[i] = ' T'
                else:
                    self.chopsticks[i].release()
                    self.chopstick_holders[i] = '     '

                
#-------------------------------------------------------         


def main():
    n = 5
    m = 9
    dining_philosophers = DiningPhilosophers(n, m)
    philosophers = [Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(n)]
    for philosopher in philosophers:
        philosopher.start()
    while sum(dining_philosophers.meals) > 0:
        os.system('cls')

        count=1
        print("\n",int(n+n/2)*" ",dining_philosophers.status[0])
        print(" ",int(n+n/2)*" ",dining_philosophers.meals[0])
        
        kontrol=False
        if (n%2==0):
            kontrol=True
        if kontrol==True:
            check=int((n-1)/2)+1
        else:
            check=int((n-1)/2)


        for i in range(n-1,check,-1):
            print((abs(count-ceil(check/2)))*"   ",dining_philosophers.status[i],(abs(check-(abs(count-ceil(check/2)))))*"      ", dining_philosophers.status[count])
            print('',(abs(count-ceil(check/2)))*"   ",dining_philosophers.meals[i],"",(abs(check-(abs(count-ceil(check/2)))))*"      ", dining_philosophers.meals[count])
            print()
            count+=1
        if kontrol==True:
            print("",int(n+n/2)*" ",dining_philosophers.status[n-1])
            print(" ",int(n+n/2)*" ",dining_philosophers.meals[n-1])





# ---------------------------------------------------------
        print("Number of eating philisophers:",str(dining_philosophers.status.count('-E-')) ,"/",n )
        print("Number of locked chopsticks:", 2* dining_philosophers.status.count('-E-')+dining_philosophers.status.count('-T') ,"/", n)
        print("Meals left  : ",str(sum(dining_philosophers.meals)),"/ ", n*m)

#-----------------------------
        time.sleep(0.1)
    for philosopher in philosophers:
        philosopher.join()


if __name__ == "__main__":
    main()