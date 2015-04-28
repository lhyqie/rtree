# input is a trajectory Q  and a couple of trajectory S to query on
from matplotlib.pyplot import figure

# each trajectory is a sequence of points
# each point is (x,y)

q = [(1,1),(2,2),(3,3)]

S = []
S.append([(1,0),(2, 3),(2,3)])
S.append([(1,3),(2, 4),(5, 3.8)])
S.append([(1,1.5),(2, 6),(3, 7)])
print q

for t in S : # for  each trajaetory in S, 
    print t

# Given multiple query points, a k-BCT query finds k closest trajectories to the set  of query points.
# The distance Distq between a query location qi and a trajectory R = {p1, p2, . . . , pl} is defined as:
# (2.2)

def point_distance(p1, p2): 
    """
    euclidean distance between two points
    """
    from math import sqrt
    return sqrt((p1[0] - p2[0]) **2  + (p1[1] - p2[1]) **2)

def point_traj_distance(p1, t): 
    """
    distance between one point p1 and a trajectory t
    is the minimum distance of p1 to each point p2 in t
    refer to Equation (2.2)
    """
    min_dist = 99999
    for p2 in t:
        dist = point_distance(p1, p2)
        if dist < min_dist:
            min_dist = dist
    return min_dist

def traj_sim(t1, t2): 
    """
        similarity of two trajectories is defined as (2.3)
    """
    from math import exp
    sum = 0
    for p1 in t1:
        dist = point_traj_distance(p1, t2)
        sum += exp(-dist)
    return sum
    
def t_query(q, S):
    #find the k - closest traj in S for Q
    for t in S:
        print 'distance between ', q, ' and ', t,  ' is ' ,traj_sim(q, t)

t_query(q, S)

import matplotlib.pyplot as plt
zipq = zip(*q)
plt.figure(figsize=(10,5))
plt.plot(zipq[0], zipq[1], '-bo')
plt.text(zipq[0][-1], zipq[1][-1] + 0.2, s="q")
for i, t in enumerate(S):
    zipt = zip(*t)
    plt.plot(zipt[0], zipt[1], '-rx')
    plt.text(zipt[0][-1], zipt[1][-1] + 0.2, s="trajectory"+str(i))
plt.xlim([0,8])
plt.ylim([-1,8])
plt.show()

