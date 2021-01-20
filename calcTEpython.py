# -*- coding: utf-8 -*-
import numpy as np


"""Tr_Y->X = SIGMA{ p(x_n+1, x_n, y_n) * log ( p(x_n+1, x_n, y_n) * p(x_n) / p(x_n, y_n) / p(x_n+1, x_n) }  """
def CAL_TE_Y_to_X(X, Y):
    """ Count """
    M_0 = np.zeros((2, 2, 2))     # p(x_n+1, x_n, y_n)
    M_1 = np.zeros((2, 2))      # p(x_n+1, x_n)
    M_2 = np.zeros((2, 2))      # p(x_n, y_n)
    M_3 = np.zeros(2)           # p(x_n)
    for t in range(len(X)):
        if t+1 != len(X):
            M_0[X[t + 1], X[t], Y[t]] += 1
            M_1[X[t + 1], X[t]] += 1
        M_2[X[t], Y[t]] += 1
        M_3[X[t]] += 1

    """ Normalizing (Count -> Probability) """
    M_0 = M_0 / M_0.sum()
    M_1 = M_1 / M_1.sum()
    M_2 = M_2 / M_2.sum()
    M_3 = M_3 / M_3.sum()

    TR_Y_to_X = 0
    for x_n1 in range(2):
        for x_n in range(2):
            for y_n in range(2):
                if ((M_0[x_n1, x_n, y_n] * M_3[x_n]) != 0) and (M_2[x_n, y_n] * M_1[x_n1, x_n] != 0):
                    TR_Y_to_X += M_0[x_n1, x_n, y_n] * np.log(M_0[x_n1, x_n, y_n] * M_3[x_n] / M_2[x_n, y_n] / M_1[x_n1, x_n])

    return TR_Y_to_X

""" d1 생성 : random """
d1 = np.random.randint(2, size=1000)
""" d1이 한칸씩 뒤로 밀린 data d2 생성 """
d2 = np.insert(d1, 0, 0)[:-1]

""" Transfer entropy 계산"""
TE1 = CAL_TE_Y_to_X(X=d1, Y=d2)
TE2 = CAL_TE_Y_to_X(X=d2, Y=d1)
print(TE1, TE2)

d1, d2

# +
import matplotlib.pyplot as plt
import numpy as np

X = np.random.randn(10000)
Y = np.random.randn(10000)
fig = plt.figure(figsize=(14, 7))
for cnt in range(10):
    """ Random Value 설정 """
    V1 = X.copy()
    u = 0.1 * cnt
    Y_new = (1 - u) * X + u * Y     # u가 클수록 Y_new는 X와 독립적인 성질을 나타냄
    V2 = Y_new.copy()

    q1 = np.linspace(min(V1), max(V1), 51)  # min ~ max 까지 50개의 영역 생성
    q2 = np.linspace(min(V2), max(V2), 51)  # min ~ max 까지 50개의 영역 생성

    """ Matrix 생성 """   # 같은 타이밍에 X, Y의 특징에 따라 Matrix M 에 갯수 누적
    N = 10000
    M = np.zeros((50, 50))  # X, Y 개수를 누적 할 50 x 50 Joint distribution 행렬 생성
    for step in range(N):
        x = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
        y =[0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
        for i in range(50):
            if (x >= q1[i]) and (x < q1[i+1]):
                break
        for j in range(50):
            if (y >= q2[j]) and (y < q2[j+1]):
                break
        M[i, j] += 1

    """ Mutual Information """
    """ MI = p(x,y) * log ( p(x,y) / p(x) / p(y) ) """
    """ MI = N_xy / N * log ( N_xy / N_x / N_y * N) """
    MI = 0
    N = M.sum()
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            N_x = M[i].sum()
            N_y = M[:, j].sum()
            N_xy = M[i, j]
            if N_xy != 0:
                MI += N_xy / N * np.log(N_xy * N / N_x / N_y)
    print(MI)
    d1 = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]

    d2 = [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
    subplot = fig.add_subplot(2, 5, cnt+1)
    plt.imshow(M)
    plt.title('u: ' + str(round(u,1)) + ' MI: ' + str(round(MI, 5)))
plt.suptitle('N: 10000 ; X,Y: Gausian distribution ; X vs (1-u)X+uY Mutual Information')
plt.show(block=False)
# -

pip install PyIF

from PyIF import te_compute

# +
from PyIF import te_compute as te
import numpy as np
rand = np.random.RandomState(seed=23)

X_1000 = rand.randn(2, 51)
Y_1000 = rand.randn(2, 51)

TE = te.te_compute(X_1000, Y_1000, k=2, embedding=2, safetyCheck=True, GPU=False)

print(TE)
# -

rand.randn(20, 2)
