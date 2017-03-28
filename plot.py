import seaborn as sns
import numpy as np
l = np.loadtxt("Label.txt")
sns.distplot(l)
sns.plt.show()
