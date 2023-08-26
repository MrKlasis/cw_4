from abc import ABC, abstractmethod


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def validate(self):
        # Валидация данных вакансии
        pass

    def __eq__(self, other):
        # Метод сравнения вакансий по зарплате
        pass

    def __lt__(self, other):
        # Метод сравнения вакансий для сортировки
        pass


class VacancyFile(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy):
        pass
