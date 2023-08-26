from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


def connect_to_platform_a():
    # Логика подключения к API платформы A
    print("Connected to Platform A")


class MyVacancyAPI:
    hh = "https://api.hh.ru/"
    sj = "https://api.superjob.ru/:version/method_name/:params"

    platform_a = PlatformA(hh)
    platform_b = PlatformB(sj)

    def get_vacancies_from_platform_a(self):
        # Логика получения вакансий с платформы A
        vacancies = [
            {"title": "Job A1", "link": "https://example.com/job-a1", "salary": 50000,
             "description": "Description A1"},
            {"title": "Job A2", "link": "https://example.com/job-a2", "salary": 60000,
             "description": "Description A2"},
            {"title": "Job A3", "link": "https://example.com/job-a3", "salary": 55000,
             "description": "Description A3"}
        ]
        return vacancies

    def connect_to_platform_b(self):
        # Логика подключения к API платформы B
        print("Connected to Platform B")

    def get_vacancies_from_platform_b(self):
        # Логика получения вакансий с платформы B
        vacancies = [
            {"title": "Job B1", "link": "https://example.com/job-b1", "salary": 45000,
             "description": "Description B1"},
            {"title": "Job B2", "link": "https://example.com/job-b2", "salary": 65000,
             "description": "Description B2"},
            {"title": "Job B3", "link": "https://example.com/job-b3", "salary": 52000,
             "description": "Description B3"}
        ]
        return vacancies


class PlatformA(VacancyAPI):
    #hh.ru
    def __init__(self, api):
        self.api = api

    def connect(self):
        self.api.connect_to_platform_a()

    def get_vacancies(self):
        return self.api.get_vacancies_from_platform_a()


class PlatformB(VacancyAPI):
    #superjob
    def __init__(self, api):
        self.api = api

    def connect(self):
        self.api.connect_to_platform_b()

    def get_vacancies(self):
        return self.api.get_vacancies_from_platform_b()




