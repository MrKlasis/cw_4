def main():
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    hh_engine = HH(keyword)
    sj_engine = Superjob(keyword)
    connector = JSONVacancyFile("vacancy.json")

    # Получить вакансии из апи hh и sj

    while True:
        command = input("Введите команду (sort, top, search): ")
        if command == "sort":
        # выполни сортировку
        elif command == "top":
        # выполни сортировку
        elif command == "search":
        # внести параметры поиска
        # выполнить поиск по параметрам
        else:
            print("Некорректная команда. Попробуйте ещё раз.")
        continue_running = input("Хотите продолжить работу с программой? (yes/no): ")
        if continue_running.lower() == "no":
            break


if __name__ == "__main__":
    main()
