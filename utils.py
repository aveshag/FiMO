import pandas as pd
import numpy as np
from ete3 import Tree
from ete3 import TreeStyle, TextFace, add_face_to_node

# return all edges of given tree
def get_edges(tree):
    # storing branch ID's
    branch_id = {}
    # storing all edges
    edge_lst = []
    # branch_time_list is the branch length of sub tree
    branch_time_lst = []
    branch = 0
    for node in tree.iter_descendants('preorder'):
        branch_id[node.name] = branch 
        edge_lst.append((node.up.name, node.name))
        branch_time_lst.append(node.dist)
        branch += 1

    edges = {}
    edges['branch_id'] = branch_id
    edges['edge_lst'] = edge_lst
    edges['branch_time_lst'] = branch_time_lst
    return edges

# return descendants of every tree's node
def get_descendants(tree, branch_id):
    desc_leaves = {}
    desc_branches = {}
    branch = 0
    for node in tree.iter_descendants('preorder'):
        desc_leaves[branch] = node.get_leaf_names()
        desc_branches[branch] = []
        for desc in node.iter_descendants("preorder"):
            desc_branches[branch].append(branch_id[desc.name])
        branch += 1
    descendants = {}
    descendants['desc_leaves'] = desc_leaves
    descendants['desc_branches'] = desc_branches
    return descendants

# return ancestor branches of every tree's node
def get_ancestors(tree, branch_id):
    ancs_branches = {}
    branch = 0
    for node in tree.iter_descendants('preorder'):
        ancs_branches[branch] = []
        parent = node.up.name
        if parent != 'R':
            ancs_branches[branch].append(branch_id[parent])
            ancs_branches[branch] += ancs_branches[branch_id[parent]]
        branch += 1

    return ancs_branches

# append row in given dataframe
def append_row(dataf, col_name):
    dataf = dataf.append(pd.Series(0, index = col_name, dtype = int),  ignore_index = True)
    return dataf

# show tree in ETE Tree Browser
def show_tree(tree):
    t = tree.copy()
    ts = TreeStyle()
    ts.orientation = 1
    ts.rotation = 270
    def my_layout(node):
            F = TextFace(node.name, tight_text=True)
            add_face_to_node(F, node, column=0, position="branch-right")
    ts.layout_fn = my_layout
    ts.branch_vertical_margin = 15
    # ts.show_branch_length = True
    t.show(tree_style = ts)

