# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:24:08 2017

@author: Joshua
"""
from sklearn.cluster.bicluster import SpectralCoclustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")
flavors = whisky.iloc[:, 2:14]
corr_flavors = pd.DataFrame.corr(flavors)
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")
whisky = whisky.reset_index(drop=True)
model = SpectralCoclustering(n_clusters=6, random_state=0)
model.rows_
np.sum(model.rows_, axis=0)
whisky['Group'] = pd.Series(model.row, index=whisky.index)
whisky = whisky.ix[np.argsort(model.row)]
whisky = whisky.rest_index(drop=True)

correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlation = np.array(correlations)
corr_whisky = pd.DataFrame.corr(flavors.transpose())
model.fit(corr_whisky)
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()
plt.savefig("corr_whisky.pdf")
plt.figure(figsize = (14, 7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Orignial")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefic("correlations.pdf")

