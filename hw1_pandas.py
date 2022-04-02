"""
Name:Sidhartha Amperayani
"""
from matplotlib import pyplot as plt
import networkx as nx
import pandas as pd


def read_file(file_path):
    """
    Returns the dataframe computed from the CSV file
    :param file_path:
    :return:
    """
    df = pd.DataFrame(pd.read_csv(file_path, delimiter=';'))
    return df

# print(read_file('student-mat.csv'))

def normalize(r):
    """
    Returns the normalized version of a single row entry
    :param r:
    :return: r
    """
    # school=r['school']
    # school_flag=[]
    if r['school'] == 'GP':
        r['school'] = 1
    else:
        r['school'] = 0
    if r['sex'] == 'F':
        r['sex'] = 0
    else:
        r['sex'] = 1
    if r['address'] == 'U':
        r['address'] = 0
    else:
        r['address'] = 1
    columns = ['school', 'sex', 'age', 'address', 'Medu', 'Fedu', 'traveltime', 'studytime',
               'failures', 'G1', 'G2', 'G3']
    r = r[columns]
    return r

def distance(u, v):
    """
    Computes the euclidean distance between 2 normalized rows
    :param u: Row 1
    :param v: Row 2
    :return: Distance between u and v
    """
    sum_of_squares = 0
    for i in range(len(u)):
        u_comp = u[i]
        v_comp = v[i]
        difference = abs(u_comp - v_comp)
        sum_of_squares += difference ** 2
    return sum_of_squares ** (1 / 2)

def compute_min_list(df):
    """
    Computes the minimum distanced row for each index in the dataframe
    :param df:
    :return: List of tuple pairs
    """
    list_of_pairs = []
    # pointer=0
    for i in range(len(df)):
        r1 = normalize(df.iloc[i])
        distance_dict = {}
        # pointer2=0
        # print('Index:',i)
        print('Processing Distance for Index:', i)
        for j in range(len(df)):
            r2 = normalize(df.iloc[j])
            if i == j:
                # print("Here")
                # print(i, j)
                continue
            distance_dict[j] = distance(r1, r2)
            # pointer2+=1
            # print(j)
            # print('Distance:',distance(r1,r2))
        min_val_dict = min(distance_dict, key=distance_dict.get)
        # print(distance_list)
        list_of_pairs.append((i, min_val_dict))
        # k=min(distance_dict)
        print('Minimum Distance is from Index:', min_val_dict)
        print('Min distance:', distance_dict[min_val_dict])
    return list_of_pairs

def compute_graph(pair_list):
    """
    Using the pair list, compute the graph
    :param pair_list:
    :return: Graph
    """
    G = nx.Graph()
    for i in range(len(pair_list)):
        G.add_node(i)
        G.add_edge(pair_list[i][0], pair_list[i][1])
    return G

def main():
    df = read_file('student-mat.csv')
    list_of_pairs = compute_min_list(df)
    graph = compute_graph(list_of_pairs)
    plt.figure(figsize=(45, 40))
    nx.draw_spring(graph, node_size=2000, width=9, with_labels=True, font_size=22)
    plt.draw()
    plt.savefig("graph.svg")


if __name__ == '__main__':
    main()
