import matplotlib.pyplot as plt
import ElArbol as arbol

def graficar_arbol(nodo, x=0, y=0, delta_x=1):
    if nodo is not None:
        plt.text(x, y, str(nodo.data), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

    if nodo.left is not None:
            plt.plot([x, x - delta_x], [y - 0.1, y - 1], 'k-')
            graficar_arbol(nodo.left, x - delta_x, y - 1, delta_x / 2)

    if nodo.right is not None:
            plt.plot([x, x + delta_x], [y - 0.1, y - 1], 'k-')
            graficar_arbol(nodo.right, x + delta_x, y - 1, delta_x / 2)


arbol.tree.insert(arbol.tree.root, 'silence')
arbol.tree.insert(arbol.tree.root, 'wonder woman')
arbol.tree.insert(arbol.tree.root, 'Unbreakable')
arbol.tree.insert(arbol.tree.root, 'traffic')

plt.figure(figsize=(8, 6))
graficar_arbol(arbol.tree.root)
plt.axis('off')  # Ocultar los ejes
plt.show()