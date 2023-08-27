from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    def get_vacancies_from_hh(self):
    # Логика получения вакансий с hh
    res = requests.get("https://api.hh.ru/vacancies", params={"text": "python"})
    print(res.json()["items"])

    def connect_to_superjob(self):
        # Логика подключения к API superjob
        print("Connected to Platform B")

    def get_vacancies_from_superjob(self):
        headers = {"X-Api-App-Id": os.environ["SUPERJOB_API_KEY"]}
        requests.get("https://api.superjob.ru/2.0/vacancies/", headers=headers, params={"keywords": "python"})
        print(res.json()["objects"])


class HH(VacancyAPI):
    # hh.ru
    def __init__(self, api):
        self.api = api

    def connect(self):
        self.api.connect_to_hh()

    def get_vacancies(self):
        return self.api.get_vacancies_from_hh()


class Superjob(VacancyAPI):
    # superjob
    def __init__(self, api):
        self.api = api

    def connect(self):
        self.api.connect_to_superjob()

    def get_vacancies(self):
        return self.api.get_vacancies_from_superjob()


# API для сайтов
hh = "https://api.hh.ru/"
sj = "https://api.superjob.ru/:version/method_name/:params"
HH = HH(hh)
Superjob = Superjob(sj)
