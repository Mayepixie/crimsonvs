from backend.cards.BaseCard import BaseCard


class General(BaseCard):
    def __init__(self, card_id, name, junction, junction_description, junction_state, charisma, hp, ap, trinity, rarity):
        """
        Representation of a General Card.

        :param general_id: ID of General Card
        :type general_id: int
        :param title: Name of General Card
        :type title: basestring
        :param hp: Health Points
        :type hp: int
        :param ap: Attack Points
        :type ap: int
        :param charisma: Max amount of Charisma Cost usage allowed by General
        :type charisma: int
        """
        self._card_type = "general"
        BaseCard.__init__(self, card_id, name, self.card_type, junction, junction_description, junction_state, trinity, rarity)
        self._hp = hp
        self._ap = ap
        self._charisma = charisma
        self._active_abilities = []

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_hp_value):
        self._hp = new_hp_value

    @property
    def ap(self):
        return self._ap

    @ap.setter
    def ap(self, new_ap_value):
        self._ap = new_ap_value

    @property
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, charisma):
        self._charisma = charisma

    @property
    def abilities(self):
        return self._active_abilities

    @abilities.setter
    def abilities(self, abilities):
        for ability in abilities:
            self._active_abilities.append(ability)

    @abilities.deleter
    def abilities(self):
        self.abilities = []

    def remove_abilities(self, abilities):
        for ability in abilities:
            if ability in self.abilities:
                self.abilities.remove(ability)
