import json


def criteria_matches(vacancy, criteria):
    # логика для сравнения критериев с вакансией и возвращения соответствующего результата

    if vacancy == "Software Engineer" and criteria == "Python":
        return True
    elif vacancy == "Data Analyst" and criteria == "SQL":
        return True
    else:
        return False


class JSONVacancyFile:
    def __init__(self, filename):
        self.filename = filename

    def add_vacancy(self, vacancy):
        with open(self.filename, 'a') as file:
            json.dump(vacancy, file)
            file.write('\n')

    def get_vacancies(self, criteria):
        vacancies = []
        with open(self.filename, 'r') as file:
            for line in file:
                vacancy = json.loads(line)
                if criteria_matches(vacancy, criteria):
                    vacancies.append(vacancy)
        return vacancies

    def remove_vacancy(self, vacancy):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        with open(self.filename, 'w') as file:
            for line in lines:
                existing_vacancy = json.loads(line)
                if existing_vacancy != vacancy:
                    file.write(line)

