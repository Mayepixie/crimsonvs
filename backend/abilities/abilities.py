class BaseAbility(object):
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def effect(self, caster, target):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value


def get_ability(ability_name):
    ability = getattr(module, ability_name)
    return ability()


def get_ability_description(ability_name):
    return get_ability(ability_name).description


def perform_ability_effect(ability_name, caster=None, target=None):
    ability = get_ability(ability_name)
    ability.effect(caster, target)


class AIDABerserk(BaseAbility):
    def __init__(self):
        self._name = "AIDA Berserk"
        self._description = "At the beginning of this turn, your General gets +2 AP and takes 2 damage."
        BaseAbility.__init__(self, self._name, self._description)

    def effect(self, caster, target=None):
        caster.ap + 2
        caster.hp - 2


class AIDACorrosion(BaseAbility):
    def __init__(self):
        self._name = "AIDA Corrosion"
        self._description = "At the beginning of your turn, your General gets +1 AP and takes one damage."
        BaseAbility.__init__(self, self._name, self._description)

    def effect(self, caster, target=None):
        caster.ap + 1
        caster.hp - 1


class AllAtOnce(BaseAbility):
    # All At Once
    # Adds 2 AP to your General for every Junctioned card you hold.
    pass


class AnusKarma(BaseAbility):
    # Anu's Karma
    # Recovers 3 HP at the end of your turn when your General goes second.
    pass


class AuroraTears(BaseAbility):
    # Aurora Tears
    # Recovers 3 HP at the end of your turn when your General goes second.
    pass


class AvatarBerserk(BaseAbility):
    # Avatar Berserk
    # Skip 3 turns of the enemy General, in exchange for receiving an additional 5 points of damage per turn.
    pass


class AvatarsDescent(BaseAbility):
    # Avatar's Descent
    # Your General gets AP +5 boost for 5 turns, reduce all damage from Enemy General's junctioned abilities to 0
    pass


class BladesCrossing(BaseAbility):
    # Blades Crossing
    # Whenever your General deals damage, deal an additional 1 damage.
    pass


class BoneCrunching(BaseAbility):
    # Bone Crunching
    # Your General gets +4 AP, -4 HP
    pass


class BorderOfZero(BaseAbility):
    # Border of Zero
    # Changes both Generals' HP to 1.
    pass


class ChangeRing(BaseAbility):
    # Change Ring
    # Switches enemy General's AP and HP
    pass


class ChargeAhead(BaseAbility):
    # Charge Ahead
    # Forces your General to take the first turn.  If both parties have junctioned this ability, it loses its effect.
    pass


class ClenchingTeeth(BaseAbility):
    # Clenching Teeth
    # Forcefully restores your General's HP to 1 when his HP becomes 0.  Can only be used once per battle.
    pass


class CrossCounter(BaseAbility):
    # Cross Counter
    # Whenever you receive damage from the Enemy General, deal 1 damage to the Enemy General.
    pass


class DefensiveStance(BaseAbility):
    # Defensive Stance
    # Force your General to go second.  Reduce damage your General would receive by 1.
    pass


class DemonicSpear(BaseAbility):
    # Demonic Spear
    # Deals 7 points of damage to enemy General.
    pass


class DemonSwordMaxwell(BaseAbility):
    # Demon Sword Maxwell
    # Nullifies all damage your General would receive from junctioned abilities.
    pass


class DetailOriented(BaseAbility):
    # Detail Oriented
    # Reduce up to 2 damage dealt to either General to 0.  All damage 3 and above is dealt normally.
    pass


class DifferentMix(BaseAbility):
    # Different Mix
    # Gives AP +2, HP +2, when junctioned with a different trinity, AP -2, HP -2 with the same trinity.
    pass


class DivinePunishment(BaseAbility):
    # Divine Punishment
    # Deals 5 points of damage to enemy General.
    pass


class DoubleTrigger(BaseAbility):
    # Double Trigger
    # When your General deals damage, add an additional 2 damage.
    pass


class EmperorsPride(BaseAbility):
    # Emperor's Pride
    # Reduce normal damage dealt to your General by 1.
    pass


