class Matrice:
    def __init__(self, nbcolonne = 3, nbligne = 3, data = list(range(9))):
        self.__nbcolonne = nbcolonne
        self.__nbligne =nbligne
        self.__data = data
    @property
    def nbcolonne (self):
        return self.__nbcolonne

    @property
    def nbligne (self):
        return self.__nbligne

    @property
    def data (self):
        return self.__data

    def __str__(self):
        txt = ""
        for i in range(self.__nbligne) :
            for j in range(self.__nbcolonne):
                txt += str(self.__data[i*self.__nbcolonne*j]) + "/t"
            txt += "/n"
        return txt

    def __add__(self, m):
        if isinstance(m, Matrice):
            if (m.__nbligne == self.__nbligne and m.__nbcolonne == self.__nbcolonne):
                obj = Matrice()
                for i in range(self.__nbligne):
                    for j in range(self.__nbcolonne):
                        obj.data[i * self.__nbcolonne * j] = self.data[i*self.__nbcolonne + j] + m.data[i*self.__nbcolonne+j]
                return
        elif isinstance(m,int) or isinstance(m,float):
            m= Matrice()
            for i in range(self.__nbligne):
                for j in range(self.nbcolonne):
                    m.data[i*self.__nbcolonne+j] = self.__data[i*self.__nbcolonne+j] + m
            return m
        elif isinstance(m, list):
            if len(obj) == self.__nbcolonne*self.__nbligne):




m1 = Matrice()
m2 = Matrice()
m = m1 +list(range(9))
print(m)