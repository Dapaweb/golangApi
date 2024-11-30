import sys
from PyQt5 import QtWidgets, uic 
import conndb

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Mahasiswa.ui", self)
        self.setWindowTitle("MAHASISWA")
        self.pushButton.clicked.connect(self.loadData)
        self.pushButtonSimpan.clicked.connect(self.createData)
        self.pushButtonUpdate.clicked.connect(self.updateData)
        self.pushButtonDelete.clicked.connect(self.deleteData)
        self.tableWidget.clicked.connect(self.getData)
        self.tableWidget.setColumnWidth(0, 220)
        self.tableWidget.setColumnWidth(3, 220)
        pass
    
    def getData(self):
        row = self.tableWidget.currentRow()
        print(str(row))
        rowItemNama = self.tableWidget.item(row, 0).text()
        rowItemNpm = self.tableWidget.item(row, 1).text()
        rowItemKelas = self.tableWidget.item(row, 2).text()
        rowItemMatprak = self.tableWidget.item(row, 3).text()

        self.lineEditNama.setText(rowItemNama)
        self.lineEditNpm.setText(rowItemNpm)
        self.lineEditKelas.setText(rowItemKelas)
        self.lineEditMatprak.setText(rowItemMatprak)

    def createData(self):
        nama = self.lineEditNama.text()
        npm = self.lineEditNpm.text()
        kelas = self.lineEditKelas.text()
        mata_prak = self.lineEditMatprak.text()
        strsql = "INSERT INTO tbl_mahasiswa VALUES ('"+nama+"', '"+npm+"', '"+kelas+"', '"+mata_prak+"')"
        conn = conndb.conndb()
        conn.queryExecute(strsql)
        self.lineEditNama.clear()
        self.lineEditNpm.clear()
        self.lineEditKelas.clear()
        self.lineEditMatprak.clear()
        self.loadData()

    def updateData(self):
        nama = self.lineEditNama.text()
        npm = self.lineEditNpm.text()
        kelas = self.lineEditKelas.text()
        mata_prak = self.lineEditMatprak.text()
        strsql = "UPDATE tbl_mahasiswa SET nama ='"+nama+"', kelas='"+kelas+"', mata_prak='"+mata_prak+"' WHERE npm='"+npm+"'"
        conn = conndb.conndb()
        conn.queryExecute(strsql)
        self.lineEditNama.clear()
        self.lineEditNpm.clear()
        self.lineEditKelas.clear()
        self.lineEditMatprak.clear()
        self.loadData()

    def loadData(self):
        conn = conndb.conndb()
        strsql = "SELECT * FROM tbl_mahasiswa"
        result = conn.queryResult(strsql)
        print(result)
        row=0
        self.tableWidget.setRowCount(len(result))
        for user in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(user[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(user[3]))
            row = row+1

    def deleteData(self):
        npm = self.lineEditNpm.text()
        strsql = "DELETE FROM tbl_mahasiswa WHERE npm ='"+npm+"'"
        conn = conndb.conndb()
        conn.queryExecute(strsql)
        self.loadData()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()