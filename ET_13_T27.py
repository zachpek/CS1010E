# Name: Pek Tze Hng, Zachary
# NUSNET ID: e1525681
# Question Number: 1

class Man:
    def __init__(self,name,dad=None):
        self.name = name    # of type string
        self.dad = dad      # of type Man
    def ancestor(self,other):    
        if self.name == other.name:
            return 0
        if not self.dad :
            return -1
        if self.dad.name == other.name:
            return 1
        grandy = self.dad.ancestor(other)
        if grandy >= 0:
            return grandy+1
        return -1
    def callme(self,other): 
        # returns what object "other" should call "self"
        # check sample run for detail
        self_ancestor_number = self.ancestor(other)
        other_ancestor_number = other.ancestor(self)
        if self_ancestor_number == 0:
            return 'me'
        elif self_ancestor_number >= 1:
            return 'son' + "'s son" * (self_ancestor_number - 1)
        else:
            if other_ancestor_number > 0:
                return "dad" + "'s dad" * (other_ancestor_number - 1)
        return 'who?'
