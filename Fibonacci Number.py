def fib(n):

    if n == 1:
        result = 1
        return result
    elif n == 2:
        result = 1
        return result
    elif n > 2:
        result = fib(n - 1) + fib(n - 2)
        return result

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))