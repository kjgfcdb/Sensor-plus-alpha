import seaborn as sns
import numpy as np
sns.distplot(np.loadtxt("Label.txt"))
sns.plt.show()
