def sleep_in():
    assert sleep_in(False, False) == True	
    assert sleep_in(True, False) == False
    assert sleep_in(False, True) == True	
    assert sleep_in(True, True) == True

def monkey_trouble():
    assert monkey_trouble(True, True) == True
    assert monkey_trouble(False, False) == True	
    assert monkey_trouble(True, False) == False
    assert monkey_trouble(False, True) == False 

def sum_double():
    assert sum_double(1, 2) == 3
    assert sum_double(3, 2) == 5
    assert sum_double(2, 2) == 8	
    assert sum_double(-1, 0) == -1
    assert sum_double(3, 3) == 12	
    assert sum_double(0, 0) == 0
    assert sum_double(0, 1) == 1
    assert sum_double(3, 4) == 7

def diff21():
    assert diff21(19) == 2
    assert diff21(10) == 11
    assert diff21(10) == 11
    assert diff21(21) == 0	
    assert diff21(22) == 2
    assert diff21(25) == 8	
    assert diff21(30) == 18	
    assert diff21(0) == 21
    assert diff21(1) == 20
    assert diff21(2) == 19	
    assert diff21(-1) == 22		
    assert diff21(-2) == 23
    assert diff21(50) == 58

def string_times():
    assert string_times('Hi', 2) == 'HiHi'
    assert string_times('Hi', 3) == 'HiHiHi'
    assert string_times('Hi', 1) == 'Hi'
    assert string_times('Hi', 0) == ''	
    assert string_times('Hi', 5) == 'HiHiHiHiHi'
    assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
    assert string_times('x', 4) == 'xxxx'
    assert string_times('', 4) == ''
    assert string_times('code', 2) == 'codecode'
    assert string_times('code', 3) == 'codecodecode'

def front_times():
    assert front_times('Chocolate', 2) == 'ChoCho'
    assert front_times('Chocolate', 3) == 'ChoChoCho'	
    assert front_times('Abc', 3) == 'AbcAbcAbc'
    assert front_times('Ab', 4) == 'AbAbAbAb'
    assert front_times('A', 4) == 'AAAA'
    assert front_times('', 4) == ''
    assert front_times('Abc', 0) == ''
