
from backend import DB_PATH


class User(object):
    def __init__(self, name):
        self._name = name
        self._id = None
        self._gallery_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def gallery_id(self):
        return self._gallery_id

    @gallery_id.setter
    def gallery_id(self, value):
        self._gallery_id = value

    def setup_gallery(self):
        import sqlite3
        from backend import DB_PATH

        db_con = sqlite3.connect(DB_PATH)
        with db_con:
            db_cursor = db_con.cursor()

            db_cursor.execute('''SELECT * FROM crimsonvs_card''')
            cards = db_cursor.fetchall()

            to_insert = []
            identifier = 1
            for card in cards:
                statement = (identifier, self.gallery_id, 0, card[0], self.id)
                to_insert.append(statement)
                identifier += 1

            db_cursor.executemany('''
                INSERT INTO crimsonvs_gallery(id, gallery_id, count, card_id, user_id)
                    VALUES (?, ?, ?, ?, ?);
            ''', to_insert)

        db_con.close()

    def create_deck(self):
        pass

    def get_deck(self):
        pass
