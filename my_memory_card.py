from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QHBoxLayout, QGroupBox



app = QApplication([])



btn_OK = QPushButton("Answer")

lb_Question = QLabel('Question Here?')

RadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton("Answer 1")
rbtn_2 = QRadioButton("Answer 2")
rbtn_3 = QRadioButton("Answer 3")
rbtn_4 = QRadioButton("Answer 4")


h_layout_1 = QVBoxLayout()

v_layout_1 = QHBoxLayout()
v_layout_2 = QHBoxLayout()


v_layout_1.addWidget(rbtn_1)
v_layout_1.addWidget(rbtn_2)

v_layout_2.addWidget(rbtn_3)
v_layout_2.addWidget(rbtn_4)

h_layout_1.addLayout(v_layout_1)
h_layout_1.addLayout(v_layout_2)

RadioGroupBox.setLayout(h_layout_1)



AnsGroupBox = QGroupBox("Test Result!")
lb_result = QLabel("Are you correct or not?")
lb_correct = QLabel("The result is here")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignCenter))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

main_h_line1 = QHBoxLayout()
main_h_line2 = QHBoxLayout()
main_h_line3 = QHBoxLayout()

main_h_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
main_h_line2.addWidget(RadioGroupBox)
main_h_line2.addWidget(AnsGroupBox)
# RadioGroupBox.hide()

main_h_line3.addStretch(1)
main_h_line3.addWidget(btn_OK, stretch=2)
main_h_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(main_h_line1, stretch= 2)
layout_card.addLayout(main_h_line2, stretch= 8)
layout_card.addStretch(1)
layout_card.addLayout(main_h_line3, stretch= 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle("Memory Card")
window.show()
app.exec_()