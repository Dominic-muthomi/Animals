class animal:
    def __init__(self, name, __multicellular, __heterotrophic, __canMove):
        self.name = name
        self.multicellular = __multicellular
        self.heterotrophic = __heterotrophic
        self.canMove = __canMove

class mammal(animal):
    def __init__(self, name, __multicellular, __heterotrophic, __canMove, __warmBlooded, __mammaryGlands):
        super().__init__(self, name, __multicellular, __heterotrophic, __canMove)
        self.warmBlooded = __warmBlooded
        self.mammaryGlands = __mammaryGlands

class amphibians(animal):
     def __init__(self, name, __multicellular, __heterotrophic, __canMove, __smoothSkin, __coldBlooded, __fertilizeExternally):
        super().__init__(self, name, __multicellular, __heterotrophic, __canMove)
        self.smoothSkin = __smoothSkin
        self.coldBlooded = __coldBlooded
        self.fertilizeExternally = __fertilizeExternally

class reptiles(animal):
      def __init__(self, name, __multicellular, __heterotrophic, __canMove, __smoothSkin, __coldBlooded, __haveScales, __fertilizeExternally):
         super().__init__(self, name, __multicellular, __heterotrophic, __canMove)
         self.smoothSkin = __smoothSkin
         self.coldBlooded = __coldBlooded
         self.fertilizeExternally = __fertilizeExternally
         self.haveScales = __haveScales
      def swimEfficiently(self):
          if self.havescales:
              self.haveScales = self.swimEfficiently
              return self.swimEfficiently() 
      def getname(self):
          return self.name          

class birds(animal):
      def __init__(self, name, __multicellular, __heterotrophic, __canMove, __haveScales, __warmBlooded, __layEggs, __haveBeaks):
          super().__init__(self, name, __multicellular, __heterotrophic, __canMove)
          self.haveScales = __haveScales
          self.warmBlooded = __warmBlooded
          self.layEggs = __layEggs
          self.haveBeaks = __haveBeaks
      def canFly(self):
          self.canFly = True  
          if self.haveFeathers:
              self.haveFeathers = self.canFly
              return self.canFly
      def getname(self):
          return self.canFly

      def getname(self):
          return self.name

      def setname(self,newBird):
          self.name = newBird

          newBird = birds("crow","multicellular","heterotrophic","canMove","haveScales","warmBlooded","layEggs","haveBeaks")
          







         

             


