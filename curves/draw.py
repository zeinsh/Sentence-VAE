import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

train_loss=pd.read_csv('TRAIN_loss.csv',sep='\t')

fig1=plt.figure()
plt.plot(train_loss.NLL/32.)
plt.xlabel('global-steps')
plt.title('Negative Log Likelihood NLL term in Loss and Training Loss')
plt.legend()
plt.grid()
plt.tight_layout()
fig1.savefig('train-Loss,NLL.png')

fig2=plt.figure()
plt.plot(train_loss.KL/32.)
plt.xlabel('global-steps')
plt.legend()
plt.title('KL divergence term in Loss fucntion')
plt.grid()
plt.tight_layout()
fig2.savefig('train-KL.png')

fig2=plt.figure()
plt.plot(train_loss.KL_Weight)
plt.xlabel('global-steps')
plt.legend()
plt.title('KL_Weight')
plt.grid()
plt.tight_layout()
fig2.savefig('KL_Weight.png')

fig2=plt.figure()
plt.plot(train_loss.KL/32.)
plt.plot(train_loss.KL_Weight*1.5)
plt.annotate("KL_Weight=1",(1100,1.5))
plt.xlabel('global-steps')
plt.legend()
plt.title('KL_term and KL_Weight')
plt.grid()
plt.tight_layout()
fig2.savefig('KL+KL_Weight.png')


import matplotlib.pyplot as plt
import pandas as pd
train_loss=pd.read_csv('VALID_loss.csv',sep='\t')

fig1=plt.figure()
plt.plot(train_loss.NLL/32.)
plt.xlabel('global-steps')
plt.title('Negative Log Likelihood NLL term in Loss and VALID Loss')
plt.legend()
plt.grid()
plt.tight_layout()
fig1.savefig('VALID-Loss,NLL.png')

fig2=plt.figure()
plt.xlabel('global-steps')
plt.plot(train_loss.KL/32.)

plt.legend()
plt.title('KL divergence term in Loss fucntion')
plt.grid()
plt.tight_layout()
fig2.savefig('VALID-KL.png')

import matplotlib.pyplot as plt
import pandas as pd
train_loss=pd.read_csv('elbo.csv',sep='\t')

fig1=plt.figure()
elbovalues=[]
for i in range(len(train_loss.elbo/32.)): 
    if i%2==0:
       elbovalues.append(train_loss.elbo.loc[i]/32.)
plt.plot(np.arange(len(elbovalues))+1,elbovalues)
plt.xlabel('global-steps')
plt.title('ELBO')
plt.grid()
plt.tight_layout()
fig1.savefig('ELBO.png')

