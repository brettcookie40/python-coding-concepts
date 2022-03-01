#This is a python script exhibiting classes and subclasses

class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude
    
    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face

class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)
    
    def nurture_talent(self):
        #Good bosses nurture talent, it makes the employees happy
        print("The employees feel all warm and fuzzy then put their talents to good use!")

    def encourage(self):
        # Good bosses encourage their employees!
        print("The team cheers, starts shouting awesome slogans then gets back to work!")