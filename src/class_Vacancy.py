from abc import ABC, abstractmethod


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def validate(self):
        # Валидация данных вакансии
        if not isinstance(self.title, str):
            raise ValueError("Title must be a string")
        if not isinstance(self.link, str):
            raise ValueError("Link must be a string")
        if not isinstance(self.salary, (int, float)):
            raise ValueError("Salary must be a number")
        if not isinstance(self.description, str):
            raise ValueError("Description must be a string")

    def __eq__(self, other):
        # Метод сравнения вакансий по зарплате
        return self.salary == other.salary

    def __lt__(self, other):
        # Метод сравнения вакансий для сортировки
        return self.salary < other.salary


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
