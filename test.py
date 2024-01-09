import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QSpinBox


class Test(QDialog):
    """
    Test dialog for displaying QSpinBoxes.
    """

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        for i in range(2):
            layout.addWidget(QSpinBox())


if __name__ == '__main__':
    import os

    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    app = QApplication(sys.argv)
    dialog = Test()
    sys.exit(dialog.exec())