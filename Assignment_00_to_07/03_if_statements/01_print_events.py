import time

def main():
    print("This program generates numbers divisible by 2 (limit: 20 numbers)")
    count = 0
    num = 0
    while count < 20:
        if num % 2 == 0:
            print(num)
            count += 1
            time.sleep(0.1)  
        num += 1


if __name__ == "__main__":
    main()