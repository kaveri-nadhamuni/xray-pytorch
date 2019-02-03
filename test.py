import train
import time

data = 'xray'
#dim_word = 1000
dim_word = 300
#dim_image =4096
dim_image = 512
#data = 'f8k'
saveto = 'vse/%s' %data
encoder = 'lstm'

if __name__ == "__main__":
    begin_time = time.time()
    train.trainer(data=data, dim_image=dim_image, lrate=0.001, margin=0.2, encoder=encoder, max_epochs=100000, batch_size=300,
                dim=300, dim_word=dim_word, maxlen_w=150, dispFreq=10, validFreq=100, early_stop=10, saveto=saveto)

    print('Using %.2f s' %(time.time()-begin_time))