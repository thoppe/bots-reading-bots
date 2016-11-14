import glob
import numpy as np
from tqdm import tqdm
import pandas as pd
import seaborn as sns
from scipy.cluster.hierarchy import linkage, leaves_list

cmap = sns.cubehelix_palette(as_cmap=True, rot=-.3,
                             light=1, reverse=True)

# Plot in resorted order

F_DATA = glob.glob("results/*")

data = []
for f in tqdm(F_DATA):
    val = pd.read_csv(f)
    val.loss /= val.loss.min()
    data.append(val)

df = pd.concat(data)
df = df.pivot('model','text','loss')
#print df.values
X = df.values
X = (X + X.T)/2.0
#X = np.exp(-X)
Z = linkage(X, 'ward')
idx = leaves_list(Z)

#B = df.values[idx,:][:,idx]
#B = np.exp(-B)
#sns.heatmap(df.values[idx,:][:,idx], cmap=cmap)
#sns.plt.show()
#print B

df = pd.DataFrame(data=X,index=df.index,columns=df.index)
#sns.clustermap(df)
sns.clustermap(df, cmap=cmap, vmax=1.25,method='centroid')

#sns.heatmap(A)
sns.plt.show()
