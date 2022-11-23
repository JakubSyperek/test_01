class Trip(object):

    goal: str
    price: float

    def __init__(self, goal: str, price: float) -> None:
        self.goal = goal
        self.price = price

    def __str__(self):
        return f"Opis wycieczki: {self.goal} {self.price}"
