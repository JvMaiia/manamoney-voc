import android
from android.database.sqlite import SQLiteDatabase

class manamoneyDB(extends=android.database.sqlite.SQLiteOpenHelper):
    @super({
        context: android.content.Context,
        "com.jvmaiia.managing_money": java.lang.String,
        None: android.database.sqlite.SQLiteDatabase[CursorFactory],
        2: int
    })
    def __init__(self, context):
        pass

    def onCreate(self, db: android.database.sqlite.SQLiteDatabase) -> void:
        print('initiating manamoney database')
        db.execSQL(
            "CREATE TABLE sale ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "person TEXT NOT NULL,"
            "value INTEGER NOT NULL,"
            "payed BOOLEAN NOT NULL CHECK (payed IN (0,1)),"
            "products TEXT NOT NULL"
            "),"
            "CREATE TABLE product ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "name TEXT NOT NULL,"
            "quantity INTEGER NOT NULL,"
            "value INTEGER NOT NULL"
            ")"
        )

    def onUpgrade(self, db: android.database.sqlite.SQLiteDatabase,
                  oldVersion: int, newVersion: int) -> void:
        print('will upgrade database from', oldVersion, ' to', newVersion)
        raise NotImplementedError

    def create_product(self, item):
        values = ContentValues()
        values.put("name", name)
        values.put("value", value)
        values.put("quantity", quantity)
        db = self.getWritableDatabase()
        db.insertWithOnConflict("product", None, values, SQLiteDatabase.CONFLICT_REPLACE)
        db.close()

    def fetch_products(self):
        result = []

        db = self.getReadableDatabase()
        cursor = db.rawQuery("SELECT * FROM product", None)
        while cursor.moveToNext():
            product_id = int(cursor.getInt(cursor.getColumnIndex('id')))
            name = cursor.getString(cursor.getColumnIndex('name'))
            value = cursor.getInt(cursor.getColumnIndex('value'))
            quantity = cursor.getInt(cursor.getColumnIndex('quantity'))
            result.append(dict(id=product_id, name=name, value=int(value), quantity=int(quantity)))
        db.close()

        return result

    def changeQuantity_product(self, value):
        db = self.getWritableDatabase()
        product = db.rawQuery("SELECT * FROM product WHERE id=%d" % (value['id']), None).moveToFirst()
        quantity = product.getString(product.getColumnIndex('quantity'))
        f_quantity = quantity + int(item['quantity'])
        db.execSQL(
            "UPDATE product SET quantity=%d WHERE id=%d"%(f_quantity, value['id'])
        )
        db.close()