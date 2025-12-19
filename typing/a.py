# model_config: dict[str, int] = {"batch_size": 32, "epochs": 10, "input_dim": 768}

# # print(model_config)


# def add(x: int | float, y: float = 5.5):
#     print(x + y)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 111]

# from typing import Callable


# def filtruj_liste(lista: list[int], warunek: Callable[[int], bool]) -> list[int]:
#     wynik = []
#     for liczba in lista:
#         if warunek(liczba):  # Wywołujemy przekazaną funkcję
#             wynik.append(liczba)
#     return wynik


# # Definiujemy różne warunki
# def czy_parzysta(n: int) -> bool:
#     return n % 2 == 0


# liczby = [1, 2, 3, 4, 5, 6]

# # Używamy funkcji 'czy_parzysta' jako argumentu
# tylko_parzyste = filtruj_liste(liczby, czy_parzysta)
# print(tylko_parzyste)  # [2, 4, 6]

from typing import Callable


def rabat_staly(cena: float) -> float:
    return cena - 10.0


def rabat_procentowy(cena: float) -> float:
    return cena * 0.8


def brak_rabatu(cena: float) -> float:
    return cena


def oblicz_cene_koncowa(cena: float, logika_rabatu: Callable[[float], float]) -> float:
    return logika_rabatu(cena)


print(oblicz_cene_koncowa(50.0, rabat_staly))
print(oblicz_cene_koncowa(50.0, rabat_procentowy))
print(oblicz_cene_koncowa(50.0, brak_rabatu))
