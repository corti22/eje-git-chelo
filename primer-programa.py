#print("Hola mundo")
#a=150
#B=400
#a+B
#print(a+B)

import numpy as np
import plotly.graph_objects as go

t=np.arange(0,1,0.01)
f1=np.sin(2*np.pi*t)
f2=np.cos(2*np.pi*t)
fig=go.Figure()

fig.add_trace(go.Scattergl(x=t, y=f1, mode="lines", name="sin()"))
fig.add_trace(go.Scattergl(x=t, y=f2, mode="lines", name="cos()"))

fig.add_trace(go.Scattergl(x=t, y=f1+f2, mode="lines", name="suma"))

fig.show()  

print(np.__version__)

