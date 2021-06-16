from core.pyba_logic import PybaLogic


class StoreLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getStoreById(self, id):
        database = self.createDatabaseObj()
        sql = f"select * from store where store_id={id};"
        result = database.executeQuery(sql)
        return result

    def insertStore(self, store):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `sakila`.`store`"
            + f"(`store_id`,`manager_staff_id`,`address_id`,`last_update`) "
            + f"VALUES(0, {store['manager']}, {store['address']}, "
            + f"{store['lastUpdate']}"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateStore(self, id, store):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE `sakila`.`store` "
            + f"SET `manager_staff_id` = '{store['manager']}', `address_id`` = '{store['address']}', "
            + f"`last_update` = {store['lastUpdate']} "
            + f"WHERE `store_id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteStore(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from store where store_id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows
