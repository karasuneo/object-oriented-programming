#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PySide6 import QtGui, QtCore
from my_module.K21999.lecture05_sample import GameModel

class MainWidget(QWidget):
      def __init__(self, game_model : GameModel):
            super().__init__()
            self.game_model = game_model
            self.top_label = QLabel()
            self.top_label.setText("ゲームメッセージ")
            self.top_label.setFont(QtGui.QFont('Arial', 20))
            self.top_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.buttons = [QPushButton() for _ in range(9)]
            [btn.setFont(QtGui.QFont('Arial', 40)) for btn in self.buttons]
            layout1 = QGridLayout()
            layout1.addWidget(self.top_label,0,0)
            layout2 = QGridLayout()
            for i in range(3):
                  for j in range(3):
                        layout2.addWidget(self.buttons[i*3+j], i, j)
            layout3 = QGridLayout()
            self.update_btn = QPushButton()
            self.update_btn.setText("更新")
            self.update_btn.setFont(QtGui.QFont('Arial', 20))
            layout3.addWidget(self.update_btn, 0,0)
            layouts = QGridLayout()
            layouts.addLayout(layout1, 0,0)
            layouts.addLayout(layout2, 1,0)
            layouts.addLayout(layout3, 2,0)
            self.setLayout(layouts)

if __name__ == "__main__":
      game_model = GameModel()
      app = QApplication(sys.argv)
      mw = MainWidget(game_model)
      mw.show()
      mw2 = MainWidget(game_model)
      mw2.show()
      app.exec()