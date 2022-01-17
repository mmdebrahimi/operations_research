import pyomo.environ as pyo
import numpy as np
import time
from pyomo.environ import *
from pyomo.opt import SolverFactory


model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(-np.inf,3))
model.y = pyo.Var(bounds=(0,np.inf))

x = model.x
y = model.y

model.C1 = pyo.Constraint(expr= x+y<=8)
model.C2 = pyo.Constraint(expr= 8*x+3*y>=-24)
model.C3 = pyo.Constraint(expr= -6*x+8*y<=48)
model.C4 = pyo.Constraint(expr= 3*x+5*y<=15)

model.obj = pyo.Objective(expr= -4*x-2*y, sense=minimize)

tempo_inicial = time.time()
opt = SolverFactory('glpk')
opt.solve(model)
tempo = time.time()-tempo_inicial

x_value = pyo.value(x)
y_value = pyo.value(y)

print('tempo:',tempo)
print('x:',x_value)
print('y:',y_value)
