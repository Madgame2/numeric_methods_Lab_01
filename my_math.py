from decimal import Decimal, getcontext

getcontext().prec = 50

def bisection_method (f,a,b,tol=1e-6,max_iter=100):
    if f(a)*f(b)>=0:
        raise ValueError("Метод бисекции не применим: f(a) и f(b) должны иметь разные знаки.")

    for _ in range(max_iter):
        c=(a+b)/2

        if abs(f(c)) <tol:
            return c
        elif f(a)*f(c) <0:
            b=c
        else:
            a=c

    return (a+b)/2

def Newton_method(f, f_prime, x0,tol=1e-6,max_iter=100):
    x=x0
    for _ in range(max_iter):
        fx=f(x)
        fpx=f_prime(x)

        if abs(fx)<tol:
            return x

        if fpx ==0:
            raise ValueError("Производная функции равна нулю. Метод Ньютона не применим.")

        x=x-fx/fpx

    return x

def simple_iteration(phi, x0, epsilon=1e-6, max_iterations=100):

    x_prev = x0
    for _ in range(max_iterations):
        x_next = phi(x_prev)
        if abs(x_next - x_prev) < epsilon:
            return x_next
        x_prev = x_next
    return x_prev  # Возвращаем последнее приближение, если не сошлось