class EnergyDrain(BaseAbility):
    # Energy Drain
    # Subtract 3 HP from the enemy General and add 3 HP to your General.
    pass


class EnergyGenome(BaseAbility):
    # Energy Genome
    # Recovers 1 HP for your General each time it becomes your turn.
    pass


class EstrangedSelf(BaseAbility):
    # Estranged Self
    # Removes all Junction Abilities from enemy General.
    # Receives additional 2 points of damage when your General is damaged.
    pass


class FillingHollow(BaseAbility):
    # Filling Hollow
    # Randomly removes a Junction Ability from both Generals each time it becomes your turn.
    pass


class FireFang(BaseAbility):
    # Fire Fang
    # Adds 1 AP to your General.
    pass


class FirstStrike(BaseAbility):
    # First Strike
    # Deals 1 point of damage to both Generals at the beginning of each players' turns.
    pass


class FirstToAction(BaseAbility):
    # First to Action
    # Deals 5 damage to the Enemy General.  Receive 1 damage to your General at the beginning of each subsequent turn.
    pass


class FlameFang(BaseAbility):
    # Flame Fang
    # Adds 2 AP to your General
    pass


class FolsetsTrial(BaseAbility):
    # Folset's Trial
    # Adds 1 AP to your General and reduces 1 HP at the beginning of each of your turns.
    pass


class FusedConsciousness(BaseAbility):
    # Fused Consciousness
    # Change your General's AP and HP value to the average values of both Generals' AP and HP.
    pass


class GabisCall(BaseAbility):
    # Gabi's Call
    # Nullifies abilities of snipe and assault type units junctioned by the Enemy General.
    pass


class GatheringOfTheStrong(BaseAbility):
    # Gathering of the Strong
    # For 5 turns, this deals 1 damage to the Enemy General every turn.
    pass


class GoldenSpear(BaseAbility):
    # Golden Spear
    # Deal 4 damage to the Enemy General.
    pass


class GriefOfComrade(BaseAbility):
    # Grief of Comrade
    # Adds 2 HP to your General for every Junctioned card held by enemy General.
    pass


class HammerOfUndoing(BaseAbility):
    # Hammer of Undoing
    # Deals 5 points of damage to both Generals.
    pass


class HarmonicRhythm(BaseAbility):
    # Harmonic Rhythm
    # AP +2 at the beginning of your turn if your General goes first.
    # HP +4 at the beginning of your turn if your General goes second.
    pass


class ImmortalGenome(BaseAbility):
    # Immortal Genome
    # Recovers 2 HP for your General each time it becomes your turn.
    pass


class IngeniousScheme(BaseAbility):
    # Ingenious Scheme
    # Reflects all damage from your General to the Enemy General for 2 turns.
    pass


class KaedesGuard(BaseAbility):
    # Kaede's Guard
    # Nullifies abilities of snipe and shield type units junctioned by the Enemy General.
    pass


class LightOfAnnihilation(BaseAbility):
    # Light of Annihilation
    # Deals 3 damage to both generals every turn.
    pass


class LongAwaitedReturn(BaseAbility):
    # Long-awaited Return
    # At the beginning of your turn, your General gets AP +1, HP +2.
    pass


class MassacrePulse(BaseAbility):
    # Massacre Pulse
    # Whenever you attack the Enemy General, your General gets AP +1.
    pass


class MeetingOfSouls(BaseAbility):
    # Meeting of Souls
    # Switches all Junctioned cards for both Generals.
    pass


class MercilessLight(BaseAbility):
    # Merciless Light
    # Deals 2 points of damage to both Generals at the beginning of each players' turns.
    pass


class MindsEye(BaseAbility):
    # Mind's Eye
    # Evades an attack from enemy General for one turn only.
    pass


class MirrorOfRevenge(BaseAbility):
    # Mirror of Revenge
    # Reflects all damage your General receives onto enemy General for 3 turns.
    pass


class MobilizeTheTroops(BaseAbility):
    # Mobilize the Troops
    # After 5 turns, this heals your General every turn by 1.
    pass


