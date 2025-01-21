# Тензоры многомерная матрица
# Тензор должен иметь один тип данных
import torch

from SSE.SSEserver import ACCESS_TOKEN_EXPIRE_DAYS

# Пороговая функция
def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    # вектор с вещественными с весами связи нейронны скрытого слоя
    X = torch.tensor([house, rock, attr], dtype=torch.float32)
    #
    Wh = torch.tensor([[0.3, 0.3, 0], [0.4, -0.5, 1]])
    Wout = torch.tensor([-1.0, 1.0])

    Zh = torch.mv(Wh, X)
    print(f"Значение сумм на нейронах скрытого слоя: {Zh}")

    Uh = torch.tensor([act(x) for x in Zh], dtype=torch.float32)
    print(f'Значение на выходах нейронов скрытого слоя {Uh}')

    Zout = torch.dot(Wout, Uh)
    Y = act(Zout)
    print(f'Выходное значение НС {Y}')
    return Y


res = go(1,0,0)
if res == 1:
    print(f'нравится')
