from dataclasses import dataclass


@dataclass
class MyDataClass:
    first_name: str
    last_name: str

    def __post_init__(self):
        self.first_name = self.first_name.strip().title()
        self.last_name = self.last_name.strip().title()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def check_full_name(self, full_name: str) -> bool:
        return self.full_name == full_name


data = MyDataClass(first_name=" john ", last_name=" doe ")
print(data.full_name)
