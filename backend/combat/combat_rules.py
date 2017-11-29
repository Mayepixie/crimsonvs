

class CombatRules:
    """
    Snipe wins over Shield, Shield wins over Assault, and Assault wins over Snipe.
    This applies for Units and Generals.
    Unit card battles are resolved, before Generals are compared to see who begins.

    Units:
    Unit with winning attribute gets Charisma Cost increased by 1 point.
    Winning Unit is determined by highest Charisma Cost and remains in play,
        losing card is discarded from game (unless other ability brings it back into play).
    If Units have same Charisma Cost both cards are discared from game. (unless other ability brings it back into play).

    Generals:
    If General has winning attribute that User goes first.
    If left General and Right General have same attribute the one with the highest Charisma goes first.
    If both Generals have the same attribute and Charisma then the left General starts.

    After determining which User goes first then the remaining Units have applicable ablities performed, then starting
    General begins and applicable Unit abilities are again applied if there are any. General then attacks,
        and the turn is over. Then enemy General's surviving Units apply their abilities if applicable,
        General attacks and the turn is over. This process continues until one of the General's HP reaches 0 or 10 turns
        have passed, after which the General with most HP is decided as winner. If both have same HP both lose.

    Battle happens every one minute against random User in database, and upon winning user gets 1-2 random cards. As
        they increase in rank more rare cards are unlocked as possible rewards. Upon reaching rank 50 X card is
        given as a reward, then rank 20, rank 10, rank 5, and again at rank 1.

    For now lets keep rank set at amount of wins because anything else would be so dang difficult


    """
    BEATS = {'snipe': 'assault',
             'assault': 'shield',
             'shield': 'snipe'}

    def determine_first_player(self, ldeck, rdeck):
        lgen = ldeck.general
        rgen = rdeck.general
        superior_attribute = self.attribute_resolver(lgen.attribute, rgen.attribute)

        if superior_attribute is True:
            return True  # Left General wins
        elif superior_attribute is False:
            return False  # Right General wins
        else:
            if lgen.attribute > rgen.attribute:
                return True  # Left General wins
            elif lgen.attribute < rgen.attribute:
                return False  # Right General wins
            return True  # No winner, Left General wins by default

    def determine_unit_winner(self, lunit, runit):
        winner = self.attribute_resolver(lunit.attribute, runit.attribute)
        if winner is True:
            lunit.cost += 1
            return winner
        elif winner is False:
            runit.cost += 1
            return winner
        else:
            return winner

        # costs = {'lunit': lunit.cost, 'runit': runit.cost}
        # return max(costs, key=costs.get)

    def attribute_resolver(self, left_attribute, right_attribute):
        if left_attribute == self.BEATS[right_attribute]:
            return True  # Left wins
        elif left_attribute == self.BEATS[right_attribute]:
            return False  # Right wins
        else:
            return None  # Both lose

    def handle_deck_clash(self, ldeck, rdeck):
        for position in range(3):
            position = str(position)  # To pick the correct Unit in the deck's units dict
            survivor = self.determine_unit_winner(ldeck.units[position], rdeck.units[position])

            if survivor is True:  # Left Unit won clash
                ldeck.units[position].state = True
                rdeck.units[position].state = False

            elif survivor is False:  # Right Unit won clash
                ldeck.units[position].state = False
                rdeck.units[position].state = True

            else:  # Both Units lost clash
                ldeck.units[position].state = False
                rdeck.units[position].state = False

    @staticmethod
    def apply_ability(lunit, lgen, runit, rgen):
        from backend.abilities.abilities import perform_ability_effect

        if lunit.state:
            perform_ability_effect(lunit.ability, lgen, rgen)
        elif runit.state:
            perform_ability_effect(runit.ability, lgen, rgen)
        else:
            pass

    def apply_abilities(self, ldeck, rdeck):
        for position in range(3):
            position = str(position)  # To pick the correct Unit in the deck's units dict
            self.apply_ability(ldeck.units[position], ldeck.general, rdeck.units[position], rdeck.general)

    @staticmethod
    def general_clash(lgen, rgen, attacker):
        from backend.abilities.abilities import perform_ability_effect

        if attacker:
            for ability in lgen.abilities:
                perform_ability_effect(ability, lgen, rgen)
        else:
            for ability in rgen.abilities:
                perform_ability_effect(ability, lgen, rgen)
