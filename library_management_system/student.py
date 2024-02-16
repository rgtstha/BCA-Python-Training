class Student:
    def __init__(self, name, email, phone, address) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.phone} {self.address}"

        