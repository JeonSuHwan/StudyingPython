#Showing distributions using histograms
import numpy as np
import matplotlib.pyplot as plt

x=20*np.random.randn(10000)

plt.hist(x,25,range=(-50,51),
         histtype="stepfilled",align="mid",color='g',
         label="Test Data")
plt.legend()
plt.xlabel("x")
plt.ylabel('y')
plt.title("Step Filled Histogram")
plt.show()
