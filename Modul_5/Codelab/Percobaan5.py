from matplotlib import pyplot as plt

#Mengimpor fungsi normal dari pustaka numpy.random
#Digunakan untuk menghasilkan sampel data dari distribusi normal
from numpy.random import normal

#Mengimpor fungsi mean dan std dari pustaka numpy
#Digunakan untuk menhitung rata-rata dan standar deviasi data
from numpy import mean,std

#Mengimpor distribusi normal dari pustaka scipy stats
#Digunakan untuk analisis statistik terkait distribusi normal
from scipy.stats import norm

sample = normal (size=1000)
plt.hist(sample,bins=10)
plt.show()

dist = norm(sample_mean, sample_std)
dist 
values = [value for value in range (30,70)]

probabilitas = [dist.pdf(value) for value in values]
probabilitas

plt.hist(sample, bins=10, density=True)
plt.plot(values,probabilitas)
plt.show()