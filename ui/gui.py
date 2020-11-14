from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys
import os
# personal modules
import rulebook
from players import *
import ttt


# MAIN WINDOW #######################################################################################
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # making main window
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(1120, 850)  # setting size
        MainWindow.setMaximumSize(QtCore.QSize(1120, 850))

        icon = QtGui.QIcon()  # setting icon
        icon.addPixmap(QtGui.QPixmap("ui/images/favicon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        # CENTRAL WIDGET
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # games box with buttons #
        self.games_box = QtWidgets.QGroupBox(self.centralwidget)
        # game box size
        self.games_box.setGeometry(QtCore.QRect(10, 10, 350, 325))
        self.games_box.setMinimumSize(QtCore.QSize(350, 0))
        self.games_box.setMaximumSize(QtCore.QSize(350, 325))
        # game box font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        self.games_box.setFont(font)
        # object name
        self.games_box.setObjectName("games_box")
        # game box layout
        self.gridLayout = QtWidgets.QGridLayout(self.games_box)
        self.gridLayout.setObjectName("gridLayout")
        # game buttons
        # blackjack
        self.blackjack_button = QtWidgets.QPushButton(self.games_box)
        self.blackjack_button.setObjectName("blackjack_button")
        self.gridLayout.addWidget(self.blackjack_button, 0, 0, 1, 1)
        # hangman
        self.hangman_button = QtWidgets.QPushButton(self.games_box)
        self.hangman_button.setObjectName("hangman_button")
        self.gridLayout.addWidget(self.hangman_button, 1, 0, 1, 1)
        # num guess
        self.num_guess_button = QtWidgets.QPushButton(self.games_box)
        self.num_guess_button.setObjectName("num_guess_button")
        self.gridLayout.addWidget(self.num_guess_button, 2, 0, 1, 1)
        # rps
        self.rps_button = QtWidgets.QPushButton(self.games_box)
        self.rps_button.setObjectName("rps_button")
        self.gridLayout.addWidget(self.rps_button, 3, 0, 1, 1)
        # ttt
        self.ttt_button = QtWidgets.QPushButton(self.games_box)
        self.ttt_button.setObjectName("ttt_button")
        self.gridLayout.addWidget(self.ttt_button, 4, 0, 1, 1)
        # war
        self.war_button = QtWidgets.QPushButton(self.games_box)
        self.war_button.setObjectName("war_button")
        self.gridLayout.addWidget(self.war_button, 5, 0, 1, 1)

        # making the buttons work
        # blackjack
        self.blackjack_button.clicked.connect(
            lambda: self.show_rules('Blackjack'))
        self.blackjack_button.clicked.connect(
            lambda: self.start_game('Blackjack'))

        # hangman
        self.hangman_button.clicked.connect(lambda: self.show_rules('Hangman'))
        self.hangman_button.clicked.connect(lambda: self.start_game('Hangman'))

        # number guessing
        self.num_guess_button.clicked.connect(
            lambda: self.show_rules('Number guessing'))
        self.num_guess_button.clicked.connect(
            lambda: self.start_game('Number guessing'))

        # rock paper scissors
        self.rps_button.clicked.connect(
            lambda: self.show_rules('Rock Paper Scissors'))
        self.rps_button.clicked.connect(
            lambda: self.start_game('Rock Paper Scissors'))

        # tic tac toe
        self.ttt_button.clicked.connect(lambda: self.show_rules('Tic Tac Toe'))
        self.ttt_button.clicked.connect(lambda: self.start_game('Tic Tac Toe'))

        # war
        self.war_button.clicked.connect(lambda: self.show_rules('War'))
        self.war_button.clicked.connect(lambda: self.start_game('War'))

        # game widget to run the actual game hopefully #
        self.games_widget = QtWidgets.QWidget(self.centralwidget)
        self.games_widget.setGeometry(QtCore.QRect(380, 10, 730, 775))
        self.games_widget.setObjectName("games_widget")

        # scroll area for the rules #
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        # size
        self.scrollArea.setGeometry(QtCore.QRect(10, 345, 350, 385))
        self.scrollArea.setWidgetResizable(True)
        # object name
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(
            QtCore.QRect(0, 0, 348, 383))
        self.scrollAreaWidgetContents_2.setObjectName(
            "scrollAreaWidgetContents_2")
        # layout
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        # the label
        self.rules_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        # font
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(12)
        self.rules_label.setFont(font)
        # allignment
        self.rules_label.setAlignment(QtCore.Qt.AlignCenter)
        # word wrap
        self.rules_label.setWordWrap(True)
        # object name
        self.rules_label.setObjectName("rules_label")

        self.verticalLayout.addWidget(self.rules_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        # exit widget #
        self.exit_widget = QtWidgets.QWidget(self.centralwidget)
        self.exit_widget.setGeometry(QtCore.QRect(10, 740, 350, 45))
        self.exit_widget.setObjectName("exit_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.exit_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # the button
        self.exitButton = QtWidgets.QPushButton(self.exit_widget)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        # on click
        self.exitButton.clicked.connect(self.exit_application)

        # CENTRAL WIDGET ENDPOINT
        MainWindow.setCentralWidget(self.centralwidget)

        # MENU BAR
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # STATUS BAR
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # calling retransalateUi
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """RetransalateUi."""

        _translate = QtCore.QCoreApplication.translate
        # main window text
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Games"))

        # games box text
        self.games_box.setTitle(_translate("MainWindow", "The Games"))

        # button texts
        self.blackjack_button.setText(_translate("MainWindow", "Blackjack"))
        self.hangman_button.setText(_translate("MainWindow", "Hangman"))
        self.num_guess_button.setText(
            _translate("MainWindow", "Number Guessing"))
        self.rps_button.setText(_translate(
            "MainWindow", "Rock Paper Scissors"))
        self.ttt_button.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.war_button.setText(_translate("MainWindow", "War"))

        # rules label text
        self.rules_label.setText(_translate(
            "MainWindow", "Click a game to see the rules!"))

        # exit button text
        self.exitButton.setText(_translate("MainWindow", "EXIT"))

    def show_rules(self, game):
        """Rules."""

        self.rules_label.setText(game + '\n\n' + rulebook.rule_book(game))
        self.rules_label.setAlignment(QtCore.Qt.AlignJustify)

    def start_game(self, game):
        """Start game."""

        game = game.lower()

        if game == 'blackjack':
            pass

        elif game == 'hangman':
            pass

        elif game == 'number guessing':
            pass

        elif game == 'rock paper scissors':
            players = QtWidgets.QWidget()
            ui = Ui_players()
            ui.setupUi(players)

            players.setParent(self.games_widget)
            players.show()

        elif game == 'tic tac toe':
            TicTacToe = QtWidgets.QWidget()
            ui = ttt.Ui_TicTacToe()
            ui.setupUi(TicTacToe)

            TicTacToe.setParent(self.games_widget)
            TicTacToe.show()
        
        elif game == 'war':
            pass

    def exit_application(self):
        """Exits."""

        sys.exit()


def main():
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
