import torch
from torch import nn


class Tudui(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self,input):
        output=input+1
        return output

tudui=Tudui()
print(tudui.forward(9))
x=torch.tensor(12)
y=tudui.forward(x)
print(y)