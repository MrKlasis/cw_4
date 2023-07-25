import json
from pathlib import Path
from app.models.operation import Operation


class Data:
    def __init__(self, path: [Path, str] = None):
        self._path = path
        self.data = None

    def get_data(self):
        with open(self._path, encoding="utf-8") as file:
            self.data = json.load(file)

    def _convert_bad_names(self):
        operations = []
        for operation in self.data:
            data = {}
            for key, value in operation.items():
                if key in ('operationAmount', 'from', 'id'):
                    data[key.lower() + '_'] = value
                else:
                    data[key] = value
            operations.append(data)
        return operations

    def _get_operation_list(self) -> list[Operation]:
        operations_list: list[Operation] = []
        operations = self._convert_bad_names()
        for iteration, operation in enumerate(operations, start=1):
            try:
                operations_list.append(Operation(**operation))
            except TypeError:
                print(f'Не валидные данные в операции №{iteration}: {operation}')
                continue
        return operations_list

    def _get_first_five_sorted_operations(self) -> list[Operation]:
        operations = self._get_operation_list()
        return sorted(
            operations,
            key=lambda operation_data: operation_data.date,
            reverse=True
        )[:5]

    def get_results(self) -> bool:
        five_operations: list[Operation] = self._get_first_five_sorted_operations()
        for operation in five_operations:
            print(operation.get_info_for_operation())
        return True
