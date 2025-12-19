from dataclasses import dataclass


# @dataclass
# class ModelConfig:
#     lr: float
#     model: str
#     batch_size: int


# config = ModelConfig(0.001, "orzeł-50", 32)
# config2 = ModelConfig(0.001, "orzeł-50", 16)
# print(config.lr)
# print(repr(config))
# print(config)
# print(config == config2)
# print(config.lr > config2.lr)


@dataclass(frozen=True)
class ModelConfig:
    lr: float
    batch_size: int
    model: str = "orzeł-69"


config = ModelConfig(0.001, 32, "orzeł-50")


print(config.lr)
