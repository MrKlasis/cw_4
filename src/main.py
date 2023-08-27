from src.class_api import HH, Superjob
from src.class_file import JSONVacancyFile


def main():
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    hh_engine = HH(keyword)
    sj_engine = Superjob(keyword)
    connector = JSONVacancyFile("vacancy.json")

    HH.connect()
    HH.get_vacancies()

    Superjob.connect()
    Superjob.get_vacancies()

    while True:
        command = input("Введите команду (sort, top, search): ")
        if command == "sort":
            # выполни сортировку
            sorted_hh_vacancies = sorted(hh_vacancies, key=lambda x: x["salary"])
            sorted_sj_vacancies = sorted(sj_vacancies, key=lambda x: x["salary"])
            print("Сортировка выполнена.")
        elif command == "top":
            # выполни сортировку по самой высокой оплате
            sorted_hh_vacancies = sorted(hh_vacancies, key=lambda x: x["salary"], reverse=True)
            sorted_sj_vacancies = sorted(sj_vacancies, key=lambda x: x["salary"], reverse=True)
            print("Сортировка по самой высокой оплате выполнена.")
        elif command == "search":
            # внести параметры поиска по ключевым словам
            keywords = input("Введите ключевые слова для поиска: ")
            # выполнить поиск по параметрам
            filtered_hh_vacancies = [v for v in hh_vacancies if keywords in v["title"]]
            filtered_sj_vacancies = [v for v in sj_vacancies if keywords in v["title"]]
            print("Поиск выполнен.")
        else:
            print("Некорректная команда. Попробуйте ещё раз.")
        continue_running = input("Хотите продолжить работу с программой? (yes/no): ")
        if continue_running.lower() == "no":
            break


if __name__ == "__main__":
    main()
