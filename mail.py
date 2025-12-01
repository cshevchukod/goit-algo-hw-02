from queue import Queue

# створюємо чергу заявок
requests_queue = Queue()
request_id = 1


def generate_request():

    #Створює нову заявку та додає її в чергу.
  
    global request_id
    request = f"Request #{request_id}"
    request_id += 1

    requests_queue.put(request)
    print(f"[+] Додано заявку: {request}")


def process_request():

    #Видаляє заявку з черги та обробляє її.
    #Якщо черга порожня — виводить повідомлення.

    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Обробка: {request}")
    else:
        print("Черга порожня.")
        

def main():

    while True:
        generate_request()
        process_request()


if __name__ == "__main__":
    main()
