from src.invalid_data_exception import InvalidDataException


class FileHandler:
    def __init__(self, file_path: str, no_connectors: int, max_file_size: int):
        if file_path == "":
            raise InvalidDataException("File path cannot be empty.")
        if no_connectors > 10:
            raise InvalidDataException("Number of connectors cannot be greater than 10.")
        if not isinstance(max_file_size, int) or not 1000 <= max_file_size <= 9999:
            raise InvalidDataException("Max file size must be a four-digit integer.")
        self._file_path = file_path
        self._no_connectors = no_connectors
        self._max_file_size = max_file_size

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, value) -> None:
        if value == "":
            raise InvalidDataException("File path cannot be empty.")
        self._file_path = value

    @property
    def no_connectors(self) -> int:
        return self._no_connectors

    @no_connectors.setter
    def no_connectors(self, value) -> None:
        if value > 10:
            raise InvalidDataException("Number of connectors cannot be greater than 10.")
        self._no_connectors = value

    @property
    def max_file_size(self) -> int:
        return self._max_file_size

    @max_file_size.setter
    def max_file_size(self, value) -> None:
        if not isinstance(value, int) or not 1000 <= value <= 9999:
            raise InvalidDataException("Max file size must be a four-digit integer.")
        self._max_file_size = value

    def read_content(self):
        print("read_content")

    def save_to_file(self):
        print("save_to_file")
