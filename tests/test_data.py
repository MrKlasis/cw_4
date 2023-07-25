from app.models.data import Data
import pytest

from app.models.operation import Operation


@pytest.fixture()
def data():
    return Data("operations_test.json")

def test_init(data):
    assert data.data == None
    assert data._path == "operations_test.json"

def test_get_data(data):
    data.get_data()
    assert isinstance(data.data, list)
    assert data.data is not None

def test_bad_convert(data):
    data.get_data()
    assert data._convert_bad_names() == [{
    "id_": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationamount_": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from_": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id_": 41428829,
    "state": "CANCELED",
    "date": "2019-07-03T18:35:29.512364",
    "operationamount_": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "to": "Счет 35383033474447895560"
  },
  {
    "id_": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationamount_": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from_": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {}
]

def test_operation_list(data):
    data.get_data()
    operation1 = Operation(441945886,
                           "2019-08-26T10:50:58.294041",
                           "EXECUTED", {
                               "amount": "31957.58",
                               "currency": {
                                   "name": "руб.",
                                   "code": "RUB"
                               },},

                           "Перевод организации",
                           "Счет 64686473678894779589",
                           "Maestro 1596837868705199")

    operations = data._get_operation_list()
    print(operations[0].id_, operation1.id_)
    assert operations[0].__dict__ == operation1.__dict__