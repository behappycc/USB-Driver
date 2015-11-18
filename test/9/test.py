import itertools
import numpy as np

a = np.array([1, 2, 3, 4])
print a + a

def dedupe():
    b = [1, 2, 3, 1]
    d = 1
    listNum = []
    for number in b:
        if number not in listNum:
            listNum.append(number)
        else:
            return number

def nextSeq(number):
    return ''.join('%s%s' % (len(list(group)), digit) 
        for digit, group in itertools.groupby(str(number)))

def seqGenerator(max):
    n, seq = 0, 1
    while n < max :
        yield seq
        seq = nextSeq(seq)
        n += 1

class Student:  
        def __init__(self, name, grade, age):  
                self.name = name  
                self.grade = grade  
                self.age = age  
        def __repr__(self):  
                return repr((self.name, self.grade, self.age)) 

def testSort():
    a = [2, 4, 3, 5, 1]
    sorted(a)
    print a

    student_objects = [  
            Student('john', 'A', 15),  
            Student('jane', 'B', 12),  
            Student('dave', 'B', 10),  
    ]  
  
    a = sorted(student_objects, key=lambda student: student.age)  
    print a

def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1

def fab(n):
    if n >1 :
        return fab(n -1) + fab(n - 2)
    else:
        return 1

def main():
    ans = dedupe()
    print ans

    for seq in seqGenerator(5):
        print seq

    testSort()
    print fact(3)
    print fab(5)

if __name__ == '__main__':
    main()


