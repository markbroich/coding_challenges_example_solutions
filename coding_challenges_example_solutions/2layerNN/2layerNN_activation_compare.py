# 2-layer neural network 
# here I am comparing signmid and relu activation
# for 30 weights and 20 nodes, relu trains faster 

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
#
# input specs only 30 weights and 20 nodes
N, DIn, H, DOut = 64, 30, 20, 10
#learning rate
lr = 1e-4 
########################################################################
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

# relu module
class ReluGate:
    def fw(self, x):
        z = x * (x > 0)
        return z
    def bp(self, dz):
        dx = (1. * (dz > 0))
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
########################################################################


########################################################################
########################################################################
# random init of x, y, w1, w2
np.random.seed(seed)
x, y = randn(N, DIn), randn(N, DOut)
w1, w2 = randn(DIn, H), randn(H, DOut)


# random init of x, y, w1, w2
np.random.seed(seed)
x, y = randn(N, DIn), randn(N, DOut)
w1, w2 = randn(DIn, H), randn(H, DOut)

# init gates
MulGate1 = MultiplicationGate()
SigGate1 = SignmoidGate()
MulGate2 = MultiplicationGate()
MseGate1 = MseGate()

print('comparison between sigmoid and relu')
print('signmoid:')
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
print('')

#### run again this time w relu
# random init of x, y, w1, w2
np.random.seed(seed)
x, y = randn(N, DIn), randn(N, DOut)
w1, w2 = randn(DIn, H), randn(H, DOut)

# init gates
MulGate1 = MultiplicationGate()
ReluGate1 = ReluGate()
MulGate2 = MultiplicationGate()
MseGate1 = MseGate()

print('comparison between sigmoid and relu')
print('relu:')
for t in range(epochs):
    # forward pass
    # loss = sum(((1/(1+exp(x*w1)))* w2-y)^2)
    yTemp = MulGate1.fw(x, w1)
    h = ReluGate1.fw(yTemp)
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
    gradYtemp = ReluGate1.bp(gradH)
    gradW1, gradX = MulGate1.bp(gradYtemp)

    # gradient decent 
    w1 -= lr * gradW1 
    w2 -= lr * gradW2

print(t, loss, "done w", epochs, "epochs")
print('')

print('Here, I am comparing signmoid and relu activation \
for 30 weights and 20 nodes, relu trains faster ')
print('Yet, for 1000 weights and 100 nodes, I get an error for the relu version. ')
print('The error does not occur when I reduce the learning rate but relu is \
also slower than signmoid')

########################################################################
########################################################################
print('I can get 1000 weights and 100 nodes relu result that \
is better than sigmoid with a lr =',lr ,'and training for more epochs')
#
epochs = 10000
# report every x epochs
report = 2000

# input specs only 1000 weights and 100 nodes
N, DIn, H, DOut = 64, 1000, 100, 10
#learning rate
lr = 1e-7 # with a learning rate of : lr = 1e-6, the relu loss explodes

# random init of x, y, w1, w2
np.random.seed(seed)
x, y = randn(N, DIn), randn(N, DOut)
w1, w2 = randn(DIn, H), randn(H, DOut)

print('comparison between sigmoid and relu 1000 weights and 100 nodes w lr = 1e-7')
print('signmoid:')
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
print('')

#### run again this time w relu
# random init of x, y, w1, w2
np.random.seed(seed)
x, y = randn(N, DIn), randn(N, DOut)
w1, w2 = randn(DIn, H), randn(H, DOut)

print('comparison between sigmoid and relu')
print('relu:')
for t in range(epochs):
    # forward pass
    # loss = sum(((1/(1+exp(x*w1)))* w2-y)^2)
    yTemp = MulGate1.fw(x, w1)
    h = ReluGate1.fw(yTemp)
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
    gradYtemp = ReluGate1.bp(gradH)
    gradW1, gradX = MulGate1.bp(gradYtemp)

    # gradient decent 
    w1 -= lr * gradW1 
    w2 -= lr * gradW2

print(t, loss, "done w", epochs, "epochs")
print('the final relu loss is < the sigmoid loss of 2layerNN.py when trining for', epochs, 'epochs')
print('Finally, for a lr = 1e-6, the relu loss explodes highlighting the importance of lr as a hyperparameter')
#####################################################
########################################################################

# inspired by Serena Yeung's lecture (Stanford CS): 
# https://www.youtube.com/watch?v=d14TUNcbn1k&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv&index=4 





