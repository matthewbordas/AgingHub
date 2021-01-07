import json
import pathlib

class Repository():

    aging_counter = None

    def get_aging_counter_path(self) -> str:
        path_str = str(pathlib.Path(__file__).parent.absolute())
        path_list = path_str.rsplit('/', maxsplit=1)
        path_list.pop()
        path_list.append('/data/aging_counter.json')
        path_str = ''.join(path_list)
        return path_str

    def load_aging_counter(self, path: str) -> None:
        if self.__class__.aging_counter is None:
            with open(path) as data_file:
                json_loaded = json.load(data_file) 
                self.__class__.aging_counter = json_loaded
    
    def get_aging_counter(self) -> dict:
        return self.__class__.aging_counter
    
    def clear_aging_counter(self) -> None:
        self.__class__.aging_counter = None
