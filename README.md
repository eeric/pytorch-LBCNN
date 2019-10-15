# pytorch-LBCNN
Local Binary Convolutional Neural Networks by pytorch

1.Original torch project

https://github.com/juefeix/lbcnn.torch

2.This project by pytorch

Only including the Convolutional layer through Local Binary,it was named LBCNN.py

3.Usage

Making Local Binary Convolutional layer instead of the original Convolutional layer

e.g:

from LBCNN import LBCNN #module

....

....

self.conv = LBCNN(in_channels,out_channels,3,stride,1) #define LBCNN in model file

4.See blog

http://blog.csdn.net/yyqq7226741/article/details/78308036

5.Thanks

In 11th line of LBCNN.py, taked 'False' to 'True', by Lynkzhang's testing
the reason that the new convolution layer needs to update the gradient

@Lynkzhang, https://github.com/Lynkzhang
