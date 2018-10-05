NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

'''
def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    New_lst = []
    for i in names:
        if i.title() not in  New_lst:
            New_lst.append(i.title())        
    return New_lst


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    lst = []

    nw = []
    names = dedup_and_title_case_names(names)
    for i in names:
        lst.append(tuple(i.split(' ')))
    sortedlst = sorted(lst,reverse=True,key=takeSecond)
    for i  in sortedlst :
        nw.append(i[0]+' '+i[1])
    return nw


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    lst = []

    nw = []
    names = dedup_and_title_case_names(names)
    for i in names:
        lst.append(tuple(i.split(' ')))
    sortedlst = sorted(lst,key=takeone)
    for i  in sortedlst :
        nw.append(i[0]+' '+i[1])
    return nw

def takeSecond(elem):
    return elem[1]

def takeone(elem):
    return elem[0]'''
def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    for name in names:
    return list({name.title() for name in names})


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names,
                  key=lambda x: x.split()[-1],
                  reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    names = [name.split()[0] for name in names]
    return min(names, key=len)


names1 = dedup_and_title_case_names(NAMES)
print (names1)
#sort_by_surname_desc(names1)
#print(shortest_first_name(names1))

