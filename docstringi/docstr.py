# class Odliczanie:
#     def __init__(self, start):
#         self.liczba = start

#     def __iter__(self):
#         return self  # Obiekt sam jest swoim iteratorem

#     def __next__(self):
#         # 1. Warunek stopu (kiedy pętla for ma się zatrzymać)
#         if self.liczba <= 0:
#             raise StopIteration

#         # 2. Zapamiętaj obecną wartość
#         wynik = self.liczba

#         # 3. Przygotuj stan na następny krok
#         self.liczba -= 1

#         # 4. Zwróć wartość
#         return wynik


# # --- UŻYCIE ---
# timer = Odliczanie(3)

# # Python automatycznie woła __next__ w każdym kroku pętli
# for sekunda in timer:
#     print(f"Pozostało: {sekunda}...")

# # Wynik:
# # Pozostało: 3...
# # Pozostało: 2...
# # Pozostało: 1...
# # (Pętla kończy się, gdy napotka StopIteration)


# import time


# class Timer:
#     def __enter__(self):
#         # 1. Startujemy licznik w momencie wejścia w 'with'
#         self.start = time.time()
#         return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # 2. Zatrzymujemy licznik przy wyjściu
#         end = time.time()
#         print(f"⏱️ Czas operacji: {end - self.start:.4f} sekundy.")
#         # Zwrócenie False (domyślne) oznacza: "jeśli był błąd, nie ukrywaj go, wywal go na ekran"


# # --- UŻYCIE ---
# print("Start treningu...")

# with Timer():
#     # Symulacja ciężkiej operacji (np. trening sieci)
#     time.sleep(2)
#     print("...Trenuję model...")

# # Wynik w konsoli:
# # Start treningu...
# # ...Trenuję model...
# # ⏱️ Czas operacji: 2.0021 sekundy.


# import functools


# def train_model(data, lr, optimizer):
#     print(f"Trenowanie: LR={lr}, Opt={optimizer}, dane: {data}")


# # Tworzymy gotowy wariant pod konkretny eksperyment
# # Zamrażamy learning_rate i optimizer, zostawiamy tylko 'data'
# run_baseline = functools.partial(train_model, lr=2137, optimizer="piwo")

# # W pętli głównej podajemy już tylko dane
# run_baseline(data="perła.csv")


import time
import functools


@functools.lru_cache(maxsize=1024)
def get_embedding(text):
    # symulacja kosztownego kroku
    # wynik zostanie przeliczony tylko raz
    return  # embeding


def time_logger(func):
    # Bez tego func.__name__ zwróciłoby 'wrapper'
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Funkcja {func.__name__} wykonana.")
        return result

    return wrapper


@time_logger
def train_step(batch):
    """Wykonuje jeden krok treningowy."""
    print(train_step.__name__)
    print(train_step.__doc__)


train_step("elo")
