import torch
import torch.nn as nn   # ✅ вот это нужно
import torch.nn.functional as F
import torch.optim as optim
from random import randint





class NetGirl(nn.Module):
    def __init__(self, input_dim, num_hidden, output_dim):
        super().__init__()
        self.layer1 = nn.Linear(input_dim, num_hidden)
        self.layer2 = nn.Linear(num_hidden, output_dim)

    def forward(self,x):
        x = self.layer1(x)
        x = F.tanh(x)
        x = self.layer2(x)
        x = F.tanh(x)
        return x

model_1 = NetGirl(3,2,1)
print(model_1)
gen_p = model_1.parameters()
print(list(gen_p))

x_train = torch.FloatTensor([(-1, -1, -1), (-1, -1,  1), (-1,  1, -1), (-1,  1,  1),
                             ( 1, -1, -1), ( 1, -1,  1), ( 1,  1, -1), ( 1,  1,  1)])

y_train = torch.FloatTensor([-1, 1, -1, 1, -1, -1])

total = len(y_train)


optimizer = optim.RMSprop(params=model_1.parameters(), lr=0.01)
loss_func = torch.nn.MSELoss()
model_1.train()

for _ in range(1000):
    k = randint(0, total - 1)
    y = model_1(x_train[k])                 # shape [1]
    t = y_train[k].unsqueeze(0)             # [] -> [1]
    loss = loss_func(y, t)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()



model_1.eval()

for x, d in zip(x_train, y_train):
    y=model_1(x)
    print(f"Выходное знчение нс {y.data} => {d}")
# model_2 = NetGirl(3,5,2)
# model_3 = NetGirl

# def forward(inp, l1: nn.Linear, l2: nn.Linear):
#     u1 = l1.forward(inp)
#     s1 = F.tanh(u1)
#     u2 = l2.forward(s1)
#     s2 = F.tanh(u2)
#     return s2
#
# layer1 = nn.Linear(in_features=3, out_features=2)
# layer2 = nn.Linear(2,1)
# print(layer1.weight)
# print(layer1.bias)
#
# layer1.weight.data = torch.tensor([[0.7402,  0.6008, -1.3340], [0.2098,  0.4537, -0.7692]])
# layer1.bias.data   = torch.tensor([0.5505, 0.3719])
#
# layer2.weight.data = torch.tensor([[-2.0719, -0.9485]])
# layer2.bias.data   = torch.tensor([-0.1461])
#
# x = torch.FloatTensor([1,-1,1])
# y = forward(x, layer1, layer2)
# print(y.data)