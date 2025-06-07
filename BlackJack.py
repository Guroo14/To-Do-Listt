import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Blackjack(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blackjack")
        self.design()
        self.reset()

    def design(self):
        self.setFixedSize(300, 100)

        self.info = QLabel("Welcome to Blackjack!")
        self.player = QLabel("Player :")
        self.dealer = QLabel("Dealer :")

        self.hit_button = QPushButton("Hit")
        self.stand_button = QPushButton("Stand")
        self.reset_game_button = QPushButton("Reset")

        self.hit_button.clicked.connect(self.hit)
        self.stand_button.clicked.connect(self.stand)
        self.reset_game_button.clicked.connect(self.reset)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.info)
        vertical_layout.addWidget(self.player)
        vertical_layout.addWidget(self.dealer)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.hit_button)
        horizontal_layout.addWidget(self.stand_button)
        horizontal_layout.addWidget(self.reset_game_button)

        vertical_layout.addLayout(horizontal_layout)

        self.setLayout(vertical_layout)

    def reset(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.cards)

        self.player_cards = [self.draw_card(), self.draw_card()]
        self.dealer_cards = [self.draw_card(), self.draw_card()]

        self.hit_button.setEnabled(True)
        self.stand_button.setEnabled(True)
        self.reset_game_button.setEnabled(False)

        self.update_design()

    def draw_card(self):
        return self.cards.pop()

    def value(self, hand):
        card_count = sum(hand)
        aces = hand.count(11)
        while card_count > 21 and aces:
            card_count -= 10
            aces -= 1
        return card_count

    def update_design(self):
        self.player.setText(f"Player: {self.player_cards} ({self.value(self.player_cards)})")
        self.dealer.setText(f"Dealer: {self.dealer_cards[0]}, ?")
        self.info.setText("Hit or Stand?")

    def hit(self):
        self.player_cards.append(self.draw_card())
        if self.value(self.player_cards) > 21:
            self.end_game("Unlucky! Dealer Won.")
        else:
            self.update_design()

    def stand(self):
        while self.value(self.dealer_cards) < 17:
            self.dealer_cards.append(self.draw_card())

        player_sum = self.value(self.player_cards)
        dealer_sum = self.value(self.dealer_cards)
        if player_sum > dealer_sum or dealer_sum > 21:
            self.end_game("Congratulations, You Win.")
        elif player_sum < dealer_sum:
            self.end_game("Unlucky, You Lose.")
        else:
            self.end_game("Push! It's a draw.")

    def end_game(self, message):
        self.player.setText(f"Player: {self.player_cards} ({self.value(self.player_cards)})")
        self.dealer.setText(f"Dealer: {self.dealer_cards} ({self.value(self.dealer_cards)})")
        self.info.setText(message)

        self.hit_button.setEnabled(False)
        self.stand_button.setEnabled(False)
        self.reset_game_button.setEnabled(True)


app = QApplication(sys.argv)
game = Blackjack()
game.show()
sys.exit(app.exec_())