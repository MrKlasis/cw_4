import json


class JSONVacancyFile(VacancyFile):
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        # Добавление вакансии в JSON-файл
        pass

    def get_vacancies(self, criteria):
        # Получение данных из JSON-файла по указанным критериям
        pass

    def remove_vacancy(self, vacancy):
        # Удаление информации о вакансии из JSON-файла
        pass
