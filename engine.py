import program_path
import networkx as nx

# do scc analysis
def scc(relations, rules):

    relation_graph = nx.DiGraph()

    for rule in rules:
        for body in rule[1:]:
            relation_graph.add_edge(body[0], rule[0][0])

    sccs = nx.condensation(relation_graph)
    sccs_topo = nx.topological_sort(sccs)

    result = []
    for c in sccs_topo:
        result.append(sccs.node[c]['members'])

    return result

# get rules of an scc component
def get_nonrec_rules(comp, rules):
    result = []

    for rule in rules:
        if rule[0][0] in comp:
            add = True
            for body in rule[1:]:
                if body[0] in comp:
                    add = False
            if add:
                result.append(rule)

    return result

# get recursive rules of an scc component
def get_rec_rules(comp, rules):
    result = []

    for rule in rules:
        if rule[0][0] in comp:
            add = False
            for body in rule[1:]:
                if body[0] in comp:
                    add = True
            if add:
                result.append(rule)

    return result

# evaluate datalog program
def evaluate(relations, rules, database):
    relation_sccs = scc(relations, rules)

    for comp in relation_sccs:
        # evaluate non-recursive rules
        for rule in get_nonrec_rules(comp, rules):


print(scc(program_path.relations, program_path.rules))
