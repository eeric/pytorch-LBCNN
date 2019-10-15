import torch
from torch.nn import Module, Parameter, Conv2d

class LBCNN(Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1):
		super(LBCNN, self).__init__()
		self.nInputPlane = in_channels
		self.nOutputPlane = out_channels
		self.kW = kernel_size
		self.LBCNN = Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, False)
		self.LBCNN.weight.requires_grad=False
         #init weight
		numElements = self.nInputPlane*self.nOutputPlane*self.kW*self.kW
		index = torch.randperm(numElements)
		self.LBCNN.weight.copy = (torch.Tensor(self.nOutputPlane,self.nInputPlane,self.kW,self.kW).uniform_(0, 1))
		temp = (torch.bernoulli(self.LBCNN.weight.copy)*2-1).view(-1)
		for i in range(1,numElements/2):
		    temp[index[i]] =0;
		self.LBCNN.weight.copy = temp.view(self.nOutputPlane,self.nInputPlane,self.kW,self.kW)
		self.LBCNN.weight = Parameter(self.LBCNN.weight.copy)
		
    def forward(self, input):
         return self.LBCNN.forward(input)
