def summ(args, *vartuple):
    result = args


    for i in vartuple:
        result += i

    print(result)

summ(2,4,5,7,3,0,3,6,0)
print(summ)
