import pandas as pd
from data import *
import matplotlib.pyplot as plt
import numpy as np
import statistics

pd.options.display.max_columns = 500
df = pd.DataFrame()

df['year'] = year
df['month'] = month
df['domestic price'] = domestic
df['international price'] = international

x = df['domestic price']
y = df['international price']

m,b = np.polyfit(x,y,1)
print("domestic mean = " + str(statistics.mean(x)))
print("domestic max = " + str(max(x)))
print("domestic min " + str(min(x)))
print("international mean = " + str(statistics.mean(y)))
print("international max = " + str(max(y)))
print("international min = " + str(min(y)))


df['regress'] = m*df['domestic price'] + b

equation = "Regression eq: f(x) = " + str(round(m,4)) + "x + " + str(round(b,4))
print(equation)


plt.figure('domestic vs international gas price')
plt.suptitle('domestic vs international gas price', fontsize=20)
x_pos = 2.3
y_pos = 3.2
plt.text(x_pos, y_pos, equation, fontsize = 13)
plt.scatter(x,y)
plt.plot(x,df['regress'])
plt.xlabel('domestic price ($/gal)', fontsize = 15)
plt.ylabel('international price ($/gal)', fontsize = 15)

df['resid'] = df['international price'] - df['regress']

plt.figure('Residual')
plt.suptitle('Residual', fontsize=20)
plt.scatter(x,df['resid'])
plt.xlabel('domestic price ($/gal)', fontsize = 15)
plt.ylabel('observed - expected', fontsize = 15)
plt.plot(x,x*0,'k')
plt.show()
