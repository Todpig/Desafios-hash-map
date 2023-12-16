import threading
import time
import random


class Sensor:
    def __init__(self, sensor_id, leituras):
        self.id = sensor_id
        self.leituras = leituras

    def __str__(self):
        return f"Sensor {self.id}\nLeituras {self.leituras}"

    def add_leitura(self, leitura):
        self.leituras.append(leitura)


class SensorData:
    def __init__(self, sensor_id, timestamp, value):
        self.id = sensor_id
        self.timestamp = timestamp
        self.value = value

    def __str__(self):
        return f"Sensor {self.id} - Timestamp: {self.timestamp} - Value: {self.value}"


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.lock = threading.Lock()

    def hash(self, sensor_id):
        return hash(sensor_id) % self.tamanho

    def inserir(self, dados):
        key = self.hash(dados.id)
        with self.lock:
            if self.tabela[key] is None:
                self.tabela[key] = [dados]
            else:
                self.tabela[key].append(dados)

    def buscar(self, sensor_id):
        key = self.hash(sensor_id)
        with self.lock:
            return self.tabela[key]

    def __str__(self):
        return str(self.tabela)


def process_sensor_data(sensor, tabela_hash, qtd):
    for _ in range(qtd):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        value = random.uniform(20.0, 30.0)
        data = SensorData(sensor.id, timestamp, value)

        tabela_hash.inserir(data)
        time.sleep(random.uniform(1, 3))


if __name__ == "__main__":
    tamanho_tabela_hash = int(input("Digite o tamanho da tabela hash: "))
    qtd = int(input("Digite a quantidade de dados a serem inseridos: "))

    tabela_hash = TabelaHash(tamanho_tabela_hash)
    threads = []
    sensores = []

    sensor1 = Sensor(1, [])
    sensor1.add_leitura(10)
    sensor2 = Sensor(2, [])
    sensor2.add_leitura(20)
    sensor3 = Sensor(3, [])
    sensor3.add_leitura(30)

    sensores.extend([sensor1, sensor2, sensor3])

    for sensor in sensores:
        thread = threading.Thread(
            target=process_sensor_data, args=(sensor, tabela_hash, qtd))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for sensor in sensores:
        print(sensor)

    print(tabela_hash)
