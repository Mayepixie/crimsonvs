from backend.cards.BaseCard import BaseCard


class Unit(BaseCard):

    def __init__(self, card_id, name, junction, junction_description, junction_state, characters, charisma_cost, trinity, rarity):
        self.card_type = "unit"
        BaseCard.__init__(self, card_id, name, self.card_type, junction, junction_description, junction_state, trinity, rarity)
        self._charisma_cost = charisma_cost
        self._characters = characters

    @property
    def cost(self):
        return self._charisma_cost

    @cost.setter
    def cost(self, new_cost):
        self._charisma_cost = new_cost

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, list_of_characters):
        for char in list_of_characters:
            self._characters.append(char)
