# Pràctica 2
En aquesta carpeta trobem les classes MySocket corresponent al Client i MyServerSocket corresponent al servidor. Dins del client trobem l' utilització de dos threads concurrents, un per input i l'altre per output. En el cas del servidor, treballem amb un thread que representa un Socket "fill" que ens ajuda a treballar amb els clients. La forma d'accedir sincronitzadament als usuaris ha estat amb la classe ConcurrentHashMap.

## Archius a executar
java MyServerSocket

java MySocket nick