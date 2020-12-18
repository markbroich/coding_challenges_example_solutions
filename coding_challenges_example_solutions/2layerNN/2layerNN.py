# 2-layer neural network in ~20 lines of code (from scratch via numpy)
# ignoring comments :) 

########################################################################
########################################################################
import numpy as np
from numpy.random import randn
########################################################################
# random seed
seed = 1
# epochs 
epochs = 200
# report every x epochs
report = 50
########################################################################
########################################################################


########################################################################
########################################################################
# forward pass equation: 
# loss = sum(((1/(1+exp(x*w1)))* w2-y)^2) 

# N = number of samples or rows = 64
# DIn = number of predictor variables or columns = 1000; 
#   (could also be = 3 if simple example with 3 predictor variables)
# H = number of 'intermediate' classes = 100; (could also be = 1)
# DIn = number of final classes = 10; (could also be = 1)
N, DIn, H, DOut = 64, 1000, 100, 10
# x and y are the inputs (64 samples 
# by 1000 predictor variables) and 
# the true results (64 samples by 10 classes)
np.random.seed(seed)
x, y = randn(N, DIn), randn(N, DOut)
w1, w2 = randn(DIn, H), randn(H, DOut)
#learning rate
lr = 1e-4
#
print("loop over epochs and train spelled out 2layerNN")
for t in range(epochs):
    # forward pass
    # first layer w sigmoid activation
    yTemp = x.dot(w1)
    h = 1/ (1+ np.exp(-yTemp))
    # second layer
    yPred = h.dot(w2)
    # loss
    loss = np.square(yPred - y).sum()
    # report every k epochs
    if t%report == 0:
        print(t, loss)
    #
    # backprop
    # gradYpred = grad of loss w R t yPred or df/ YPred
    gradYpred = 2.0 *(yPred - y)
    # gradW2 = grad of h w R t w2 or df/ w2
    gradW2 = h.T.dot(gradYpred)
    # gradH = grad of h w R t h or df/ h
    gradH = gradYpred.dot(w2.T)
    # gradYTemp = grad of h w R t yTemp or df/ yTemp
    gradYTemp = gradH * h * (1-h)
    # gradW1 = grad of h w R t w1 or df/ w1
    gradW1 = x.T.dot(gradYTemp)
    # 
    # gradient decent 
    w1 -= lr * gradW1 
    w2 -= lr * gradW2

print(t, loss, "done w", epochs, "epochs")
print("")
########################################################################
########################################################################


########################################################################
########################################################################
###### Diagram of matrices and operations
# forward pass equation: 
# loss = sum(((1/(1+exp(x*w1)))* w2-y)^2) 

#      x      *      w1   =   yTemp  
#                  [   ]
#  64[    ]    1000[   ]   64[   ]
#    [    ]        [   ]     [   ]
#     1000         [   ]      100
#                   100

#       sigm(yTemp)  *       w2   =  yPred
#                           [ ]  
# sigm(   64[   ]       100 [ ]    64 [ ]
#           [   ] )         [ ]       [ ]
#            100             10        10

#    (  yPred   -    y  )^2    =   loss
#                           
#    (  64 [ ]   64 [ ]        
#          [ ]      [ ] )^2         []
#           10       10             10

########################################################################
########################################################################


########################################################################
########################################################################
# And now in modular form.

########################################################################
# network gates:

# multiplication module
class MultiplicationGate:
    def fw(self, x, y):
        self.x = x
        self.y = y
        z = self.x.dot(self.y)
        return z
    def bp(self, dz):
        dx = self.x.T.dot(dz) 
        dy = dz.dot(self.y.T) 
        return dx, dy

# signmoid module
class SignmoidGate:
    def fw(self, x):
        z = 1/ (1+ np.exp(-x))
        self.z = z
        return z
    def bp(self, dz):
        dx = dz * self.z * (1-self.z)
        return dx

# mse (loss) module 
class MseGate:
    def fw(self, yPred, y):
        self.yPred = yPred
        self.y = y
        loss = np.square(yPred - y).sum()
        return loss
    def bp(self):
        dz = 2.0 *(self.yPred - self.y)
        return dz
########################################################################


# input specs
N, DIn, H, DOut = 64, 1000, 100, 10
# random init of x, y, w1, w2
np.random.seed(seed)
x, y = randn(N, DIn), randn(N, DOut)
w1, w2 = randn(DIn, H), randn(H, DOut)
#learning rate
lr = 1e-4

# init gates
MulGate1 = MultiplicationGate()
SigGate1 = SignmoidGate()
MulGate2 = MultiplicationGate()
MseGate1 = MseGate()

print("loop over epochs and train modular 2layerNN")
for t in range(epochs):
    # forward pass
    # loss = sum(((1/(1+exp(x*w1)))* w2-y)^2)
    yTemp = MulGate1.fw(x, w1)
    h = SigGate1.fw(yTemp)
    yPred = MulGate2.fw(h, w2)
    loss = MseGate1.fw(yPred, y)
    #
    # report every k epochs
    if t%report == 0:
        print(t, loss)
    #
    # backprop
    gradYpred = MseGate1.bp()
    gradW2, gradH = MulGate2.bp(gradYpred)
    gradYtemp = SigGate1.bp(gradH)
    gradW1, gradX = MulGate1.bp(gradYtemp)

    # gradient decent 
    w1 -= lr * gradW1 
    w2 -= lr * gradW2

print(t, loss, "done w", epochs, "epochs")
########################################################################
########################################################################

# inspired by Serena Yeung's lecture (Stanford CS): 
# https://www.youtube.com/watch?v=d14TUNcbn1k&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv&index=4 





