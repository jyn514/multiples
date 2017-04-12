def fibonacci(n, *option, **kwarg):
    t,a,b=0,0,1
    if ((kwarg=={}) and (option==())):
        while  t<n:
            a,b=b,a+b
            t+=1
        print(a)
    elif ('all' in option):
        while  t<n:
            print(a)
            a,b=b,a+b
            t+=1
        print(a)
    else:
        print("You entered an option that is not available.\nOptions: 'all'")
    
