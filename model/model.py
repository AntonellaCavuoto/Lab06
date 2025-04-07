from database.DAO import DAO


class Model:
    def __init__(self):
        self.DAO = DAO()

    def getAnni(self):
        return self.DAO.getAnno()

    def getBrand(self):
        return self.DAO.getBrand()

    def getRetailer(self):
        return self.DAO.getRetailer()

    def getTopVendite(self, anno, brand, retailer):
        list = self.DAO.getTopVendite(anno, brand, retailer)
        print(list)
        return list

    def getAnalisiVendite(self, anno, brand, retailer):
        return self.DAO.getAnalisiVendite(anno, brand, retailer)





