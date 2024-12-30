import threading

def factorial_partial(start, end, result):
    partial_result = 1
    for i in range(start, end + 1):
        partial_result *= i
    result.append(partial_result)

def calculate_factorial(number, num_threads):
    result = []
    threads = []
    step = number // num_threads
    start = 1
    end = step

    for _ in range(num_threads):
        thread = threading.Thread(target=factorial_partial, args=(start, end, result))
        threads.append(thread)
        thread.start()

        start = end + 1
        end = start + step - 1 if end + step <= number else number

    for thread in threads:
        thread.join()

    final_result = 1
    for partial_result in result:
        final_result *= partial_result

    return final_result

if __name__ == "__main__":
    number_to_factorial = 5
    num_threads = 2

    result = calculate_factorial(number_to_factorial, num_threads)
    print(f"Giai thừa của {number_to_factorial} là {result}")
