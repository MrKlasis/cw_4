from app.models.data import Data
from settings import PATH_WITH_FIXTURES

def main():
    database = Data(PATH_WITH_FIXTURES)
    database.get_data()
    database.get_results()



if __name__ == '__main__':
    main()