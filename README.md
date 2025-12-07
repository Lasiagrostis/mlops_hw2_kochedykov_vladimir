## Домашнее задание 2. Реализация /health и /predict эндпоинтов в gRPC-сервисе

### Цели задания:
- Освоить базовые принципы разработки и тестирования gRPC-сервисов;
- Научиться описывать контракты API в Protocol Buffers и генерировать Python-код;
- Уметь упаковать ML-модель в контейнер, настроить переменные окружения;
- Проверить работоспособность сервисов внутри Docker-контейнера.

### Инструкция по запуску
1. Клонируете репозиторий в рабочую директорию `git clone https://github.com/Lasiagrostis/mlops_hw2_kochedykov_vladimir.git`  
2. Создаёте докер - образ `docker build -t grpc-ml-service .`  
3. Поднимаете контейнер `docker run --name grpc_service -p 50051:50051 grpc-ml-service`  
4. Для проверки эндпоинтов запустите клиент `python -m client.client`  

### Примеры вывода команд
Создание образа и поднятие docker - контейнера  
![запуск контейнера](screenshots\docker_up.png)  
Проверка /health и /predict через запуск client.py из контейнера  
![запуск контейнера](screenshots\docker_check.png)  
