

class TooMuchCharisma(Exception):
    def __init__(self, message):
        super(TooMuchCharisma, self).__init__(message)
        self._error_message = message


class NotEnoughUnits(Exception):
    def __init__(self, message):
        super(NotEnoughUnits, self).__init__(message)
        self._error_message = message


class Deck(object):
    """
    A representation of a Deck
    """
    def __init__(self, deck_id, user, units, general):
        """

        :param deck_id: ID of deck
        :type deck_id: int
        :param user: User who owns/will own Deck
        :param user: User Object
        :param units: dict with Unit Objects, paired with keys <1>, <2>, and <3>
        :type units: dict - {'1': <unit_id>, '2': <unit_id>, '3': <unit_id>}
        :param general: General
        :type general: General Object
        """
        self._deck_id = deck_id
        self._user = user
        self._units = units
        self._general = general
        self._current_charisma_total = self.charisma_total()
        self._turn_block_count = 0

    @property
    def deck_id(self):
        return self._deck_id

    @deck_id.setter
    def deck_id(self, deck_id):
        self._deck_id = deck_id

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def units(self):
        """
        Gets deck's Units
        :return: dict of Unit Objects
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets decks Unit cards
        :param units: dict of Unit objects
        :return: None
        """
        self._units = units

    @property
    def general(self):
        """
        Gets deck's General
        :return: General Object
        """
        return self._general

    @general.setter
    def general(self, general):
        """
        Sets deck's General
        :param general: General object
        :return: None
        """
        self._general = general

    @property
    def current_charisma_total(self):
        return self._current_charisma_total

    @current_charisma_total.setter
    def current_charisma_total(self, value):
        self._current_charisma_total = value

    @property
    def turn_block_count(self):
        return self._turn_block_count

    @turn_block_count.setter
    def turn_block_count(self, value):
        self._turn_block_count = value

    def charisma_total(self):
        if self.general and self.units:
            cost = 0
            for unit in self.units:
                cost += unit.charisma
            return cost
        return None

    def add_deck_to_db(self, deck_id, user_id, units, general):
        """
        Adds deck into the decks.db
        :param deck_id:
        :param user_id:
        :param units:
        :param general:
        :return:
        """
        import sqlite3 as lite
        from backend import DB_PATH

        db = lite.connect(DB_PATH)
        with db:
            db_cursor = db.cursor()

            question = "INSERT OR REPLACE INTO deck VALUES " \
                       "('{deck_id}', '{user_id}', '{unit_1}', '{unit_2}', '{unit_3}', '{general}')"
            db_cursor.execute(
                question.format(
                    deck_id,
                    user_id,
                    units['1'].id,
                    units['2'].id,
                    units['3'].id,
                    general.id))
        db.close()

        return Deck(deck_id, user_id, units, general)

    @classmethod
    def create_deck(cls, deck_id, user_id, units=None, general=None):
        """
        Creates deck
        :param deck_id:
        :param user_id:
        :param units:
        :param general:
        :return:
        """
        cls._validate_units(units)
        cls._validate_general(general)
        deck = cls.add_deck_to_db(deck_id, user_id, units, general)
        return deck

    def _validate_units(self, units):
        from backend import Unit

        if not all(position in units for position in ('1', '2', '3')):
            raise NotEnoughUnits("units dict must have the positional keys as follows: "
                                 "{'1': <Unit>, '2': <Unit>, '3': <Unit>}")
        for unit in units:
            if not isinstance(units[unit], Unit) or units[unit] is not None:
                raise TypeError('unit has wrong type. Must be Unit object or None for no unit in deck position')

    def _validate_general(self, general):
        from backend import General

        if not isinstance(general, General) or general is not None:
            raise TypeError('general has wrong type. Must be General object or None for no general in deck')

    def replace_deck_unit(self, new_unit, position):
        """
        Replaces unit in deck if new total Charisma Cost doesn't exceed General's Charisma
        :param new_unit: new unit object to add
        :param position: Position in deck - string
        :return: None?
        """
        self.units = self.units

        if not self.units or self.units[position]:
            self.units[position] = new_unit
        elif self.current_charisma_total - self.units[position].charisma + new_unit.charisma <= self.general.charisma:
            raise TooMuchCharisma("The new Charisma Cost total would exceed the Charisma of your General!")
        else:
            del self.units[position]
            self.units[position] = new_unit
