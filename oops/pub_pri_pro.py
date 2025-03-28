class Access:
    pub = 10
    _pro = 12
    __pri = 13

    def __init__(self,a,b,c):
        self.pub=a
        self._pro=b
        self.__pri=c

    def get_public(self):
        print(self.pub,self._pro,self.__pri)

    def _get_pro(self):
        print(self.pub,self._pro,self.__pri)

    def __get_private(self):
        print(self.pub,self._pro,self.__pri)

    @staticmethod
    def __get_value():
        return Access.__pri


obj = Access(1,2,3)

obj.get_public() #access public mrthod
obj._get_pro() # acess protected method
obj._Access__get_private() ##access private method using object

##important
print(Access.pub , Access._pro , Access._Access__get_value() )
