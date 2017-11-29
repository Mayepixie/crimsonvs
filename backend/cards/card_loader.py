import sqlite3 as lite
from sqlite3 import Error as LiteError


class CardLoader:
    DB_PATH = 'data/cards.db'

    CARD_QUERY = "SELECT * FROM cards WHERE card_id IS '{}'"
    # CARDS_QUERY = "SELECT * FROM cards WHERE card_ID in '({})'"

    @classmethod
    def get_by_id(cls, card_id):
        """
        Fetches and instantiates an existing deck

        @param card_id: the id of the deck to fetch based on deck id
        @type card_id: int

        @returns: Card Object
        @returntype: cards.Card
        """
        from backend.utils import validate_id

        if not card_id:
            return None

        validate_id(card_id)
        return cls._get_card(cls.CARD_QUERY.format(card_id))

    @classmethod
    def get_by_ids(cls, ids):
        """
        Fetches multiple cards and returns them as lists in a dict
        Example: {'generals': [General Object], 'units': [Unit Object]}

        :param ids: list of card ids
        :return: dict with lists of Generals and Units
        """
        from backend.utils import validate_id

        for card_id in ids:
            if card_id:
                validate_id(card_id)
        card_list = []
        for card_id in ids:
            card = cls._get_card(cls.CARD_QUERY.format(card_id))
            card_list.append(card)
        if not card_list:
            return None

        cards = {'generals': [], 'units': []}
        for card in card_list:
            if card.card_type == "general":
                cards['generals'].append(card)
            else:
                cards['units'].append(card)
        return cards

    @staticmethod
    def _get_from_db_by_query(query):
        from backend import DECKS_DB_PATH
        db = lite.connect(DECKS_DB_PATH)
        with db:
            db_cursor = db.cursor()

            try:
                cursor_object = db_cursor.execute(query)
                return cursor_object.fetchone()
            except LiteError:
                pass
        db.close()

    @classmethod
    def _get_card(cls, query):
        from backend import Unit, General
        from backend.abilities.abilities import get_ability_description

        row = cls._get_from_db_by_query(query)

        if row:
            if row[1] == "general":  # row[1] is card type in cards.sqlite
                return General(card_id=row[0],
                               name=row[2],
                               junction=row[3],
                               junction_description=get_ability_description(row[4]),
                               junction_state= True if row[3] else False,
                               charisma=row[4],
                               hp=row[5],
                               ap=row[6],
                               trinity=row[9],
                               rarity=row[10])
            else:
                return Unit(card_id=row[0],
                            name=row[2],
                            junction=row[3],
                            junction_description=get_ability_description(row[4]),
                            junction_state=True if row[3] else False,
                            characters=row[7],
                            charisma_cost=row[8],
                            trinity=row[9],
                            rarity=row[10])
        return None
