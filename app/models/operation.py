import re
from datetime import datetime


class Operation:
    def __init__(self, id_, date, state, operationamount_, description, to, from_=None):
        self.id_ = id_
        self.date = date
        self.state = state
        self.operations_amount = operationamount_
        self.description = description
        self.from_ = _encode_data(from_) if from_ else""
        self.to = _encode_data(to)

    @property
    def _encoded_date(self):
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        date = datetime.strptime(self.date, date_format)
        return date.date().strftime("%d.%m.%Y")

    def get_info_for_operation(self):
        return f"""{self._encoded_date} {self.description} 
{self.from_ if self.from_ else ""} -> {self.to} 
{self.operations_amount["amount"]} {self.operations_amount["currency"]["name"]}\n"""


def _encode_data(value: str) -> str:
    data = value.split()
    number_card = data[-1]
    if value.startswith('Счет'):
        data[-1] = '**' + data[-1][-4:]
        return ' '.join(data)

    hidden_number = number_card[0:6] + '******' + number_card[-4:]
    result = ' '.join(re.findall('(.{%s}|.+$)' %4, hidden_number))
    data[-1] = result
    return ' '.join(data)