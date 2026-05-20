from dataclasses import dataclass

@dataclass
class User:
    name: str
    email:str
    cpf: str
    password: str