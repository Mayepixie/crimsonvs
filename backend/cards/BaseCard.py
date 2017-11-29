

class BaseCard(object):
    def __init__(self, card_id, name, card_type, junction, junction_description, junction_state, trinity, rarity):
        """
        Base version of all cards, sets up certain information that all cards share.

        :param name: Name of card
        :param card_type: General or Unit
        :param attribute: Snipe, Assault or Shield

        """
        self._id = card_id
        self._name = name
        self._card_type = card_type
        self._trinity = trinity
        self._junction = junction
        self._junction_description = junction_description
        self._junction_state = junction_state
        self._rarity = rarity
        self._image_path = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, card_id):
        self._id = card_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, new_type):
        self._card_type = new_type

    @property
    def trinity(self):
        return self._trinity

    @trinity.setter
    def trinity(self, trinity):
        self._trinity = trinity

    @property
    def junction(self):
        return self._junction

    @junction.setter
    def junction(self, junction):
        self._junction = junction

    @property
    def junction_description(self):
        return self._junction_description

    @junction_description.setter
    def junction_description(self, new_description):
        self._junction_description = new_description

    @property
    def junction_state(self):
        return self._junction_state

    @junction_state.setter
    def junction_state(self, junction_state):
        self._junction_state = junction_state

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, rarity):
        self._rarity = rarity

    @property
    def image(self):
        return self._image_path

    @image.setter
    def image(self, path):
        self._image_path = path
