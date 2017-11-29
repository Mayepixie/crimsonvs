from backend.combat.combat_rules import CombatRules


class Combat(CombatRules):

    def start_game(self, left_user, right_user, left_deck, right_deck):
        turn_count = 0
        left_user_turns_skip = 0
        right_user_turns_skip = 0
        self.handle_deck_clash(left_deck, right_deck)
        starting_player = self.determine_first_player(left_deck, right_deck)

        winner = self.perform_combat(left_deck, right_deck, turn_count, starting_player)
        if winner:
            return left_user
        else:
            return right_user

    def perform_combat(self, left_deck, right_deck, turn_count, starting_player):
        attacker = starting_player
        while left_deck.general.hp > 0 and right_deck.general.hp > 0 and turn_count > 10:
            if attacker:
                self.perform_turn(left_deck, right_deck, attacker)
                attacker = False
            else:
                self.perform_turn(left_deck, right_deck, attacker)
                attacker = True
            turn_count += 1

        if left_deck.general.hp > right_deck.general.hp:
            return True  # Left User wins
        else:
            return False  # Right User wins

    def perform_turn(self, ldeck, rdeck, attacker):
        self.apply_abilities(ldeck, rdeck)
        self.general_clash(ldeck.general, rdeck.general, attacker)

