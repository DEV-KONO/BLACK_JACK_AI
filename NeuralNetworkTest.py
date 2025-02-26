import random
import time


train_x = [i+1 for i in range(0,100)]
train_y = [i*2 for i in train_x]

w = random.uniform(0,1)
b = random.uniform(0,1)

alpha = .0001

cuad_diff = []
predicts = []

def MSE():
    CDS = 0
    for i in cuad_diff:
        CDS += i

    return CDS/len(cuad_diff)

def DMSE_en_Dw():
    x_Diff_Sum = 0
    for i in range(0,len(train_x)):
        x_Diff_Sum += train_x[i] * (train_y[i]-predicts[i])
    return (-2/len(train_x)) * x_Diff_Sum

def DMSE_en_Db():
    x_Diff_Sum = 0
    for i in range(0,len(train_x)):
        x_Diff_Sum += (train_y[i]-predicts[i])
    return (-2/len(train_x)) * x_Diff_Sum


def predict(w,x,b):
    return w * x + b

def MAPE():
    return (sum(abs(r - p) / r for r, p in zip(train_y, predicts)) / len(train_y)) * 100

# def ReLU(x):
#     return x * (x > 0)

prev_mse = float('inf')

start_time = time.time()

for j in range(0,1000000):
    for i in range(0,len(train_x)):
        predicts.append(predict(w,i+1,b))
        # print(f"Actual:{train_y[i]}    Prediction:{predict(w,i+1,b)}")
        cuad_diff.append((train_y[i] - predict(w,i+1,b))**2)
    
    mse = MSE()
    mape = MAPE()

    print(f"Iteration: {j}")
    print(f"MSE = {MSE()}   MAPE = {MAPE()}%")
    # print(f"MSE = {MSE()}   DMSE/Dw = {DMSE_en_Dw()}    DMSE/Db = {DMSE_en_Db()}    Weight = {w}    Bias = {b}")

    if abs(prev_mse - mse) < 1e-10:  # Si la mejora es mínima, detenemos
        print(f"Converged at iteration {j}, MSE = {mse:.10f}, MAPE = {mape:.10f}, Weight = {w:.10f}, Bias = {b:.10f}, Alpha = {alpha}")
        break  

    prev_mse = mse

    w = w - alpha*DMSE_en_Dw()
    b = b - alpha*DMSE_en_Db()

    predicts = []
    cuad_diff = []

end_time = time.time()

print(f"Tiempo de entrenamiento: {end_time-start_time:.4f}")

flag = True

while flag:
    test = float(input("Ingrese un numero: "))

    print(f"Numero Predicho: {predict(w,test,b)}")
    print(f"Numero Real: {2*test}")
    print(f"Error = {abs(((2*test)-predict(w,test,b))/(2*test))*100}%")