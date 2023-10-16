import torch
import numpy as np

w1, w2, w3, w4, w5, w6, w7, w8 = 0.2, -0.4, 0.5, 0.6, 0.1, -0.5, -0.3, 0.8
x1, x2 = 0.5, 0.3
y1, y2 = 0.23, -0.07

def sigmoid(z):
    a = 1 / (1 + np.exp(-z))
    return a


in_h1 = w1 * x1 + w3 * x2
out_h1 = sigmoid(in_h1)
in_h2 = w2 * x1 + w4 * x2
out_h2 = sigmoid(in_h2)

in_o1 = w5 * out_h1 + w7 * out_h2
out_o1 = sigmoid(in_o1)
in_o2 = w6 * out_h1 + w8 * out_h2
out_o2 = sigmoid(in_o2)

in_h1 = torch.tensor(w1 * x1 + w3 * x2)
out_h1 = torch.sigmoid(in_h1)
in_h2 = torch.tensor(w2 * x1 + w4 * x2)
out_h2 = torch.sigmoid(in_h2)

# in_o1 = torch.tensor(w5 * out_h1 + w7 * out_h2)
# out_o1 = torch.sigmoid(in_o1)
# in_o2 = torch.tensor(w6 * out_h1 + w8 * out_h2)
# out_o2 = torch.sigmoid(in_o2)


print(out_o1,out_o2)