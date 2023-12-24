# House-Price-Prediction-Program
Simple Regression model:  simple house price prediction program with one feature which is the size of the house 

## Before the prediction 
![pic1](https://github.com/Esmail-ibraheem/House-Price-Prediction-Program/assets/113830751/effa7440-862a-4f78-a96d-b8828fc9fee1)

---
```python
def compute_model_output(x, w, b): # to predict the house price depending in the earlier datasets f(x) 
    m = x.shape[0]
    f_wb =np.zeros(m)
    for i in range(m):
        f_wb[i] =  w * x[i] + b
    return f_wb
```

---

## After the prediction 
![pic2](https://github.com/Esmail-ibraheem/House-Price-Prediction-Program/assets/113830751/bf744d81-2029-4058-b94d-01474bd003ec)
