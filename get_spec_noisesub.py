import ibmseti
import os
import zipfile
import numpy as np
import scipy.misc


mydatafolder = os.path.join( os.environ['PWD'], 'data' )
zz = zipfile.ZipFile(mydatafolder + '/' + 'basic4.zip')
basic4list = zz.namelist()

csv_data = zz.namelist()[1:]
        
def aca2spec(aca):
	complex_data = aca.complex_data().reshape(32, 6144)
	complex_data = complex_data * np.hanning(complex_data.shape[1])
	cpfft = np.fft.fftshift( np.fft.fft(complex_data), 1)
	spec = np.abs(cpfft)**2
	return spec.astype(np.float32)
data = []
N = 1
for i,v in enumerate(csv_data):
    d = zz.open(v).read()
    aca = ibmseti.compamp.SimCompamp(d)
    if aca.header()['signal_classification'] == 'noise':
        spec = aca2spec(aca)
        if len(data) == 0:
            data = spec
        else:
            data = data + spec
            N += 1
data = data/N
print "got noise", N

for fname in basic4list:
	aca = ibmseti.compamp.SimCompamp(zz.open(fname).read())

	idx = aca.header()['uuid']
	#spectrogram = aca.get_spectrogram().astype(np.float32)
	spec = aca2spec(aca)
	#np.save(mydatafolder+'/png/'+idx, spectrogram)
	spec = spec - data
	spec[spec < 0] = 0.00001
	scipy.misc.imsave(mydatafolder+'/png_hanning_noisesub/'+idx+'.png', spec)
	
