import logging
import pprint

# Do you ever need to know this
TICK_INTERVAL = 0.6

FREEDOM_CD_1000 = 16
FREEDOM_CD_250 = 31
FREEDOM_CD_150 = 50
FREEDOM_CD_0 = -1

# telos can be stunned and bound and stuff same as the player so should probably
# inherit from some kind of parent Stunnable class but oh well
class Telos:
    def __init__(self, enrage, target=None):
        self.enrage = enrage
        # TODO: Actually use the target
        self.target = target

        # State objects to know what Telos is going to do #
        #
        # Cooldowns
        self.attack_cd_ticks = 4
        self.freedom_cd_ticks = 0 
        #
        # Status Effects
        self.bound_length_ticks = 0 
        self.stunned_length_ticks = 0

    @staticmethod
    def freedom_cooldown(enrage):
        if enrage >= 1000:
            return FREEDOM_CD_1000
        if enrage >= 250:
            return FREEDOM_CD_250
        if enrage >= 150:
            return FREEDOM_CD_150
        # 0 enrage can't use freedom
        return FREEDOM_CD_0

    def should_freedom(self):
        return self.bound_length_ticks or self.stunned_length_ticks

    def can_freedom(self):
        return (self.freedom_cooldown(self.enrage) > FREEDOM_CD_0) and (self.freedom_cd_ticks <= 0)

    def use_freedom(self):
        if not self.can_freedom():
            raise RuntimeError(
                f"Telos object at enrage '{self.enrage}' with freedom cooldown \
                '{self.freedom_cd_ticks}' ticks cannot use freedom"
                )
        self.freedom_cd_ticks = self.freedom_cooldown(self.enrage)

    def update(self):
        if self.can_freedom() and self.should_freedom():
            self.use_freedom()
        if self.can_attack():
            self.attack(target)
