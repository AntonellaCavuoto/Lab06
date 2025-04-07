from flet_core import row

from database.DB_connect import DBConnect
import mysql.connector

from model import retailer


class DAO():
    def __init__(self):
        pass

    def getAnno(self):
        a = []
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="go_sales")

        cursor = cnx.cursor()
        query = """select YEAR(Date)
                    from go_daily_sales """
        cursor.execute(query)

        for row in cursor:
            if a.__contains__(row) == False:
                a.append(row)
        cnx.close()

        a.sort()
        a_normal = [x[0] for x in a]

        return a_normal

    def getBrand(self):
        a = []
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """select Product_brand
                from go_products"""

        cursor.execute(query)

        for row in cursor:
            if a.__contains__(row) == False:
                a.append(row)
        cnx.close()

        a.sort()
        a_normal = [x[0] for x in a]

        return a_normal

    def getRetailer(self):
        a = []
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = """select * 
                from go_retailers"""
        cursor.execute(query)
        for row in cursor:
            r = retailer.Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row["Country"])
            a.append(r)

        a.sort(key=lambda x: x.name)
        cnx.close()
        return a

    def getTopVendite(self, anno, brand, ret):
        # WHERE product_number = COALESCE(%s, product_number)
        a = []
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="go_sales")
        cursor = cnx.cursor(dictionary = True)
        query = """select year(s.Date) as anno,
                p.Product_brand as brand,
                r.Retailer_name as retailer,
                s.Unit_sale_price *s.Quantity as ricavo,
                p.Product_number as numProd,
                r.Retailer_code as numRet,
                s.Date as data
                
                from go_daily_sales s
                join go_products p on s.Product_number = p.Product_number 
                join go_retailers r on s.Retailer_code = r.Retailer_code 
                
                where
                year(s.Date) = coalesce (%s, year(s.Date)) and
                p.Product_brand = coalesce (%s, p.Product_brand)and
                r.Retailer_name = coalesce (%s, r.Retailer_name)
                
                order by ricavo desc 
                limit 5"""

        cursor.execute(query, (anno, brand, ret))

        for row in cursor:
            formatted_row = f"Data: {row['data']}; Ricavo: {row['ricavo']}; Retailer: {row['numRet']}; Product: {row['numProd']}"
            a.append(formatted_row)

        return a

    def getAnalisiVendite(self, anno, brand, ret):
        a = []
        ricavi = 0
        nRet = []
        nProd = []
        cnx = mysql.connector.connect(  # creo la connessione
            user="root",
            password="AticniviR1121!",
            host="127.0.0.1",
            database="go_sales")
        cursor = cnx.cursor(dictionary=True)

        query = """select year(s.Date) as anno,
                p.Product_brand as brand,
                r.Retailer_name as retailer,
                s.Unit_sale_price *s.Quantity as ricavo,
                p.Product_number as numProd,
                r.Retailer_code as numRet,
                s.Date as data
                
                from go_daily_sales s
                join go_products p on s.Product_number = p.Product_number 
                join go_retailers r on s.Retailer_code = r.Retailer_code 
                
                where
                year(s.Date) = coalesce (%s, year(s.Date)) and
                p.Product_brand = coalesce (%s, p.Product_brand)and
                r.Retailer_name = coalesce (%s, r.Retailer_name)
                
                order by ricavo desc"""

        cursor.execute(query, (anno, brand, ret))

        for row in cursor:
            ricavi += row['ricavo']

            if not nRet.__contains__(row['retailer']):
                nRet.append(row['retailer'])

            if not nProd.__contains__(row['numProd']):
                nProd.append(row['numProd'])

            a.append(row)

        formatted_row = f"Giro d'affari: {ricavi}\n" \
                        f"Numero vendite: {len(a)}\n" \
                        f"Numero retailers coinvolti: {len(nRet)}\n" \
                        f"Numero prodotti coinvolti: {len(nProd)}"
        return formatted_row


if __name__ == "__main__":
    mydao = DAO()
    print(mydao.getAnalisiVendite("2017", "Star", "Grand choix"))
    print(mydao.getAnalisiVendite(None, None, None))

