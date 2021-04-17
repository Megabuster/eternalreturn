import matplotlib.pyplot as plt
import networkx as nx

from lib.Area import Area
from lib.AreaStatus import AreaStatus


class RouteMaker:
    def __init__(self):
        self.chars = [
            'Adela', 'Adriana', 'Aya', 'Bernice', 'Cathy', 'Chiara', 'Emma',
            'Fiora', 'Hart', 'Hyejin', 'Hyunwoo', 'Isol', 'Jackie',
            'LI Dailin', 'Lenox', 'Luke', 'Magnus', 'Nadine', 'Rozzi',
            'Shoichi', 'Sissela', 'Xiukai', 'Yuki', 'Zahir'
        ]
        self.items = {}
        self.location_list = []
        self.location_map = {}

    def run(self):
        print('Executing program.')
        self.build_graph()
        #check item build locations
        #minimize walking distance
        #other variables
        '''
        hero info: name, weapon
        item dict
        key: name
        value: dict
        type/slot/etc
        locations dict
        location
        quantity
        build into list
        build from list
        '''

    def build_graph(self):
        with open('data/location-graph-raw.txt') as f:
            lines = f.read().splitlines()
        for index, line in enumerate(lines):
            area_name = line.split(' ')[1].replace('_', ' ').strip()
            #build into class
            neighbors = [int(x) for x in line.split(' ')[2].split(',')]
            new_area = Area(area_name, neighbors, index, status = AreaStatus.WHITE)
            #area_dict = {}
            #area_dict['name'] = area_name
            '''area_dict['neighbors'] = [
                int(x) for x in line.split(' ')[2].split(',')
            ]'''
            #end of Area object

            #make sure it's the class being appended
            self.location_list.append(new_area)
            self.location_map[area_name] = line.split(' ')[0]
        print(self.location_list)
        print(self.location_map)
        graph = nx.Graph()

        for loc in self.location_list:
            for next in loc.neighbors:
                #print(self.location_map[loc['name']])
                #print(next)
                if int(self.location_map[loc.name]) < int(next):
                    #call from class/object
                    graph.add_edge(loc.name,
                                   self.location_list[next].name,
                                   weight=1)
        print(graph)
        #pos=nx.get_node_attributes(graph,'pos')
        #nx.draw(graph)
        pos = nx.spring_layout(graph)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_nodes(graph, pos, node_size=700)
        nx.draw_networkx_labels(graph, pos)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        nx.draw_networkx_edges(graph, pos)
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()
