import numpy as np
import gym

#posibles acciones(3): izquierda, derecha o no hacer nada

episodios = 30000
gamma = 0.9
iteraciones_maximas = 1000
n_estados = 100
estados = []

def getState(env,obs):
    env_low = env.observation_space.low
    env_high = env.observation_space.high
    env_dx = (env_high - env_low) / n_estados
    x = int((obs[0] - env_low[0])/env_dx[0])
    y = int((obs[1] - env_low[1])/env_dx[1])
    s = (x,y)
    return s

def inicializarTablas():
    for estado in estados:
        temp = {}
        tempA = {}
        for acc in range(env.action_space.n):
            temp[acc] = 0
            tempA[acc] = 0
        Q[estado] = temp
        N[estado] = tempA

def inicializarEstados():
    for i in range(n_estados):
        for j in range(n_estados):
            estados.append((i,j))

def incQ(s, a, alpha, inc):
    Q[s][a] = Q[s][a] + alpha*(inc - Q[s][a])

def maxQ(s):
    val = None
    acc = None
    for a, q in Q[s].items():
        if val is None or (q > val):
            val = q
            acc = a
    return acc,val

env_name = 'MountainCar-v0'
env = gym.make(env_name)
#limites de los estados
#limite superior
print(env.observation_space.high)
#limite inferior
print(env.observation_space.low)
Q = {}
N = {}
inicializarEstados()
inicializarTablas()
evaluacion = []
for i_episode in range(episodios):
    observation = env.reset()
    sumRec = 0
    for iter in range(iteraciones_maximas):
        s = getState(env,observation)
        action,_ = maxQ(s)
        observation, recompensa, done, _ = env.step(action)
        N[s][action] += 1
        alpha = float(500)/float(499 + N[s][action])
        s2 = getState(env,observation)
        _, maxVal = maxQ(s2)
        incQ(s, action, alpha, recompensa + gamma * maxVal)
        sumRec += recompensa
        if done:
            break
    if i_episode % 100 == 0:
        print("Episodio {0} acabado con recompensa total de {1} ".format(i_episode,sumRec))
    if i_episode>= (episodios-100):
        evaluacion.append(sumRec)
        if i_episode == episodios-1:
            env.render()
print "evaluacion media: ",np.mean(evaluacion)