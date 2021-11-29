from magazine import utils
class Product:
    def __init__(self, id_num: str, name: str):
        self.id_num = id_num
        self.name = name
        utils.test("test")