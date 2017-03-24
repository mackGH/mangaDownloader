#! python3
from PyQt4 import QtCore, QtGui
import sys, os, requests, bs4, logging
import gui_design, gui_design_about

logging.basicConfig(filename = 'mangadownloader_logfile.txt', filemode = 'w', level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

class workerThread(QtCore.QThread):
	def __init__(self, mangaName, saveFolder=None, parent=None):
		QtCore.QThread.__init__(self, parent)
		self.url ='http://www.mangareader.net'
		self.mangaName = '-'.join(mangaName.lower().split(' '))
		self.targetFolder = saveFolder
		self.stopRequested = False
		self.chaptersList = []
		self.mangaInfo = {}

	def __del__(self):
		self.wait()

	def download_full_chapter(self, chapter_link):
		mangaFolder = os.path.join(self.targetFolder, chapter_link[1:])
		os.makedirs(mangaFolder, exist_ok = True)
		try:
			getPage = requests.get(self.url + chapter_link)
			getPage.raise_for_status()
			getImageSoup = bs4.BeautifulSoup(getPage.text, 'lxml')
			getNumPages = getImageSoup.find_all('option')

			for i in range(len(getNumPages)):
				if self.stopRequested == True:
					break
				else:
					try:
						downloadChapter = requests.get(self.url + getNumPages[i].get('value'))
						downloadChapter.raise_for_status()
						self.emit(QtCore.SIGNAL('update_gui_notification(QString)'), ('   :%s%s' % (self.url, getNumPages[i].get('value'))))
						getImage = bs4.BeautifulSoup(downloadChapter.text, 'lxml')
						getImgTag = getImage.select('#img')
						getImgSrc = getImgTag[0].get('src')

						downloadChapter = requests.get(getImgSrc)
						saveToFile = open(os.path.join(mangaFolder, 'Page {}.jpg'.format(i + 1)), 'wb')

						for chunks in downloadChapter.iter_content(100000):
							saveToFile.write(chunks)

						saveToFile.close()

					except Exception as downloadErr:
						self.emit(QtCore.SIGNAL('update_gui_notification(QString)'), ('WARNING DOWNLOAD ERROR: %s...' % str(downloadErr)))
						logging.critical(downloadErr)
		except Exception as connErr:
			self.emit(QtCore.SIGNAL('update_gui_notification(QString)'), ('WARNING CONNECTION ERROR: %s...' % str(connErr)))
			logging.critical(connErr)

	def get_chapters(self):
		try:
			mangaUrl = str(self.url + '/' + self.mangaName)
			getPage = requests.get(mangaUrl)
			getPage.raise_for_status()
			coverFolder = os.path.join(self.targetFolder, 'covers')
			os.makedirs(self.targetFolder, exist_ok = True)
			os.makedirs(coverFolder, exist_ok = True)
			mangaSoup = bs4.BeautifulSoup(getPage.text, 'lxml')

			mangaImg = mangaSoup.find(id = 'mangaimg')
			getPage = requests.get(mangaImg.contents[0].get('src'))
			imgName = mangaImg.contents[0].get('src').split('/')
			saveImg = open(os.path.join(coverFolder, imgName[-1]), 'wb')
			self.mangaInfo['defaultMangaFolder'] = self.targetFolder
			self.mangaInfo['mangaImg'] = os.path.join(coverFolder, imgName[-1])

			for chunks in getPage.iter_content(100000):
				saveImg.write(chunks)

			saveImg.close()
			tempList = []
			getInfo = mangaSoup.find_all('td', 'propertytitle')

			for tags in getInfo:
				tempList.append(tags.find_next('td').get_text())
			self.mangaInfo['Name'] = tempList[0]
			self.mangaInfo['Alternate Name'] = tempList[1]
			self.mangaInfo['Release Year'] = tempList[2]
			self.mangaInfo['Status'] = tempList[3]
			self.mangaInfo['Author'] = tempList[4]

			for tags in mangaSoup.find_all('div', 'chico_manga'):
				getLink = tags.find_next('a').get('href')
				if getLink in self.chaptersList:
					continue
				else:
					self.chaptersList.append(getLink)

			self.mangaInfo['maxChapters'] = len(self.chaptersList)
			tempList = self.chaptersList[0:6]
			del self.chaptersList[0:6]
			tempList.reverse()
			self.chaptersList = self.chaptersList + tempList
			self.chaptersList.reverse()
			self.emit(QtCore.SIGNAL('update_gui_notification(QString)'), ('Manga series found %s...' % mangaUrl))
			self.emit(QtCore.SIGNAL('update_gui_notification(QString)'), ('%s chapter(s) found...\n' % len(self.chaptersList)))
			self.emit(QtCore.SIGNAL('set_manga_info(PyQt_PyObject)'), self.mangaInfo)

		except Exception as connErr:
			self.emit(QtCore.SIGNAL('update_gui_notification(QString)'), ('%s...\n' % str(connErr)))
			logging.critical(connErr)

	def run(self):
		self.get_chapters()
		for i in range(len(self.chaptersList)):
			if self.stopRequested == True:
				break
			else:
				self.emit(QtCore.SIGNAL('update_gui(PyQt_PyObject, PyQt_PyObject)'), i, self.chaptersList[i])
				self.download_full_chapter(self.chaptersList[i])

class mangaReaderApp(QtGui.QMainWindow, gui_design.Ui_MainWindow):
	def __init__(self, parent=None):
		super(mangaReaderApp, self).__init__(parent)
		self.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('icon\\favicon.bmp'))
		self.setStyle(QtGui.QApplication.setStyle('plastique'))
		self.progressBar.hide()
		self.actionQuit_Ctrl_Q.setShortcut('Ctrl+Q')
		self.actionAbout.setShortcut('F12')
		self.textBrowser.setEnabled(False)
		self.comboSaveFolder.setEditable(False)
		self.toolButtonSaveFolder.setEnabled(True)
		self.pushButton_submit.setAutoDefault(True)
		self.pushButton_submit.setDefault(True)
		self.threadExists = False

		self.targetFolder = os.path.join(os.getcwd(), 'Mangadownloader')
		self.comboSaveFolder.addItem(self.targetFolder)
		self.aboutWindow = aboutPage()

		#Event Triggers
		self.actionQuit_Ctrl_Q.triggered.connect(self.close_app)
		self.actionAbout.triggered.connect(self.aboutWindow.show)
		self.lineEdit.returnPressed.connect(self.pushButton_submit.click)
		self.pushButton_submit.clicked.connect(self.get_manga)
		self.pushButton_cancel.clicked.connect(self.download_cancelled)
		path = self.toolButtonSaveFolder.clicked.connect(self.get_cwd)

	def close_app(self):
		msgBox = QtGui.QMessageBox()
		msgBox.setIcon(QtGui.QMessageBox.Question)
		msgBox.setText('Are you sure you wan\'t to Exit?')
		msgBox.setWindowTitle('Exit Application')
		msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.No)
		result = msgBox.exec_()
		if result == QtGui.QMessageBox.Ok:
			sys.exit()

	def download_cancelled(self):
		self.lineEdit.setReadOnly(False)
		self.lineEdit.clear()
		self.pushButton_submit.setEnabled(True)

		if self.threadExists == True and self.mangaThread.isRunning() == True:
			msgBox = QtGui.QMessageBox()
			msgBox.setIcon(QtGui.QMessageBox.Question)
			msgBox.setText('Are you sure you wan\'t to cancel the download?')
			msgBox.setWindowTitle('Cancel Download')
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.No)
			result = msgBox.exec_()

			if result == QtGui.QMessageBox.Ok:
				self.mangaThread.stopRequested = True
				self.downloadTerminated = True
				self.mangaThread.quit()
		else:
			self.close_app()

	def get_cwd(self):
		self.targetFolder = QtGui.QFileDialog.getExistingDirectory()
		self.comboSaveFolder.insertItem(0, self.targetFolder)
		self.comboSaveFolder.setEditText(self.comboSaveFolder.itemText(0))

	def get_manga(self):
		if self.lineEdit.text() == '':
			return
		else:
			self.progressBar.setValue(0)
			self.lineEdit.setReadOnly(True)
			self.pushButton_submit.setEnabled(False)
			self.downloadTerminated = False
			self.textBrowser.setEnabled(True)
			self.textBrowser.clear()
			self.mangaThread = workerThread(self.lineEdit.text(), self.comboSaveFolder.itemText(0))
			self.mangaThread.start()
			self.connect(self.mangaThread, QtCore.SIGNAL('started()'), self.thread_started)
			self.connect(self.mangaThread, QtCore.SIGNAL('set_manga_info(PyQt_PyObject)'), self.set_manga_info)
			self.connect(self.mangaThread, QtCore.SIGNAL('update_gui(PyQt_PyObject, PyQt_PyObject)'), self.update_gui)
			self.connect(self.mangaThread, QtCore.SIGNAL('update_gui_notification(QString)'), self.update_gui_notification)
			self.connect(self.mangaThread, QtCore.SIGNAL('finished()'), self.thread_finished)

	def set_manga_info(self, mangaInfo):
		self.mangaInfo = mangaInfo
		self.max_chapters = mangaInfo['maxChapters']
		self.progressBar.setMaximum(mangaInfo['maxChapters'])
		self.progressBar.show()

		self.imgSource = QtGui.QPixmap(mangaInfo['mangaImg'])
		self.imgSource = self.imgSource.scaledToWidth(self.mangaIMG.width() - 30, 1)
		self.mangaCover = QtGui.QGraphicsScene()
		self.mangaCover.addPixmap(self.imgSource)
		self.mangaIMG.setEnabled(True)
		self.mangaIMG.setScene(self.mangaCover)

		self.lEditName.setEnabled(True)
		self.lEditName.setReadOnly(True)
		self.lEditName.setText(mangaInfo['Name'])
		self.lEditAltName.setEnabled(True)
		self.lEditAltName.setReadOnly(True)
		self.lEditAltName.setText(mangaInfo['Alternate Name'])
		self.lEditReleaseYear.setEnabled(True)
		self.lEditReleaseYear.setReadOnly(True)
		self.lEditReleaseYear.setText(mangaInfo['Release Year'])
		self.lEditStatus.setEnabled(True)
		self.lEditStatus.setReadOnly(True)
		self.lEditStatus.setText(mangaInfo['Status'])
		self.lEditAuthor.setEnabled(True)
		self.lEditAuthor.setReadOnly(True)
		self.lEditAuthor.setText(mangaInfo['Author'])

	def thread_finished(self):
		self.lineEdit.setReadOnly(False)
		self.lineEdit.clear()
		self.pushButton_submit.setEnabled(True)
		self.threadExists = False

		if self.downloadTerminated == True:
			self.textBrowser.append('\n{}\n'.format('=' * 37))
			self.textBrowser.setTextColor(QtGui.QColor('red'))
			self.textBrowser.append('{:>30}Download Terminated by User!'.format(' '))
			self.textBrowser.setTextColor(QtGui.QColor('black'))
			self.textBrowser.append('\n{}\n'.format('=' * 37))
		else:
			self.textBrowser.append('\n{}\n'.format('=' * 37))
			self.textBrowser.append('{:>25} Chapters successfully downloaded!'.format(self.mangaInfo['maxChapters']))
			self.textBrowser.append('\n{}\n'.format('=' * 37))

	def thread_started(self):
		self.threadExists = True

	def update_gui(self, chapterNum, mangaChapter):
		self.progressBar.setValue(chapterNum + 1) 
		self.textBrowser.append('Downloading chapter %s...' % mangaChapter)

	def update_gui_notification(self, info):
		self.textBrowser.append(info)

class aboutPage(QtGui.QWidget, gui_design_about.Ui_aboutForm):
	def __init__(self, parent=None):
		super(aboutPage, self).__init__(parent)
		self.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('icon\\favicon.bmp'))

def main():
	logging.debug('Start\n')
	app = QtGui.QApplication(sys.argv)
	mainWindow = mangaReaderApp()
	mainWindow.show()
	sys.exit(app.exec_())
	logging.debug('\nEnd of Program')

if __name__ == '__main__':
	main()