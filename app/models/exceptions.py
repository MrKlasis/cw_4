class FileNotFoundExceptions(Exception):
    def __init__(self):
        self.message = "Файл с данными не найден"

