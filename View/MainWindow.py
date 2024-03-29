import sys

# import View
from View.TorturaNew import *
from View.TorturaEnd import *
from View.TorturaContinue import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100, 100, 400, 284)
        self.setWindowTitle("Tortúra")
        self.setStyleSheet("background-color : lightpink")
        self.initUI()

    def initUI(self):
        self.newTortura = createPushButton(60, 60, 280, 40, "Új Tortúra", self.newtortura, self)
        self.continueTortura = createPushButton(60, 150, 280, 40, "Tortúra folytatása", self.contortura, self)
        logic.generateDirectories()

    def newtortura(self):

        self.mb = createMessageBox(200, 380, 100, 60, "Figyelmeztetés",
                                   "Új tortúra indításával a régi adatok törlődnek. Folytatja?",
                                   (QMessageBox.Yes | QMessageBox.No), self)
        returnValue = self.mb.exec()

        if returnValue == QMessageBox.No:
            self.mb.close()
        else:
            self.newtort = NewTortura()
            self.newtort.show()

    def contortura(self):
        if exists("Docs/input/input.txt"):
            ff = open("Docs/input/input.txt", "r")
            tortura = ff.readline().rstrip()
            ff.close()

            if logic.Infos.readTorturaDatas(tortura):
                logic.readGroupsFromFile()
                logic.readSolutionsFromFile()
                logic.readGroupDatasFromFile(tortura)
                logic.ReadAdditionalDatas()

                logic.refreshPoints()

                if logic.Infos.endOfTortura:
                    self.tortveg = TorturaEnd()
                    self.tortveg.show()

                else:
                    if logic.Infos.solutionFile == "":
                        self.utolagosfelt = TorturaContinue()
                        self.utolagosfelt.show()
                    else:
                        self.tortbe = TorturaSolution()
                        self.tortbe.show()
            else:
                self.mb = createMessageBox(200, 380, 100, 60, "Figyelmeztetés",
                                           "Nincs megnyitható régi tortúra, a fájlokat törölték!", QMessageBox.Ok, self)

        else:
            self.mb = createMessageBox(200, 380, 100, 60, "Figyelmeztetés",
                                       "Nincs megnyitható régi tortúra, az input fájlt törölték!", QMessageBox.Ok, self)


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
