Q-LEARNING EN OPENAI

Implementación del algoritmo Q-Learning en el entorno MountainCar de OpenAI.

 Se basa en un coche que tiene que conseguir llegar a la meta, la cual se encuentra en la cima de la montaña. Cada accion que no llegue a la meta devolverá una recompensa de -1, por lo que hay que intentar alcanzar una política óptima que llegue a la meta cuanto antes.

Las acciones del coche son: izquierda, derecha y no hacer nada.

DEPENDENCIAS

Librería GYM de OpenAI:

git clone https://github.com/openai/gym
cd gym
pip install -e . # minimal install

Más información sobre este entorno en: https://gym.openai.com/envs/MountainCar-v0/

EVALUACIÓN

Se superará la prueba si la recompensa total por episodio de los últimos 100 episodios consecutivos es menor o igual a -110.0
