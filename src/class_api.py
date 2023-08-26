from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class PlatformA(VacancyAPI):
    def connect(self):
        # Подключение к API платформы A
        pass

    def get_vacancies(self):
        # Получение вакансий с платформы A
        pass


class PlatformB(VacancyAPI):
    def connect(self):
        # Подключение к API платформы B
        pass

    def get_vacancies(self):
        # Получение вакансий с платформы B
        pass
