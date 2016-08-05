import numpy as np
import glob
import sys
import os

#import matplotlib.pyplot as plt

FolderName = sys.argv[1]
os.chdir(FolderName)

CurrentFiles = glob.glob('*.csv*')
print "\n//////////////////////////\nSelect File to work on:\n\n"
for kat in range(len(CurrentFiles)):
    print  str(kat) + " : " + CurrentFiles[kat]

DataName = raw_input("Enter File to process (i.e. 4 or x to process all files):  ")
if (DataName == 'x' or DataName == 'X'):
    kat0 = 0
    katN = len(CurrentFiles)
else:
    kat0 = int(DataName)
    katN = int(DataName)+1
    ##FileName = CurrentFiles[int(DataName)]


Hist = raw_input("do you wish to bin the data in a histogram before doing the FFT? (Y/N): ")
if (Hist == 'Y' or  Hist == 'y'):
    BinSize = raw_input("Enter histogram bin size:  ")
    BinSize = float(BinSize)

##BinSize = int(BinSize)

for kat in range(kat0,katN):
    FileName = CurrentFiles[int(kat)]
    my_data = np.loadtxt(FileName, delimiter=',', skiprows = 1, usecols = (0,1))
    Bins=np.arange(my_data[:,0].min(),my_data[:,0].max()+BinSize,BinSize)
    if (Hist == 'Y' or  Hist == 'y'):
        Counts, Bins = np.histogram(my_data[:,0],Bins)
        ##plt.ion()
        ##plt.hist(my_data[:,0],100)
        FFT = abs(np.fft.fft(Counts-np.mean(Counts)))
        Freq= 1/np.fft.fftfreq(Counts.shape[-1],Bins[1])
        SaveFile = FileName+'FFT.dat'
        f = open(SaveFile,'w')
        f.write(" %s , %s  \n" % (" Period [nm]", "abs(FFT) "))
        for item in np.arange(len(FFT)):f.write(" %s , %s \n" % (str(Freq[item]),str(FFT[item])))
        f.close()
    else:
        FFT = abs(np.fft.fft(my_data[:,1]-np.mean(my_data[:,1])))
        katkat
        Freq= 1/np.fft.fftfreq(my_data[:,1].shape[-1],my_data[1,0])
        SaveFile = FileName+'FFT.dat'
        f = open(SaveFile,'w')
        f.write(" %s , %s  \n" % (" Period [nm]", "abs(FFT) "))
        for item in np.arange(len(FFT)):f.write(" %s , %s \n" % (str(Freq[item]),str(FFT[item])))
        f.close()
    
