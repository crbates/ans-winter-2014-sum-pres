from pylab import *
plt.title("Test", fontname="Times New Roman Bold")
import matplotlib.pyplot as plt

# time in hours
t=[1.22, 1.752, 2.008, 3.22, 4.80, 6.80, 9.47, 12.7, 15.9, 20.2, 25.2, 36.7, 59, 96, 133, 197, 292, 464, 475]

expdatac2 = [488., 415., 375., 268., 173., 101., 50.6, 23.0, 11.7 ,5.80, 3.56, 2.43, 1.78, 1.22, 0.952, 0.759, 0.667,  0.613, 0.614]
exp_unc = [19., 16., 15., 10., 7., 4., 2.0, 0.9, 0.5, 0.23, 0.14, 0.09, 0.07, 0.05, 0.037, 0.030, 0.026, 0.024, 0.024]
exp_rel_err = [x/y for x, y in zip(exp_unc, expdatac2)]
top_err_bar = [1+x for x in exp_rel_err]
bot_err_bar = [1-x for x in exp_rel_err]

r2sdatac2 = [409.6, 357.8, 325.0,  240.7, 158.8, 94.25, 47.42, 21.39, 10.71, 5.151, 3.134, 2.214, 1.724, 1.264, 1.016, 0.8208, 0.7115, 0.6375, 0.6318]
d1sdatac2 = [390.0,     341.0,    310.0,   229.0,   150.0,  88.9,  44.6,  19.9,  9.73,  4.54,  2.66,  1.86,   1.5,  1.16, 0.974,  0.818,  0.725,  0.655, 0.651]

pyne_str_unnorm = [
3.3925E-11,
3.3734E-11,
3.3814E-11,
3.3260E-11,
3.2380E-11,
3.0820E-11,
2.8236E-11,
2.3315E-11,
1.8306E-11,
1.3042E-11,
1.0287E-11,
9.2131E-12,
8.9996E-12,
8.4805E-12,
8.0850E-12,
7.9153E-12,
8.1102E-12,
8.2767E-12,
8.3486E-12
]

pyne_unstr_unnorm = [ 
3.6142E-11,
3.5940E-11,
3.5742E-11,
3.5265E-11,
3.4709E-11,
3.2948E-11,
3.0006E-11,
2.4974E-11,
1.9477E-11,
1.4030E-11,
1.1014E-11,
9.9155E-12,
9.6386E-12,
9.1964E-12,
8.8134E-12,
8.6296E-12,
8.5837E-12,
8.9214E-12,
8.9279E-12,
]

pyne_uni_unnorm = [
3.4290E-11,
3.4157E-11,
3.4040E-11,
3.3593E-11,
3.2758E-11,
3.1282E-11,
2.8431E-11,
2.3672E-11,
1.8571E-11,
1.3338E-11,
1.0430E-11,
9.3030E-12,
9.1089E-12,
8.5706E-12,
8.2195E-12,
8.0326E-12,
8.1274E-12,
8.3914E-12,
8.4058E-12]

str_norms = [
1.165672E+09,
1.023899E+09,
9.327389E+08,
6.992203E+08,
4.723243E+08,
2.935185E+08,
1.635804E+08,
8.961018E+07,
5.762522E+07,
 3.975389E+07,
 3.161722E+07,
 2.515280E+07,
 1.994249E+07,
 1.564019E+07,
 1.324200E+07,
 1.102772E+07,
 9.510200E+06,
 8.270402E+06,
 8.213313E+06]

unstr_norms= [
1.153044E+09,
1.012886E+09,
9.227689E+08,
6.919205E+08,
4.676071E+08,
2.908163E+08,
1.623132E+08,
8.912482E+07,
5.745627E+07,
 3.971895E+07,
 3.161804E+07,
 2.515815E+07,
 1.993511E+07,
 1.563258E+07,
 1.323569E+07,
 1.102264E+07,
 9.506100E+06,
 8.267623E+06,
 8.210615E+06]

pyne_str_mrem=[]
for i in range(0, 19):
    pyne_str_mrem.append(pyne_str_unnorm[i]*str_norms[i])

pyne_uni_mrem=[]
for i in range(0, 19):
    pyne_uni_mrem.append(pyne_uni_unnorm[i]*str_norms[i])

pyne_unstr_mrem=[]
for i in range(0, 19):
    pyne_unstr_mrem.append(pyne_unstr_unnorm[i]*unstr_norms[i])

# convert to uSv/hr
pyne_str = [x*10000 for x in pyne_str_mrem]
pyne_uni = [x*10000 for x in pyne_uni_mrem]
pyne_unstr = [x*10000 for x in pyne_unstr_mrem]



# calculate ce
ce_r2sdatac2 = []
ce_d1sdatac2 = []
ce_pyne_str = []
ce_pyne_uni = []
ce_pyne_unstr = []

for i in range(0, 19):
    ce_r2sdatac2.append(r2sdatac2[i]/expdatac2[i])
    ce_d1sdatac2.append(d1sdatac2[i]/expdatac2[i])
    ce_pyne_str.append(pyne_str[i]/expdatac2[i])
    ce_pyne_uni.append(pyne_uni[i]/expdatac2[i])
    ce_pyne_unstr.append(pyne_unstr[i]/expdatac2[i])


fig1=plt.figure()
ax1=fig1.add_subplot(111)
ax1.scatter(t, pyne_str, label='PyNE R2S Cartesian', s=20, color='purple', marker = '^')
ax1.scatter(t, pyne_uni, label='PyNE Cartesian uniform', s=20, color='blue')
ax1.scatter(t, pyne_unstr, label='PyNE tetrahedral', s=20, color='orange', marker = 'v')
ax1.scatter(t, r2sdatac2, label='Batistoni et. al. R2S', s=20, color='red', marker = 's')
ax1.scatter(t, d1sdatac2, label='Batistoni et. al. D1S', s=20, color='green', marker = 'd')
ax1.set_xscale('log')
ax1.set_yscale('log')

font = {'family':'serif','size':20}
matplotlib.rc('font', **font)
ax1.set_xlabel('Decay Time (h)', fontname="Times New Roman")
ax1.set_ylabel('Dose Rate ($\mu$Sv/h)', fontname="Times New Roman")
ticks_font = matplotlib.font_manager.FontProperties(family='Times New Roman', style='normal', size=18, weight='normal', stretch='normal')
for label in ax1.get_xticklabels():
    label.set_fontproperties(ticks_font)
for label in ax1.get_yticklabels():
    label.set_fontproperties(ticks_font)

# plt.axis(xmin=1, xmax=1E3, ymin=0.6, ymax=1.4, fontname="Times New Roman")
plt.axis(xmin=1, xmax=1E3, fontname="Times New Roman")
fig1.set_facecolor("white")
l=legend(scatterpoints = 1, prop={'size':14}, loc=1)
for a in l.get_texts():
    a.set_fontproperties(ticks_font)

plt.savefig("comp.pdf", bbox_inches='tight')
