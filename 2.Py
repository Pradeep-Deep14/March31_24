def func(x,y=[]):
    for i in range(x):
        y.append(i*i)
    print(y)

func(3,[3,2,1])