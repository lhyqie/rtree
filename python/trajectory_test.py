# input is a trajectory Q  and a couple of trajectory S to query on

# each trajectory is a sequence of points
# each point is (x,y)

q = [(1,1),(2,2),(3,3)]

S = []
S.append([(1,0),(0,2),(2,3)])
S.append([(1,1),(0,2.5),(2,3.5)])
S.append([(1,1.5),(1,2),(3,3)])
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

# k Best-Connected Trajectories

t_query(q, S)
