import numpy as np

class NetworksAlgo:

    def channels_chain(transition_probability, network):
        nodes_num = np.size(transition_probability, 0)
        layers_num = np.size(network, 0) + 1
        network = np.insert(network, 3, values=1, axis=0)

        for current_layer in range(1, layers_num):
            incoming_layer = current_layer - 1
            for current_node in range(nodes_num):
                nodes_prob = {}
                for x in range(nodes_num):
                    nodes_prob[x] = network[incoming_layer, x] * \
                                    transition_probability[x, current_node]
                node_output = max(nodes_prob.values()) * network[current_layer, current_node]
                network[current_layer, current_node] = node_output
        return network[layers_num-1]