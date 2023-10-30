
import numpy as np
import matplotlib.pyplot as plt
size_train = np.array([1.0, 2.0]) 
price_train = np.array([300.0, 500.0])
weight = 100
bias = 100

plt.scatter (size_train, price_train, marker = 'o', c = 'r')
plt.title("House Price prediction program")
plt.xlabel("Size of the house (square feet)") 
plt.ylabel("Price of the house (dollars$)") 
plt.show()

def compute_model_output(x, w, b): # to predict the house price depending in the earlier datasets f(x) 
    m = x.shape[0]
    f_wb =np.zeros(m)
    for i in range(m):
        f_wb[i] =  w * x[i] + b
    return f_wb

def main():
    tmp_f_wb = compute_model_output (size_train, weight, bias,)

    plt.plot(size_train, tmp_f_wb, c = 'b', label =  "My prediction")
    plt.scatter (size_train, price_train, marker = 'o', c = 'r', label = "actual values")
    plt.title("House Price prediction program")
    plt.ylabel("Price of the house (dollars$)")
    plt.xlabel("Size of the house (square feet)")
    plt.legend() 
    plt.show()

main()