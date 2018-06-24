import numpy as np

x = np.zeros((3,4))

for i in range(3):
    for j in range(4):
        
        x[i][j] = 5*i* 5*j
print(x)
x1 = np.array([[0,5,10,15],[5,5,10,15],[10,10,10,15]])

m = np.array([[0.02,0.06,0.02,0.10],[0.04,0.14,0.20,0.10],[0.01,0.15,0.15,0.01]])

z = np.sum(np.sum(np.multiply(x,m),1),0)

column = np.array([0,5,10,15])
row = np.array([0,5,10])
a = np.sum(np.multiply(row, np.sum(m,1)),0)
b = np.sum(np.multiply(column, np.sum(m,0)),0)
a1 = 45.0
mean1 = np.dot(column.T,np.sum(m,0))
mean2 = np.dot(row.T,np.sum(m,1))
std1 = np.add(column,-mean1)
std2 = np.add(row, -mean2)
std1 = np.dot(np.square(std1), np.sum(m,0))
std2 = np.dot(np.square(std2), np.sum(m,1))

std1 = np.sqrt(std1)
std2 = np.sqrt(std2)
print((z - a*b) / (std1 * std2))