from PyQt5 import QtGui, QtCore

import sys
import ui_main
import numpy as np
import pyqtgraph
import SWHear
import glob
import os
from utils import new_jitters, new_update_dir

os.environ['KMP_DUPLICATE_LIB_OK']='True'

#sys.path.append('../../../Google Drive/sempervivum/')
from loaders import load_model_pararms
from WGANGP_app import WGANGP

SECTION = 'gan_v2'
RUN_ID = '256_v2_50z_'  # 004
BATCH_SIZE = 32
IMAGE_SIZE = 256
z_dims = 64
DATA_NAME = 'sempervivum'
RUN_FOLDER = '../../../Google Drive/sempervivum/run/{}/'.format(SECTION)
paths = [file for file in glob.glob('{}/{}*'.format(RUN_FOLDER,RUN_ID))]
path = '../../../Google Drive/sempervivum/run/gan_v2/256_v2_50z_012_sempervivum'
params_file = '../../../Google Drive/sempervivum/run/gan_v2/256_v2_50z_001_sempervivum/params.pkl'

gan = load_model_pararms(WGANGP, path, params_file)

class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.grFFT.plotItem.showGrid(True, True, 0.7)
        self.grPCM.plotItem.showGrid(True, True, 0.7)
        self.maxFFT=0
        self.maxPCM=0
        self.ear = SWHear.SWHear(rate=44100, updatesPerSecond=20)
        self.ear.stream_start()
        self.height = 256
        self.width = 256
        self.channel = 3
        self.bytesPerLine = 3 * self.width
        self.fnorm = 100000
        self.cutoff = 3
        self.decay = 0.9
        self.z = np.clip(np.random.normal(loc=0.0, scale=1, size=(1, z_dims))[0],-self.cutoff,self.cutoff)
        self.a = np.zeros(shape=((1, z_dims)))[0]
        self.d = np.sign(np.random.normal(loc=0.0, scale=1, size=(1, z_dims))[0])
        self.fft_old = [0]

    def get_img(self):
        arr = 255 * ((gan.generator.predict(np.reshape(self.z, (1, -1))) + 1.) / 2.).squeeze()
        img = np.require(arr, np.uint8, 'C')
        qImg = QtGui.QImage(img, self.width, self.height, self.bytesPerLine, QtGui.QImage.Format_RGB888)
        pixmap01 = QtGui.QPixmap.fromImage(qImg)
        return pixmap01

    def updatez(self):
        if len(self.fft_old) == 1:
            self.fft_old = self.ear.fft
        self.z *= self.decay
        self.fbin = self.ear.rate / 2 / self.ear.fftx.shape[0]
        self.step = int(max(z_dims * self.fbin, 1000*self.freqSpinBox.value())/self.fbin // z_dims)
        #self.a = [self.ear.fft[i * self.step]/self.fnorm for i in range(z_dims)]
        delta_fft = self.ear.fft - self.fft_old
        self.a = [abs(delta_fft[i * self.step] / self.fnorm) for i in range(z_dims)]
        self.z += self.a * self.d
        for i in range(z_dims):
            if self.z[i] > self.cutoff:
                self.d[i] = -1
            if self.z[i] < -self.cutoff:
                self.d[i] = 1
        self.fft_old = self.ear.fft

    def update(self):
        self.grFFT.plotItem.setRange(xRange=[0, 1000*max(0.4, self.freqSpinBox.value())])
        if not self.ear.data is None and not self.ear.fft is None:

            pcmMax=np.max(np.abs(self.ear.data))

            if pcmMax>self.maxPCM:
                self.maxPCM=pcmMax
                self.grPCM.plotItem.setRange(yRange=[-pcmMax,pcmMax])

            if np.max(self.ear.fft)>self.maxFFT:
                self.maxFFT=np.max(np.abs(self.ear.fft))
                #self.grFFT.plotItem.setRange(yRange=[0,self.maxFFT])
                self.grFFT.plotItem.setRange(yRange=[0,1])

            self.pbLevel.setValue(1000*pcmMax/self.maxPCM)
            pen=pyqtgraph.mkPen(color='b')
            self.grPCM.plot(self.ear.datax,self.ear.data,pen=pen,clear=True)
            pen=pyqtgraph.mkPen(color='r')
            self.grFFT.plot(self.ear.fftx,self.ear.fft/self.maxFFT,pen=pen,clear=True)

            self.updatez()
            self.label_3.setPixmap(self.get_img())

        self.exitButton.clicked.connect(self.close)

        QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")
