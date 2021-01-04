# Pràctica 3
A la carpeta SelectorNIO, s'ha intentat implementar un chat seguint el patrò reactor i l'API NIO. No s'ha assolit el funcionament d'aquest.

A la carpeta grafichat, s'implementa un client-servidor amb interfície gràfica utilitzant Swing i agafant com a base la pràctica 2.
El servidor és igual a la pràctica anterior utilitzant en canvi un HashMap, però el client, degut a la implementació amb Swing, queda llegurament modificat, diferenciant entre el Client, el seu socket per poder treballar amb UserInterface amb major facilitat, i la part gràfica (UserInterface) on trobem un àrea d'entrada (el botó de start), un àrea de missatges (on es mostra el historial del chat) i una barra d'escriptura amb el botó
d'enviar el missatge, amb la que interactua el usuari.

## Archius a executar
java Server

java Client nick