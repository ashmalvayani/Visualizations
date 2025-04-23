import pandas as pd
from onion_rings.onion_rings import plot_onion_rings
import numpy as np

dictionary = {'Color': np.random.choice(['red','blue','green'],100,p=[0.5,0.3,0.2]), 
              'Shape': np.random.choice(['triangle','circle','square'],100),
              'Size': np.random.choice(['small','medium','large'],100,p=[0.6,0.3,0.1])
             }
dataframe = pd.DataFrame(dictionary)

plot_onion_rings(dataframe,['Shape','Color','Size'],plot_threshold=0.01,fontsize=10,rel_percent=True);