import sys
import importlib
import random
import time



def test(n, algo):
    array = random.sample(range(1,n+1),n)
    py_sort = sorted(array)
    then = time.time()
    my_sort = algo.sort(array)
    now = time.time()
    correct = False
    if my_sort==py_sort:
        correct = True
    return now-then,correct



def main():
    if len(sys.argv)==1:
        sys.argv.append("template.py")
    to_test = sys.argv[1:]
    for testing in to_test:
        a = importlib.import_module(testing[:-3])
        for x in range(7):
            cur_n = 10**(x)
            print "Testing "+str(testing[:-2])+" for n= "+str(cur_n)
            time,correct = test(cur_n, a)
            print "Correct = "+str(correct)+"\nElapsed Time = "+str(time)
            print ""






if __name__=="__main__":
    main()
