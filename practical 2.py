def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_till_n(n):
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    return primes

def generate_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main():
    n = int(input("Enter a number 'n': "))

    # Check if 'n' is prime
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

    # Generate all prime numbers till 'n'
    primes_till_n = generate_primes_till_n(n)
    print(f"Prime numbers till {n}: {primes_till_n}")

    # Generate first 'n' prime numbers
    first_n_primes = generate_first_n_primes(n)
    print(f"First {n} prime numbers: {first_n_primes}")

if __name__ == "__main__":
    main()
