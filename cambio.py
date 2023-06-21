import networkx as nx

import matplotlib.pyplot as plt

vertices = ["1","2","3","4","5","6","7","8"]
aristas = [('2', '4', 4) , ('2', '1', 5) , ('2', '3', 2) , ('3', '1', 3) , ('4', '1', 4),
('7', '5', 3), ('1', '5' , 3), ('1','6', 7), ('8' , '4' , 2), ('6', '8', 1) , ('8', '7', 6), ('6', '7' , 8), ('5', '3', 2)]

g = nx.Graph()
g.add_nodes_from(vertices)


dijkstra = nx.dijkstra_path(g , '2' , '7')
pos = nx.layout.spring_layout(g)
nx.draw_networkx(g, pos)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels) 
plt.show()

    
    
def cambiar_calles():  
    calles_a_cambiar = []
    numero_calle = 1
    
    for arista in aristas:
    
        calle_correcta = [arista[1], arista[0]]
    
        for i in range (1, len(dijkstra)):
            if(calle_correcta[0] == dijkstra[i - 1] and calle_correcta[1] == dijkstra[i]):
             calles_a_cambiar.append(numero_calle)
        numero_calle +=1
    
    print(calles_a_cambiar)
    print(nx.dijkstra_path_length(g , '2' , '7'))
    
    
cambiar_calles()



    





