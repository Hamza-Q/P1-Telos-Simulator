import logging
import pprint

# Do you ever need to know this
TICK_INTERVAL = 0.6

FREEDOM_CD_1000 = 10//0.6
FREEDOM_CD_250 = 20//0.6
FREEDOM_CD_150 = 30//0.6

# telos can be stunned and bound and stuff same as the player so should probably
# inherit from some kind of parent Stunnable class but oh well
class Telos:
    def __init__(self, logger, enrage=0):
        self.enrage = enrage
        # Need a receiver for actions to know when this guy freedoms and attacks and stuff
        # Probably want it to be some kind of testable object; use a logger for now
        self.logger = logger

        # State objects to know what Telos is going to do #
        #
        # Cooldowns
        self.attack_cd_ticks = 4
        self.freedom_cd_ticks = self.freedom_cooldown(enrage)
        #
        # Status Effects
        self.is_bound = False
        self.is_stunned = False

    @staticmethod
    def freedom_cooldown(enrage):
        if enrage >= 1000:
            return FREEDOM_CD_1000
        if enrage >= 250:
            return FREEDOM_CD_250
        if enrage >= 150:
            return FREEDOM_CD_150
        return -1

    def should_freedom(self):
        return self.is_bound or self.is_stunned

    def can_freedom(self):
        return (self.freedom_cooldown() is not None) and (self.freedom_cd_ticks <= 0)

    def update(self):
        if self.can_freedom() and self.should_freedom():
            self.freedom_cd_ticks = self.freedom_cooldown()
        

