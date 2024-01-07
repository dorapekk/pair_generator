class Gift:

    name = ""

    def __init__(self, name):
        self.name = name


    def get_name(self):
        return self.name
    

zokni = Gift("pottyos zokni")


print(zokni)

