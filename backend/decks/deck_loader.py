import sqlite3 as lite


class DeckLoader:

    DB_PATH = 'data/decks.db'

    DECK_ID_QUERY = "SELECT * FROM deck WHERE deck_id IS '{}'"
    USER_ID_QUERY = "SELECT * FROM deck WHERE user_id IS '{}'"

    @classmethod
    def by_id(cls, deck_id):
        """
        Fetches and instantiates an existing deck

        @param deck_id: the id of the deck to fetch based on deck id
        @type deck_id: int

        @returns: Deck Object
        @returntype: decks.Deck
        """
        cls._validate_id(deck_id)
        return cls._get_deck(cls.DECK_ID_QUERY, deck_id)

    @classmethod
    def by_user_id(cls, user_id):
        """
        Fetches and instantiates an existing deck based on user id

        @param user_id: the id of the deck to fetch
        @type user_id: int

        @returns: Deck Object
        @returntype: decks.Deck
        """
        cls._validate_id(user_id)
        return cls._get_deck(cls.USER_ID_QUERY, user_id)

    @staticmethod
    def _get_from_db_by_query(query):
        from backend import DECKS_DB_PATH
        db = lite.connect(DECKS_DB_PATH)
        with db:
            db_cursor = db.cursor()

            try:
                cursor_object = db_cursor.execute(query)
                return cursor_object.fetchone()
            except:
                pass
        db.close()

    @staticmethod
    def _validate_id(id_to_check):
        """ Checks if id_to_check is a integer """
        try:
            int(id_to_check)
        except Exception:
            raise ValueError("id must be a integer!")

    @classmethod
    def _get_deck(cls, by_method, id_to_check):
        from backend import Deck

        row = cls._get_from_db_by_query(by_method.format(id_to_check))

        if row:
            from backend.cards.card_loader import CardLoader
            cards_dict = CardLoader.get_by_ids([row[2], row[3], row[4], row[5]])

            units = {'1': None, '2': None, '3': None}
            for unit in cards_dict['units']:
                if row[3] == unit.id:
                    units['1'] = unit
                elif row[4] == unit.id:
                    units['2'] = unit
                elif row[5] == unit.id:
                    units['3'] = unit

            return Deck(deck_id=row[0],
                        user=row[1],
                        units=units,
                        general=cards_dict['general'])
        return None
