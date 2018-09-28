from node import Node
import math 

class MonteCarlo(object):
    baseTree = []
    researchTree = []
    ponderationValue = 2

    def setBaseTree(self, newBaseTree):
        self.baseTree = newBaseTree

    def setReasearchTree(self, newResearchTree):
        self.researchTree = newResearchTree

    def getResearchTree(self):
        return self.researchTree

    def getNodeByIndex(self, index):
        for node in self.researchTree:
            if node.index == index:
                return node
        return 0   

    #Si l'arbre de recherche à été complètement exploré
    def isTotallyExplored(self):
        if self.baseTree.count == self.researchTree.count:
            return True
        else:
            return False

    #Simule de façon récursive
    def simulate(self, count):
        if count == 0 or self.isTotallyExplored():
            return

        currentNode = self.descent(self.baseTree[0])
        self.growth(currentNode)
        self.rollOut()
        self.update()

    #Descente dans l'arbre de base
    #Si on arrive à une feuille, on retourne la rootNode
    #Si une des node enfants n'est pas explorées, on la retourne
    #Sinon calcul de l'UBC sur tous les enfants puis ré-appel de la fonction sur la nouvelle rootNode
    def descent(self, rootNode):
        selectedNode = rootNode
        currentUBC = -math.inf
        
        #Si feuille
        if rootNode.getChildCount() == 0:
            return rootNode

        #Si tous les childrens n'ont pas été exploré, retourner le plus à gauche non exploré
        #Sinon calcul de l'Upper Bound Confidence
        for node in rootNode.getChildren:
            if node.isExplored == False:
                return rootNode
            else :
                ubc = node.getScore + math.sqrt(self.ponderationValue*(math.log(rootNode.getPassCount() / node.getPassCount())))
                if ubc > currentUBC:
                    ubc = currentUBC
                    selectedNode = node
                    
        self.descent(selectedNode)
        return 0

    #Agrandir l'arbre de recherche
    def growth(self, currentNode):
        nouvelleNode = Node(len(self.researchTree))
        nouvelleNode.setScore(0)

        #Si currentNode n'est pas exploré
        if currentNode.isExplored == False:
            self.researchTree.append(nouvelleNode)
            return

        for node in currentNode.getChildren:
            ##Si node pas exploré, on créé nouvelle puis rajout dans l'arbre de recherche
            if node.isExplored == False:
                nodeInResearchTree = self.getNodeByIndex(currentNode.index)
                nodeInResearchTree.childrens.append(nouvelleNode)

        return
                
    def rollOut(self):
        print("rollOut")

    def update(self):
        print("update")

    