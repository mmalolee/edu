import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="test.log",
    format="%(asctime)s : %(levelname)s : %(message)s",
)


# Definicja funkcji
def dodawanie(a, b):
    """Zwraca sumę dwóch liczb a i b."""
    return a + b


def odejmowanie(a, b):
    """Zwraca różnicę dwóch liczb a i b."""
    return a - b


def mnozenie(a, b):
    """Zwraca iloczyn dwóch liczb a i b."""
    return a * b


def dzielenie(a, b):
    """Zwraca iloraz dwóch liczb a i b. Obsługuje dzielenie przez zero."""
    if b == 0:
        return "Błąd: Nie można dzielić przez zero!"
    return a / b


# --- Przykładowe użycie ---

x = 20
y = 4

add = dodawanie(x, y)
sub = odejmowanie(x, y)
mul = mnozenie(x, y)
div = dzielenie(x, y)

logging.debug(add)
logging.debug(sub)
logging.debug(mul)
logging.debug(div)
