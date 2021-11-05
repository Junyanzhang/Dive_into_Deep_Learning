import torch
import  sys
from torch import nn
from d2l import torch as d2l

sys.path.append('F:\\web_auto\\Dive_into_deeplearning\\d2lutil')  # 加入路径，添加目录
import common
batch_size = 256
train_iter, test_iter = common.load_fashion_mnist(batch_size)

# PyTorch不会隐式地调整输入的形状。因此，
# 我们在线性层前定义了展平层（flatten），来调整网络输入的形状
net = nn.Sequential(nn.Flatten(), nn.Linear(784, 10))
#以均值0和标准差0.01随机初始化权重。
def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)

net.apply(init_weights);

loss = nn.CrossEntropyLoss()

trainer = torch.optim.SGD(net.parameters(), lr=0.1)
num_epochs = 10
common.train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)