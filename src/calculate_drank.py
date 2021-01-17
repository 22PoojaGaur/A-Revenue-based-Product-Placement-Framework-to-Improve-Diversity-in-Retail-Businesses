from __future__ import division


def calculate_nodes_in_projection(patterns, ch_dict=None):
    if ch_dict is None:
        raise ValueError
    nodes_in_proj = set()

    for item in patterns:
        path = set(ch_dict[item.replace(' ', '_')])
        # print  [node.value for node in path]
        nodes_in_proj = nodes_in_proj | path
    return len(nodes_in_proj)


def calculate_drank(patterns, ch_dict=None, ch_height=None):
    if ch_dict is None or ch_height is None:
        raise ValueError

    num_node_in_proj = calculate_nodes_in_projection(patterns, ch_dict=ch_dict)-1
    num_item_in_pat = len(patterns)
    h = ch_height-1

    try:
        drank = (num_node_in_proj - (num_item_in_pat + h - 1)) / (
            (h-1)*(num_item_in_pat -1))
    except ZeroDivisionError as e:
        # print ("height", str(h-1))
        # print ("num items ", str(len(patterns)))
        drank = 0

    return drank


def get_dranks(freq_patterns, item_path_dict):
    '''
    Args -
        freq_patterns: List. list of itemsets
        item_path_dict: Dict. Info of CH {item -> [nodes from root to item in CH]}
    '''
    ch_height = 0
    for item in item_path_dict.keys():
        if len(item_path_dict[item]) > ch_height:
            ch_height = len(item_path_dict[item])

    dranks = {}
    for patterns in freq_patterns:
        try:
            # calculate drank
            dranks[patterns] = calculate_drank(patterns, ch_dict=item_path_dict, ch_height=ch_height)
        except KeyboardInterrupt:
            print('Drank calculation SKIPPED for ' + ' '.join(patterns))

    return dranks
    #print (sorted(dranks.items, key=lambda x: x[1], reverse=True)
