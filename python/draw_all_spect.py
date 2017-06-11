import ibmseti
import matplotlib.pyplot as plt
import numpy as np

baseDir = '/Users/jimh/SETI/basic/'
index = open(baseDir + 'public_list_basic_v2_26may_2017.csv','r')

def draw_spectrogram(data):
    
    aca = ibmseti.compamp.SimCompamp(data.read())
    spec = aca.get_spectrogram()

    # Instead of using SimCompAmp.get_spectrogram method
    # perform your own signal processing here before you create the spectrogram
    #
    # SimCompAmp.get_spectrogram is relatively simple. Here's the code to reproduce it:
    #
    # header, raw_data = r.content.split('\n',1)
    # complex_data = np.frombuffer(raw_data, dtype='i1').astype(np.float32).view(np.complex64)
    # shape = (32, 6144)
    # spec = np.abs( np.fft.fftshift( np.fft.fft( complex_data.reshape(*shape) ), 1) )**2
    # 
    # But instead of the line above, can you maniputlate `complex_data` with signal processing
    # techniques in the time-domain (windowing?, de-chirp?), or manipulate the output of the 
    # np.fft.fft process in a way to improve the signal to noise (Welch periodogram, subtract noise model)? 
    # 
    # example: Apply Hanning Window
    # complex_data = complex_data.reshape(*shape)
    # complex_data = complex_data * np.hanning(complex_data.shape[1])
    # spec = np.abs( np.fft.fftshift( np.fft.fft( complex_data ), 1) )**2


    fig, ax = plt.subplots(figsize=(10, 5))   

    # do different color mappings affect Watson's classification accuracy?
    # ax.imshow(np.log(spec), aspect = 0.5*float(spec.shape[1]) / spec.shape[0], cmap='hot')
    # ax.imshow(np.log(spec), aspect = 0.5*float(spec.shape[1]) / spec.shape[0], cmap='gray')
    # ax.imshow(np.log(spec), aspect = 0.5*float(spec.shape[1]) / spec.shape[0], cmap='Greys')
    
    ax.imshow(np.log(spec), aspect = 0.5*float(spec.shape[1]) / spec.shape[0])
    
    return fig

while True:
    line = index.readline()
    if line == '': break
    df,ty = line.split(',')
    ty = ty.strip()
    phyle = open(baseDir+df+'.dat','r+b')
    spect = draw_spectrogram(phyle)
    out = baseDir+'spect/'+ty+'/'+df+'.png'
    spect.savefig(out)
    plt.close(spect)
    print out

exit(0)