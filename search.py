import queue

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    stack = util.Stack()
    visited = []
    
    start_node = (problem.getStartState(), [], [])
    stack.push(start_node)
    
    while not stack.isEmpty():
        current , path , cost = stack.pop()
        if (problem.isGoalState(current)):      # An o current node einai o kombos einai aytos poy psaxnoyme
            return path
        if (current not in visited):            # An den exoyme episkeftei ayton ton kombo
            visited.append(current)             # kanton visited
            for newcurrent , newpath , newcost in problem.getSuccessors(current):       # Gia oloys toys geitones toy current
                stack.push((newcurrent,path + [newpath],cost + [newcost]))              # prosthese toys sthn lista gia na eksetastoyn

    
    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    q = util.Queue()
    visited = []
    start_node = (problem.getStartState(), [], [])
    q.push(start_node)                                          
                                                                                                                                                    
    while not q.isEmpty():                                      # Oysiastika ayto poy allazei apo tin ylopoihsh
        current , path , cost = q.pop()                         # se sxesh me to dfs einai oti allazoyme tin ylopoish me Stack   
        if (problem.isGoalState(current)):                      # se ylopoihsh me Queue 
            return path
        if (current not in visited):            
            visited.append(current)             
            for newcurrent , newpath , newcost in problem.getSuccessors(current): 
                q.push((newcurrent,path + [newpath],cost + [newcost]))             
    
    
    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    #
    
    Path_Cost = util.Counter()              # Oysiastika o algorithmos poy ylopoihsa xrisimopoiei tin bfs ylopoihsh
    q = util.PriorityQueue()                # kai psaxnei na brei ton node Goal-State mesa apo ta diafora monotapia poy mporei na prokeipsoyn
                                            # Krataw se enan pinaka to cost toy xreiazomai gia na ftasw se enan kombo X , prosthetontas ston sygkekrimeno 
    visited = []                            # kombo to kostos poy exw metrisei hdh apo toys komboys poy perasa gia na ftasw ston X + to kostos toy node (X-1) - > X.
    start_node = (problem.getStartState(), [])
    q.push(start_node,0)                                          
                                                                                                                                                    
    while not q.isEmpty():                                    
        current , path = q.pop()                  
        if (problem.isGoalState(current)):        
            return path
        if (current not in visited):            
            visited.append(current)   
            
            for newcurrent , newpath , newcost in problem.getSuccessors(current):   # To kostos toy child-node(newcurrent) isoytai me to athrisma 
                Path_Cost[newcurrent] = Path_Cost[current] + newcost                # toy kostoys toy parent-node(current) + to kostos ths akmhs patera-paidioy
                q.push((newcurrent,path + [newpath]),Path_Cost[newcurrent]) 
            # Xrisimo print gia katanohsh kwdika.
            #print("Current = " , current , Path_Cost)
    
    
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    path_actions = []
    
    q = util.PriorityQueue()
    visited = []
    start_node = problem.getStartState()
    start_heuristic = heuristic(start_node,problem) 
    q.push((start_node , [] , 0) , start_heuristic)                                           
                                                                                                         
    while not q.isEmpty():                    
        current , path , cost = q.pop()                        
        if (problem.isGoalState(current)):                      
            return path
        if (not current in visited):            
            visited.append(current)
              
            
            for newcurrent , newpath , newcost in problem.getSuccessors(current):               
                if (not newcurrent in visited):
                    
                    path_actions = list(path) + [newpath]
                    path_cost = problem.getCostOfActions(path_actions)
                    
                    q.push((newcurrent,path_actions , 0) , path_cost + heuristic(newcurrent,problem))
                
    

    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
