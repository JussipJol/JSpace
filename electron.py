class Electron:
    def __init__(self, height: int = 18, diam: float = 1.2, start_mass: int = 13000, levels: int = 2, material: str = "carbon fiber", fuel = "LOX/RP-1", name:str = "Electron (RocketLab)"):
        self.name = name
        self.height = height
        self.diam = diam
        self.start_mass = start_mass
        self.levels= levels
        self.material= material
        self.fuel= fuel

    def change_name(self):
        self.name = input("new name: \n")
        print(f"Name was successfully changed to {self.name}")

    def get_info(self):
        return print(f"info: \nname: {self.name} \nheight: {self.height}, \ndiam:  {self.diam}, \nfuel: {self.fuel}, \nstarting mass: {self.start_mass}, \nlevels: {self.levels}, \nmaterial: {self.material} ")

    def start_engine(self):
        pass
    # def propellant_controll(): pass
    # def get_info_payload(): pass

    def scan(): pass


    