class MomentaryGlory(BaseAbility):
    # Momentary Glory
    # Lowers enemy's and raises your AP by 3 for one turn,
    # then raises enemy's and lowers your AP by 1 for every turn after.
    pass


class PatternOfDemons(BaseAbility):
    # Pattern of Demons
    # Void one Junction Ability of the enemy General's Unit with the highest cost.
    pass


class PriceOfInsight(BaseAbility):
    # Price of Insight
    # Removes activated Junction Ability "Price of Insight" and adds another random Junction Ability.
    pass


class PromisedDiscretion(BaseAbility):
    # Promised Discretion
    # Limits the damage either General can receive to 3.
    pass


class Quickdance(BaseAbility):
    # Quickdance
    # Reduces your General's AP by 3 and also your General can attack even when enemy General attacks.
    pass


class QuickLightning(BaseAbility):
    # Quick Lightning
    # Deals 3 points of damage to enemy General.
    pass


class RecklessRewards(BaseAbility):
    # Reckless Rewards
    # Your General gets AP +2.  When your General receives damage, you receive an additional 1 damage.
    pass


class Rendezvous(BaseAbility):
    # Rendezvous
    # At the beginning of combat, your General gets HP +10.
    # At the beginning of the 8th turn, deal 10 damage to your General.
    pass


class ShieldProtection(BaseAbility):
    # Shield Protection
    # Removes 1 Junction Ability gained through a Junctioned Snipe Element Unit from an enemy General.
    pass


class ShootingSquad(BaseAbility):
    # Shooting Squad
    # Nullifies abilities of assault and shield type units junctioned by the Enemy General.
    pass


class SnipeThunder(BaseAbility):
    # Snipe Thunder
    # Removes 1 Junction Ability gained through a Junctioned Assault Element Unit from an enemy General.
    pass


class SpiritClothes(BaseAbility):
    # Spirit Clothes
    # Reduces damage your General takes by 1 point.
    pass


class SuckItUp(BaseAbility):
    # Suck it up
    # When your General's HP falls to 0, force its HP to 5.  You can only do this once.
    pass


class Teamwork(BaseAbility):
    # Teamwork
    # When your General is performing a Delta Combo, AP +2, HP +2.  All other times AP -2, HP -2.
    pass


class Telepathy(BaseAbility):
    # Telepathy
    # When your General is performing a Delta Combo, AP +5, HP +5.  All other times AP -5, HP -5.
    pass


class TimeTorrent(BaseAbility):
    # Time Torrent
    # Skips enemy Genral's turn for one round.
    pass


class TragicArrow(BaseAbility):
    # Tragic Arrow
    # Deals 2 points of damage to enemy General at the beginning of your turn.
    pass


class TrialByFire(BaseAbility):
    # Trial by Fire
    # Renders your General unable to attack for 4 turns, then raises its AP by 5 and HP by 6.
    pass


class TwilightsCall(BaseAbility):
    # Twilight's Call
    # Reactivates each of your General's Junction Abilities except for "Twilight's Call" after 5 turns.
    pass


class VeilOfAura(BaseAbility):
    # Veil of Aura
    # Reduces damage your General takes by 2 points.
    pass


class VengefulArrow(BaseAbility):
    # Vengeful Arrow
    # Deals 1 point of damage to enemy General at the beginning of your turn.
    pass


class VerbotenLibation(BaseAbility):
    # Verboten Libation
    # Adds 7 HP to your General.
    pass


class VitalityMedicine(BaseAbility):
    # Vitality Medicine
    # Adds 5 HP to your General.
    pass


class WarningHarmony(BaseAbility):
    # Warning Harmony
    # Randomly removes a single Junctioned Unit from enemy General when they have 2 or more Junctioned Abilities in use.
    pass


class WhirlwindAssault(BaseAbility):
    # Whirlwind Assault
    # Removes 1 Junction Ability gained through a Junctioned Shield Elementu Unit from an enemy General.
    pass


class WillOfSimilars(BaseAbility):
    # Will of Similars
    # Adds 3 AP and HP when your General is junctioned by the same trinity Unit,
    # and reduces 3 AP and HP when Junctioned by a different one.
    pass
