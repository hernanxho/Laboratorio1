from graphviz import Digraph

# Crear un nuevo gráfico dirigido
dot = Digraph()

# Añadir nodos
dot.node('A', 'Nodo A')
dot.node('B', 'Nodo B')
dot.node('C', 'Nodo C')

# Añadir aristas
dot.edge('A', 'B', 'A -> B')
dot.edge('B', 'C', 'B -> C')

# Renderizar el gráfico
dot.render('grafico', format='png', cleanup=True)