import pyforms
from pyforms.controls import ControlButton
from pyforms.controls import ControlText
from pyforms.controls import ControlImage
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlEmptyWidget
import random


class starting(BaseWidget):

    def __init__(self):
        self.players = int(ControlText('how many players, not including AI dealer: '))
        self.enter = ControlButton('Press the enter button to begin.')
        self.enter.value = self.enteraction

    def enteraction(self):
        return self.players


class player(BaseWidget):

    def __init__(self):
        global worldhands
        self.disclaimer = ControlText('The developer got lazy and did not have this program display different suits of cards, but it shouldn\'t change any of the math.', readonly = True)
        for i in range(len(worldhands)):
            if worldhands[i] == 1:
                self.myhand = ControlImage('ace', readonly = True)
                self.myhand.value = 'aceofspades.png'
            elif worldhands[i] == 2:
                self.twohand = ControlImage('two', readonly = True)
                self.twohand.value = 'twocard.png'
            elif worldhands[i] == 3:
                self.threehand = ControlImage('three', readonly = True)
                self.threehand.value = 'threecard.png'
            elif worldhands[i] == 4:
                self.fourhands = ControlImage('four', readonly = True)
                self.fourhands.value = 'fourcard.png'
            elif worldhands[i] == 5:
                self.fivehands = ControlImage('five', readonly = True)
                self.fivehands.value = 'fivecard.png'
            elif worldhands[i] == 6:
                self.sixhand = ControlImage('six', readonly = True)
                self.sixhand.value = 'sixcard.jpg'
            elif worldhands[i] == 7:
                self.sevenhand = ControlImage('seven', readonly = True)
                self.sevenhand.value = 'sevencard.png'
            elif worldhands[i] == 8:
                self.eighthand = ControlImage('eight', readonly = True)
                self.eighthand.value = 'eightcard.jpg'
            elif worldhands[i] == 9:
                self.ninehand = ControlImage('nine', readonly = True)
                self.ninehand.value = 'ninecard.jpg'
            elif worldhands[i] == 10:
                self.tenhand = ControlImage('ten', readonly = True)
                self.tenhand.value = 'tencardjpg'
            elif worldhands[i] == 10.0001:
                self.jackhand = ControlImage('jack', readonly = True)
                self.tenhand.value = 'jackcard.jpg'
            elif worldhands[i] == 10.0002:
                self.queenhand = ControlImage('queen', readonly = True)
                self.queenhand.value = 'queencard.png'
            elif worldhands[i] == 10.0003:
                self.kinghand = ControlImage('king', readonly = True)
                self.kinghand.value = 'kingcard.png'


        self.turning = ControlButton('Press to end turn')
        self.turning.value = self.turningaction

    def turningaction(self):
        return None


class betweenturns(player, BaseWidget):

    def __init__(self):
        self.message = ControlButton('Pass the screen to the next player and press when done.')
        self.message.value = self.messageaction
        self.newpanel = ControlEmptyWidget()

    def messageaction(self):
        dow = player()
        dow.parent = self
        self.newpanel.value = dow
        return None


class dealer(BaseWidget):

    def __init__(self):
        #this is where we show the dealer's hand
        self.hitormiss = ControlButton('Press for the dealer to determine if it will hit or not')
        self.hitormiss.value = self.hitormissaction
        self.nocheat = ControlText('Dont be a cheater. Allow the AI the oppurtunity to hit.', readonly = True)
        self.dealerdone = ControlButton('Press to continue')
        self.dealerdone.value = self.dealerdoneaction

    def hitormissaction(self):
        #this is where we show the dealer's new hand if it chooses to hit\
        holder = None

    def dealerdoneaction(self):
        return None


class lose(BaseWidget):

    def __init__(self):
        self.unfun = ControlText('Your hand has bust, you have been removed from the game', readonly = True)
        self.cry = ControlButton('press to continue')
        self.cry.value = self.cryaction

    def cryaction(self):
        BaseWidget.self.close()


class blackjack(starting, lose, betweenturns, dealer, BaseWidget):

    def __init__(self):
        super(blackjack, self).__init__('blackjack')
        self.players = starting.enteraction(self)
        self.turn = 0
        h2 = d2 = c2 = s2 = 2
        h3 = d3 = c3 = s3 = 3
        h4 = d4 = c4 = s4 = 4
        h5 = d5 = c5 = s5 = 5
        h6 = d6 = c6 = s6 = 6
        h7 = d7 = c7 = s7 = 7
        h8 = d8 = c8 = s8 = 8
        h9 = d9 = c9 = s9 = 9
        h10 = d10 = c10 = s10 = 10
        hj = dj = cj = sj = 10.0001
        hq = dq = cq = sq = 10.0002
        hk = dk = ck = sk = 10.0003
        ha = da = ca = sa = 1
        self.placeholder = [h2, h3, h4, h5, h6, h7, h8, h9, h10, hj, hq, hk, ha, d2, d3, d4, d5, d6, d7, d8, d9, d10, dj, dq, dk, da, c2, c3, c4, c5, c6, c7, c8, c9, c10, cj, cq, ck, ca, s2, s3, s4, s5, s6, s7, s8, s9, s10, sj, sq, sk, sa]
        self.deck = self.placeholder
        self.hit = ControlButton('press button to hit')
        self.hit.value = self.hitaction
        self.nexturn = ControlButton('next turn')
        self.nexturn.value = self.nexturnaction
        self._panel = ControlEmptyWidget()
        self.secondpanel = ControlEmptyWidget()
        self.thirdpanel = ControlEmptyWidget()
        self.fourthpanel = ControlEmptyWidget()
        win = starting()
        win.parent = self
        self._panel.value = win

    def setting(self):
        self.handcount = [2]
        for i in range(self.players):
            self.handcount.append(2)
        self.hands = []
        for i in range(self.players + 1):
            self.attempt = random.randint(0, len(self.deck) - 1)
            self.hands.append(self.deck[self.attempt])
            self.deck.pop(self.attempt)
            self.attempt = random.randint(0, len(self.deck) - 1)
            self.hands.append(self.deck[self.attempt])
            self.deck.pop(self.attempt)

    def hitaction(self):
        self.attempt = random.randint(0, len(self.deck) - 1)
        self.hands.insert(self.handcount[self.turn], self.deck[self.attempt])
        self.handcount[self.turn] += 1
        self.fold = 0
        for i in range(self.handcount[self.turn]):
            self.add = sum(self.handcount) - sum(self.handcount, self.turn + 1)
            self.fold += self.hands[self.add + i]
        if int(self.fold) > 21:
            self.players -= 1
            for i in range(self.handcount[self.turn]):
                self.hands.pop(self.add)
            self.handcount.pop(self.turn)
            self.turn -= 1
            fail = lose()
            fail.parent = self
            self.fourthpanel.value = fail

    def nexturnaction(self):
        if self.turn < self.players:
            self.turn += 1
        else:
            self.turn = 0
        if self.turn != 0:
            window = betweenturns()
            window.parent = self
            self.secondpanel.value = window
        else:
            wind = dealer()
            wind.parent = self
            self.thirdpanel.value = wind
        global worldhands
        worldhands = []
        for i in range(self.handcount[self.turn]):
            worldhands.append(self.hands[sum(self.handcount) - sum(self.handcount, self.turn + 1)])


pyforms.start_app(blackjack)