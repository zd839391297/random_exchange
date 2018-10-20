import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style({"font.sans-serif": ['Microsoft YaHei', 'SimHei']})

data = np.loadtxt("random.txt")
men = np.zeros(shape=(30, 2))
for i in range(0, 30):
    men[i][0] = i
for j in range(0, 30):
    for i in range(0, 30):
        a = int(data[j][i])
        men[a-1][1] += 1
# print(men)
data_draw = data
data_draw.shape = (1, 900)
fig, ax = plt.subplots()
n, bins, patches = ax.hist(data_draw[0], 30, density=1)
'''
y = men[:,1]
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
'''
# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
