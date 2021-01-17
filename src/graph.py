# graph for Execution time vs number of slots (y vs x)
# x -> y
# num_slots -> ET

# import matplotlib.pyplot as plt

# x = [27182, 54302, 81411, 108521, 122131]
# y = [6.0740, 6.1723, 6.2653, 6.2956, 6.3728]

# plt.plot(x,y)
# plt.yticks([5,6,7])
# plt.xlabel( num_slots')
# plt.ylabel('ET')
# plt.title('Graph for Execution time vs Number of slots')
# plt.show()
#-----------------------------------------------------------------------------------------------------------------

# graph for Number of patterns vs number of slots (y vs x)
# x -> y
# num_slots -> num_patterns

# import matplotlib.pyplot as plt

# x = [27182, 54302, 81411, 108521, 122131]
# y = [27180, 54302, 81410, 108519, 122131]

# plt.plot(x,y)
# plt.xlabel('num_slots')
# plt.ylabel('num_patterns')
# plt.title('Graph for Number of patterns vs Number of slots')
# plt.show()
#--------------------------------------------------------------------------------------------------------------

# graph for Total Revenue vs number of slots (y vs x)
# x -> y
# num_slots -> total_revenue


# import matplotlib.pyplot as plt

# x = [27182, 54302, 81411, 108521, 122131]
# y = [129887, 322622, 580888, 791285, 898228]

# plt.plot(x,y)
# plt.xlabel('num_slots')
# plt.ylabel('total_revenue')
# plt.title('Graph for Total Revenue vs Number of slots')
# plt.show()

#--------------------------------------------------------------------------------------------------------------

# graph for Execution time vs slot types (y vs x)
# slot_types -> ET

# import matplotlib.pyplot as plt

# x = [3,6,9,12,15,18]
# y = [6.3980, 6.3770, 6.3285, 6.3622, 6.3283, 6.3596]

# plt.plot(x,y)
# plt.yticks([5,6,7])
# plt.xlabel('slot_types')
# plt.ylabel('ET')
# plt.title('Graph for Execution time vs Slot Types')
# plt.show()

#--------------------------------------------------------------------------------------------------------------

# graph for Total Revenue vs zipf factor (y vs x)
# zipf factor -> total_revenue

# import matplotlib.pyplot as plt

# x = [0.124, 0.138, 0.230, 0.304, 0.469]
# y = [333904, 316462, 302654, 294853, 282086]

# plt.plot(x,y)
# plt.xlabel('zipf factor')
# plt.ylabel('total_revenue')
# plt.title('Graph for Total Revenue vs Zipf Factor')
# plt.show()

#--------------------------------------------------------------------------------------------------------------

# graph for ET vs zipf factor (y vs x)
# zipf factor -> ET

# import matplotlib.pyplot as plt

# x = [0.124, 0.138, 0.230, 0.304, 0.469]
# y = [6.1210, 6.1204, 6.1144, 6.1272, 6.1141]

# plt.plot(x,y)
# plt.yticks([5,6,7])
# plt.xlabel('zipf factor')
# plt.ylabel('ET')
# plt.title('Graph for ET vs Zipf Factor')
# plt.show()

#------------------------------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [524.350,647.144,783.766,899.116,1022.716,1159.811,1285.316]

# plt.plot(x1, y1, label = "Revenue Based") 

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [524.616,649.788,782.783,899.844,1023.344,1157.161,1285.316]
# plt.plot(x2, y2, label = "Diversity Based") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [754.377,817.000,964.727,1069.133,1250.722,1461.566,1551.388]

# plt.plot(x3, y3, label = "Diverse Revenue Based") 
# plt.yticks([500,800,1000,1200,1400,1600])


# plt.xlabel('Number of Slots')
# plt.ylabel('Total Revenue')
# plt.title('Diverse Total Revenue')
# plt.legend() 
# plt.show()

#----------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [6.013,6.027,6.0341,6.037,6.038,6.046,6.035]

# plt.plot(x1, y1, label = "Revenue Based")

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [6.020,6.024,6.029,6.034,6.039,6.046,6.053]
# plt.plot(x2, y2, label = "Diversity Based") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [6.015,6.018,6.030,6.034,6.040,6.046,6.052]

# plt.plot(x3, y3, label = "Diverse Revenue Based") 
# plt.yticks([5,6,7])


# plt.xlabel('Number of Slots')
# plt.ylabel('ET')
# plt.title('diverse revenue execution time')
# plt.legend() 
# plt.show()


#--------------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [292.633,359.199,424.966,496.799,576.133,647.866,728.166]

# plt.plot(x1, y1, label = "0 slot")

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [280.633,365.666,424.933,471.566,540.233,646.733,681.966]
# plt.plot(x2, y2, label = "1 slot") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [274.199,315.333,438.999,499.599,529.399,565.733,648.500]

# plt.plot(x3, y3, label = "2 slot") 
# plt.yticks([200,400,600,800])


# plt.xlabel('Number of Slots')
# plt.ylabel('slots wise revenue')
# plt.title('revenue based')
# plt.legend() 
# plt.show()

#------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [292.833,360.533,424.266,497.566,576.533, 646.366,728.166]

# plt.plot(x1, y1, label = "0 slot")

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [280.633,367.933,425.033,470.799,540.799,645.633,681.966]
# plt.plot(x2, y2, label = "1 slot") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [274.399,315.866,437.999,500.633,529.233,563.933,648.500]

# plt.plot(x3, y3, label = "2 slot") 
# plt.yticks([200,400,600,800])


# plt.xlabel('Number of Slots')
# plt.ylabel('slots wise revenue')
# plt.title('diversity based')
# plt.legend() 
# plt.show()

#------------------------------------------------------------------------------

# import matplotlib.pyplot as plt

# x1 = [4000,5000,6000,7000,8000,9000,10000]
# y1 = [443.599,488.733,529.833,650.999,781.100,993.966,1032.933]

# plt.plot(x1, y1, label = "0 slot")

# x2 = [4000,5000,6000,7000,8000,9000,10000]
# y2 = [409.666,429.666,573.499,512.933,635.733,618.266,706.933]
# plt.plot(x2, y2, label = "1 slot") 

# x3 = [4000,5000,6000,7000,8000,9000,10000]
# y3 = [317.833,340.299,444.433,485.000,455.266,475.399,494.966]

# plt.plot(x3, y3, label = "2 slot") 
# plt.yticks([300,600,900,1100])


# plt.xlabel('Number of Slots')
# plt.ylabel('slots wise revenue')
# plt.title('diverse revenue based')
# plt.legend() 
# plt.show()

#------------------------------------------------------------------------------------
# import matplotlib.pyplot as plt

# x1 = [1500,1600,1700,1800,1900,2000]
# y1 = [14411.11,14827.43,15518.28,17286.35,17004.69,18272.57]

# plt.plot(x1, y1, label = "Frequency Based") 

# x2 = [1500,1600,1700,1800,1900,2000]
# y2 = [4765.78,4984.58,5708.86,6181.04,6566.33,7073.84]
# plt.plot(x2, y2, label = "price(revenue) Based")

# x3 = [1500,1600,1700,1800,1900,2000]
# y3 = [17125.70,18928.82,19476.33,20418.97,22092.55,22481.40]
# plt.plot(x3, y3, label = "Net Revenue")

# x4 = [1500,1600,1700,1800,1900,2000]
# y4 = [2057.16,2164.92,2164.92,2550.95,2722.38,2837.16]

# plt.plot(x4, y4, label = "Diversity Based") 

# x5 = [1500,1600,1700,1800,1900,2000]
# y5 = [18800.94,19366.30,19366.30,21164.57,21981.86,22374.83]
# plt.plot(x5, y5, label = "Diverse Revenue Based")

# plt.xlabel('Number of Slots')
# plt.ylabel('Total Revenue')
# plt.legend() 
# plt.show()

# -------------------------------------------------------------------- hybrid approach with drank threshold ---------------
# itemset ratio 0.5
# drank threshold >2

# import matplotlib.pyplot as plt

# x1 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y1 = [1004.21, 2648.11, 3417.73, 4538.60, 6603.24, 7743.29, 9222.90, 9867.55, 10722.16, 11535.46, 12693.88]

# plt.plot(x1, y1, label = "Frequency Based") 

# x2 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y2 = [113.0, 348.0, 534.16, 762.66, 1202.82, 1523.90, 2058.66, 2414.12, 2943.81, 3278.70, 3740.85]
# plt.plot(x2, y2, label = "price(revenue) Based")

# x3 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y3 = [1457.65, 3542.83, 4335.81, 5847.90, 7970.10, 9418.92, 11115.50, 11986.80, 13028.39, 13938.02, 15437.04]
# plt.plot(x3, y3, label = "Net Revenue")

# x4 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y4 = [47.43, 168.36, 227.89, 344.98, 503.60, 670.71, 883.80, 1024.67, 1182.86, 1359.27, 1544.04]

# plt.plot(x4, y4, label = "Diversity Based") 

# x5 = [70, 170, 270, 370, 470, 570, 670, 770, 870, 970, 1070]
# y5 = [953.88, 2273.37, 2710.64, 3545.08, 4647.98, 5389.17, 6238.41,6659.36, 7149.85, 7598.45, 8323.03]
# plt.plot(x5, y5, label = "Diverse Revenue Based")

# plt.xlabel('Number of Slots')
# plt.ylabel('Total Revenue')
# plt.legend() 
# plt.show()

# ----------------------- drank threshold >=2 -------------
# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.72,
#  2.4699999999999998,
#  2.69,
#  18.099999999999998,
#  29.09,
#  34.33,
#  39.37]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [61.82999999999998,
#  70.86999999999998,
#  86.17999999999999,
#  121.0,
#  141.17000000000004,
#  154.70999999999998,
#  167.1]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue for alpha 1')
# plt.legend() 
# plt.show()

#----------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.72,
#  2.4699999999999998,
#  2.69,
#  18.099999999999998,
#  29.09,
#  34.33,
#  39.37]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [63.40999999999997,
#  68.95999999999997,
#  81.36999999999999,
#  117.27000000000001,
#  136.24000000000004,
#  154.42999999999998,
#  164.38]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue for alpha 2')
# plt.legend() 
# plt.show()

#---------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.72,
#  2.4699999999999998,
#  2.69,
#  18.099999999999998,
#  29.09,
#  34.33,
#  39.37]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [62.019999999999975,
#  65.31999999999996,
#  78.99999999999999,
#  112.12,
#  142.00000000000006,
#  157.32999999999998,
#  160.13999999999996]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue for alpha 5')
# plt.legend() 
# plt.show()

#------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.24731182795698933,
#  0.25373134328358216,
#  0.26923076923076916,
#  0.2981770833333333,
#  0.2861635220125787,
#  0.287878787878788,
#  0.2961904761904764]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666664,
#  0.6666666666666667,
#  0.6666666666666669,
#  0.666666666666667]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.3505747126436782,
#  0.36111111111111105,
#  0.37333333333333324,
#  0.3863636363636364,
#  0.3964285714285716,
#  0.4019607843137257,
#  0.40705128205128227]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Drank Mean for alpha 5')
# plt.legend() 
# plt.show()

#------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.72,
#  2.4699999999999998,
#  2.69,
#  18.099999999999998,
#  29.09,
#  34.33,
#  39.37]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [59.71999999999998,
#  66.19999999999995,
#  78.58999999999999,
#  115.87000000000002,
#  135.62000000000003,
#  149.97,
#  162.37999999999997]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue for alpha 7')
# plt.legend() 
# plt.show()

#--------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.72,
#  2.4699999999999998,
#  2.69,
#  18.099999999999998,
#  29.09,
#  34.33,
#  39.37]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [50.57999999999998,
#  55.44999999999998,
#  71.19999999999999,
#  108.72,
#  134.86,
#  140.57000000000002,
#  154.76999999999995]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue for alpha 15')
# plt.legend() 
# plt.show()

#---------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.24731182795698933,
#  0.25373134328358216,
#  0.26923076923076916,
#  0.2981770833333333,
#  0.2861635220125787,
#  0.287878787878788,
#  0.2961904761904764]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666664,
#  0.6666666666666667,
#  0.6666666666666669,
#  0.666666666666667]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.3107344632768362,
#  0.32291666666666663,
#  0.3419913419913419,
#  0.35217391304347834,
#  0.36442786069651756,
#  0.3782894736842108,
#  0.3802083333333336]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Drank Mean for alpha 2')
# plt.legend() 
# plt.show()

#-------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.24731182795698933,
#  0.25373134328358216,
#  0.26923076923076916,
#  0.2981770833333333,
#  0.2861635220125787,
#  0.287878787878788,
#  0.2961904761904764]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666664,
#  0.6666666666666667,
#  0.6666666666666669,
#  0.666666666666667]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.29310344827586216,
#  0.29292929292929293,
#  0.30864197530864185,
#  0.34039548022598876,
#  0.34166666666666673,
#  0.33881578947368446,
#  0.35240963855421714]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Drank Mean for alpha 1')
# plt.legend() 
# plt.show()

#----------------------------------


# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.24731182795698933,
#  0.25373134328358216,
#  0.26923076923076916,
#  0.2981770833333333,
#  0.2861635220125787,
#  0.287878787878788,
#  0.2961904761904764]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666664,
#  0.6666666666666667,
#  0.6666666666666669,
#  0.666666666666667]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.36477987421383656,
#  0.3722222222222222,
#  0.3822222222222221,
#  0.3997050147492625,
#  0.4141791044776121,
#  0.41328828828828845,
#  0.4161425576519918]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Drank Mean for alpha 7')
# plt.legend() 
# plt.show()

#-------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.24731182795698933,
#  0.25373134328358216,
#  0.26923076923076916,
#  0.2981770833333333,
#  0.2861635220125787,
#  0.287878787878788,
#  0.2961904761904764]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666666,
#  0.6666666666666664,
#  0.6666666666666667,
#  0.6666666666666669,
#  0.666666666666667]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.43478260869565216,
#  0.4339622641509434,
#  0.4154589371980675,
#  0.42056074766355134,
#  0.4368686868686871,
#  0.4388489208633095,
#  0.44260485651214154]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Drank Mean for alpha 15')
# plt.legend() 
# plt.show()

#-------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [161.239,161.239,161.239,161.239,161.239,161.239]
 

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [29.09,29.09,29.09,29.09,29.09,29.09]


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [136.240,136.240,136.240,136.240,136.240,136.240]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [136.240,148.820,147.76,144.37,161.23,161.23]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR + H combination", marker="D")

# plt.xlabel('R ratio' )
# plt.ylabel( 'TR for alpha 2')
# plt.legend() 
# plt.show()

#-----------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [0.286,0.286,0.286,0.286,0.286,0.286]
 

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [0.666,0.666,0.666,0.666,0.666,0.666]


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [0.364,0.364,0.364,0.364,0.364,0.364]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [0.364,0.329,0.329,0.309,0.286,0.286]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR + H combination", marker="D")

# plt.xlabel('R ratio' )
# plt.ylabel( 'Drank_mean for alpha 2')
# plt.legend() 
# plt.show()

#------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]
 

# x_ibd = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_ibd = [84.10899999999997,
#  92.97099999999998,
#  108.514,
#  166.43,
#  203.591,
#  213.57299999999998,
#  228.08999999999995]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [61.82999999999998,
#  70.86999999999998,
#  86.17999999999999,
#  121.0,
#  141.17000000000004,
#  154.70999999999998,
#  167.1]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_ibd, y_ibd, label = "IBD", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR + H combination", marker="D")

# plt.xlabel('Ts' )
# plt.ylabel( 'TR')
# plt.legend() 
# plt.show()

#------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.72,
#  2.4699999999999998,
#  2.69,
#  18.099999999999998,
#  29.09,
#  34.33,
#  39.37]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [61.82999999999998,
#  70.86999999999998,
#  86.17999999999999,
#  121.0,
#  141.17000000000004,
#  154.70999999999998,
#  167.1]

# x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_div = [9.310000000000002,
#  2.92,
#  11.490000000000002,
#  17.77,
#  28.569999999999997,
#  22.510000000000005,
#  53.149999999999984]




# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_div, y_div, label = "Diversification", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue')
# plt.legend() 
# plt.show()

#--------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.72,
#  2.4699999999999998,
#  2.69,
#  18.099999999999998,
#  29.09,
#  34.33,
#  39.37]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [61.82999999999998,
#  70.86999999999998,
#  86.17999999999999,
#  121.0,
#  141.17000000000004,
#  154.70999999999998,
#  167.1]

# x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_div = [7.78,
#  4.75,
#  6.29,
#  28.660000000000007,
#  25.860000000000003,
#  37.51,
#  32.8]




# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_div, y_div, label = "Diversification_HRD", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue')
# plt.legend() 
# plt.show()


#-------------new---------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [65.55999999999997,
#  71.70999999999998,
#  82.66,
#  130.13000000000002,
#  161.23999999999998,
#  167.16,
#  177.95999999999995]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.72,
#  2.4699999999999998,
#  2.69,
#  18.099999999999998,
#  29.09,
#  34.33,
#  39.37]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [61.82999999999998,
#  70.86999999999998,
#  86.17999999999999,
#  121.0,
#  141.17000000000004,
#  154.70999999999998,
#  167.1]

# x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_div = [11.5,
#  3.0199999999999996,
#  7.710000000000001,
#  21.62,
#  33.629999999999995,
#  31.009999999999998,
#  33.68000000000001]




# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_div, y_div, label = "Diversification_HRD", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue')
# plt.legend() 
# plt.show()

#---------------------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1,2,4,8,12,16,20,24]
# y_r = [161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998]

# x_d = [1,2,4,8,12,16,20,24]
# y_d = [29.09, 29.09, 29.09, 29.09, 29.09, 29.09, 29.09, 29.09]


# x_dr = [1,2,4,8,12,16,20,24]
# y_dr = [141.17000000000004,
#  136.24000000000004,
#  140.81000000000003,
#  135.36000000000004,
#  138.13000000000002,
#  133.73000000000002,
#  133.73000000000002,
#  133.26000000000002]

# # x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# # y_div = [11.5,
# #  3.0199999999999996,
# #  7.710000000000001,
# #  21.62,
# #  33.629999999999995,
# #  31.009999999999998,
# #  33.68000000000001]




# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_div, y_div, label = "Diversification_HRD", marker="D")

# plt.xlabel('alpha variation' )
# plt.ylabel( 'Total Revenue for 12000 slots')
# plt.legend() 
# plt.show()

#--------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1,2,4,8,12,16,20,24]
# y_r = [0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787]

# x_d = [1,2,4,8,12,16,20,24]
# y_d = [0.6666666666666667,
#  0.6666666666666667,
#  0.6666666666666667,
#  0.6666666666666667,
#  0.6666666666666667,
#  0.6666666666666667,
#  0.6666666666666667,
#  0.6666666666666667]


# x_dr = [1,2,4,8,12,16,20,24]
# y_dr = [0.34166666666666673,
#  0.36442786069651756,
#  0.38768115942029,
#  0.4197994987468673,
#  0.43159203980099525,
#  0.44020356234096714,
#  0.44020356234096714,
#  0.4435897435897438]

# # x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# # y_div = [11.5,
# #  3.0199999999999996,
# #  7.710000000000001,
# #  21.62,
# #  33.629999999999995,
# #  31.009999999999998,
# #  33.68000000000001]




# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_div, y_div, label = "Diversification_HRD", marker="D")

# plt.xlabel('alpha variation' )
# plt.ylabel( 'Drank-mean for 12000 slots')
# plt.legend() 
# plt.show()


#-----------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.1,0.2,0.4,0.6,0.8]
# y_r = [161.23999999999998,161.23999999999998,161.23999999999998,161.23999999999998,161.23999999999998]
 

# x_ibd = [0.1,0.2,0.4,0.6,0.8]
# y_ibd = [174.86399999999998,
#  188.488,
#  215.736,
#  242.98399999999998,
#  270.232]


# x_dr = [0.1,0.2,0.4,0.6,0.8]
# y_dr = [141.17000000000004,141.17000000000004,141.17000000000004,141.17000000000004,141.17000000000004]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_ibd, y_ibd, label = "IBD", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR + H combination", marker="D")

# plt.xlabel('beta variation' )
# plt.ylabel( 'diversity effected revenue')
# plt.legend() 
# plt.show()

#--------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.1,0.2,0.4,0.6,0.8]
# y_r = [0.2861635220125787,0.2861635220125787,0.2861635220125787,0.2861635220125787,0.2861635220125787]
 

# x_ibd = [0.1,0.2,0.4,0.6,0.8]
# y_ibd = [0.32260630808223045,0.35904909415188224,0.4319346662911857,0.5048202384304893,0.5777058105697928]


# x_dr = [0.1,0.2,0.4,0.6,0.8]
# y_dr = [0.6666666666666667,0.6666666666666667,0.6666666666666667,0.6666666666666667,0.6666666666666667]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_ibd, y_ibd, label = "IBD", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR + H combination", marker="D")

# plt.xlabel('beta variation' )
# plt.ylabel( 'diversity effected drank-mean')
# plt.legend() 
# plt.show()

#----------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.22606924643584522,
#  0.19583333333333333,
#  0.16032171581769436,
#  0.13612708846891264,
#  0.12135290838134176,
#  0.1080693707897377,
#  0.09105180533751962]
 

# x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_div = [0.2727272727272727,
#  0.20160213618157544,
#  0.17678452301534356,
#  0.155,
#  0.14225383418537452,
#  0.12968828138023003,
#  0.10654753967195627]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.412,
#  0.368,
#  0.3345,
#  0.25575,
#  0.2034586200811717,
#  0.16554777888873018,
#  0.14014878809695225]

# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.26229508196721313,
#  0.2073684210526316,
#  0.17707212055974167,
#  0.15120367865837164,
#  0.1283846012156935,
#  0.1138223051528635,
#  0.09617950272892663]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_div, y_div, label = "Diversification", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="D")


# plt.xlabel('Number of Slots(Lambda)' )
# plt.ylabel( 'SI for DO ')
# plt.legend() 
# plt.show()


#----------------------HRD-------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.22606924643584522,
#  0.19583333333333333,
#  0.16032171581769436,
#  0.13612708846891264,
#  0.12135290838134176,
#  0.1080693707897377,
#  0.09105180533751962]
 

# x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_div = [0.4572192513368984,
#  0.32309746328437916,
#  0.28819212808539024,
#  0.44666666666666666,
#  0.2030231179608773,
#  0.1316886147691282,
#  0.11201493532470996]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.26229508196721313,
#  0.2073684210526316,
#  0.17707212055974167,
#  0.15120367865837164,
#  0.1283846012156935,
#  0.1138223051528635,
#  0.09617950272892663]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.412,
#  0.368,
#  0.3345,
#  0.25575,
#  0.2034586200811717,
#  0.16554777888873018,
#  0.14014878809695225]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_div, y_div, label = "Diversification", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="D")

# plt.xlabel('Number of Slots(Lambda)' )
# plt.ylabel( 'SI for HRD')
# plt.legend() 
# plt.show()

#---------------- alpha variation(0-1)----------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.1,0.2,0.4,0.6,0.8,1.0]
# y_r = [161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998,
#  161.23999999999998]
 

# # x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# # y_div = [0.4572192513368984,
# #  0.32309746328437916,
# #  0.28819212808539024,
# #  0.44666666666666666,
# #  0.2030231179608773,
# #  0.1316886147691282,
# #  0.11201493532470996]


# x_dr = [0.0,0.1,0.2,0.4,0.6,0.8,1.0]
# y_dr = [161.23999999999998,
#  148.95000000000002,
#  144.09000000000006,
#  142.52000000000004,
#  140.21000000000006,
#  138.81000000000006,
#  141.17000000000004]

# x_d = [0.0,0.1,0.2,0.4,0.6,0.8,1.0]
# y_d = [29.09,29.09,29.09,29.09,29.09,29.09,29.09]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# #plt.plot(x_div, y_div, label = "Diversification", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('Alpha Variation' )
# plt.ylabel( 'Total Revenue for 12000 slots')
# plt.legend() 
# plt.show()


#--------------------------------------------


# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.1,0.2,0.4,0.6,0.8,1.0]
# y_r = [0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787,
#  0.2861635220125787]
 

# # x_div = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# # y_div = [0.4572192513368984,
# #  0.32309746328437916,
# #  0.28819212808539024,
# #  0.44666666666666666,
# #  0.2030231179608773,
# #  0.1316886147691282,
# #  0.11201493532470996]


# x_dr = [0.0,0.1,0.2,0.4,0.6,0.8,1.0]
# y_dr = [0.2861635220125787,
#  0.3074324324324325,
#  0.31118881118881125,
#  0.31560283687943264,
#  0.32014388489208634,
#  0.33212560386473433,
#  0.34166666666666673]

# x_d = [0.0,0.1,0.2,0.4,0.6,0.8,1.0]
# y_d = [0.6666666666666667,0.6666666666666667,0.6666666666666667,0.6666666666666667,0.6666666666666667,0.6666666666666667,0.6666666666666667]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# #plt.plot(x_div, y_div, label = "Diversification", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('Alpha Variation' )
# plt.ylabel( 'drank-mean for 12000 slots')
# plt.legend() 
# plt.show()


##--------------------premiumness change---------------------------------------------


# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [78.03999999999999,
#  96.03999999999999,
#  126.87,
#  168.76999999999998,
#  207.74999999999991,
#  225.44999999999985,
#  229.21999999999986]

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [1.42,
#  2.4699999999999998,
#  17.66,
#  40.76,
#  52.37,
#  53.49999999999999,
#  51.43]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [74.25999999999998,
#  83.71999999999997,
#  112.30000000000001,
#  161.66999999999996,
#  177.14999999999998,
#  188.20999999999992,
#  200.0299999999999]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Total Revenue for alpha 5')
# plt.legend() 
# plt.show()

# #---------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.39864864864864863,
#  0.4423076923076923,
#  0.444,
#  0.4416167664670659,
#  0.4632352941176471,
#  0.4772727272727273,
#  0.4688888888888889]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.5704225352112676,
#  0.575,
#  0.615909090909091,
#  0.6462264150943396,
#  0.6557142857142857,
#  0.6550802139037433,
#  0.6568877551020408]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'Drank Mean for alpha 5')
# plt.legend() 
# plt.show()

##-----------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [
# 198.23999999999992,
# 198.23999999999992,
# 198.23999999999992,
# 198.23999999999992,
# 198.23999999999992,
# 198.23999999999992]
 


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [
# 185.33999999999995,
# 185.33999999999995,
# 185.33999999999995,
# 185.33999999999995,
# 185.33999999999995,
# 185.33999999999995]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [177.79999999999998,
#  212.92999999999995,
#  211.48999999999987,
#  207.7099999999999,
#  208.91999999999987,
#  205.28999999999994]

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [
# 53.589999999999996,
# 53.589999999999996,
# 53.589999999999996,
# 53.589999999999996,
# 53.589999999999996,
# 53.589999999999996]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('R ratio' )
# plt.ylabel( 'TR for 12000 slots')
# plt.legend() 
# plt.show()

#----------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [
# 0.30512820512820543,
# 0.30512820512820543,
# 0.30512820512820543,
# 0.30512820512820543,
# 0.30512820512820543,
# 0.30512820512820543]
 


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [
# 0.42714025500910774,
# 0.42714025500910774,
# 0.42714025500910774,
# 0.42714025500910774,
# 0.42714025500910774,
# 0.42714025500910774]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [0.42602996254681685,
#  0.3674603174603177,
#  0.3601895734597159,
#  0.3267973856209154,
#  0.3139158576051782,
#  0.31116584564860456]

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [
# 0.6666666666666666,
# 0.6666666666666666,
# 0.6666666666666666,
# 0.6666666666666666,
# 0.6666666666666666,
# 0.6666666666666666
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('R ratio' )
# plt.ylabel( 'DRank for 12000 slots')
# plt.legend() 
# plt.show()

#---------------------------rho3----------------------------
# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [79.56,
#  94.27,
#  118.33,
#  171.45999999999998,
#  200.45999999999992,
#  224.75999999999988,
#  231.9599999999999]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [2.69,
#  3.52,
#  16.59,
#  40.04999999999999,
#  50.55,
#  53.57,
#  54.13]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [75.83999999999999,
#  87.33999999999997,
#  110.2,
#  160.29999999999998,
#  180.03999999999996,
#  197.39999999999992,
#  198.9199999999999]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

#-----------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [
# 0.4066666666666667,
#  0.4388888888888889,
#  0.4465811965811966,
#  0.44642857142857145,
#  0.45454545454545453,
#  0.4649321266968326,
#  0.47013274336283184]
 


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [
# 0.5704225352112676,
#  0.5602409638554217,
#  0.6113636363636363,
#  0.6313291139240507,
#  0.6634078212290503,
#  0.6632653061224489,
#  0.6616161616161617]



# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [
# 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')

# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('Ts' )
# plt.ylabel( 'TR')
# plt.legend() 
# plt.show()

############################--------rho2grocery-----------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [78.22,
#  98.47,
#  124.17000000000003,
#  170.84999999999994,
#  210.1099999999999,
#  223.2499999999999,
#  229.05999999999986]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [1.42,
#  2.4699999999999998,
#  17.99,
#  33.6,
#  52.17,
#  51.88999999999999,
#  56.73999999999999]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [74.77999999999999,
#  91.91999999999999,
#  119.89000000000001,
#  156.49999999999997,
#  188.09999999999997,
#  200.2699999999999,
#  208.7199999999999]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'TR for alpha 2')
# plt.legend() 
# plt.show()

#-----------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [0.3918918918918919,
#  0.4473684210526316,
#  0.4573170731707317,
#  0.46407185628742514,
#  0.47101449275362317,
#  0.4794520547945205,
#  0.45535714285714285]
 


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [0.5144927536231884,
#  0.5340909090909091,
#  0.5529661016949152,
#  0.5931372549019608,
#  0.6044973544973545,
#  0.6111111111111112,
#  0.6086956521739131]



# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [
# 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')

# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('Ts' )
# plt.ylabel( 'TR')
# plt.legend() 
# plt.show()

#----------------------------------rho5_grocery1

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [79.56,
#  94.27,
#  118.33,
#  171.45999999999998,
#  200.45999999999992,
#  224.75999999999988,
#  231.9599999999999]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [2.69,
#  3.52,
#  16.59,
#  40.04999999999999,
#  50.55,
#  53.57,
#  54.13]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [75.83999999999999,
#  87.33999999999997,
#  110.2,
#  160.29999999999998,
#  180.03999999999996,
#  197.39999999999992,
#  198.9199999999999]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

# #-----------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [
# 0.4066666666666667,
#  0.4388888888888889,
#  0.4465811965811966,
#  0.44642857142857145,
#  0.45454545454545453,
#  0.4649321266968326,
#  0.47013274336283184]
 


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [
# 0.5704225352112676,
#  0.5602409638554217,
#  0.6113636363636363,
#  0.6313291139240507,
#  0.6634078212290503,
#  0.6632653061224489,
#  0.6616161616161617]



# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [
# 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')

# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('Ts' )
# plt.ylabel( 'Drank-mean for alpha 5')
# plt.legend() 
# plt.show()

# #----------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992]
 


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [
# 180.03999999999996,
# 180.03999999999996,
# 180.03999999999996,
# 180.03999999999996,
# 180.03999999999996,
# 180.03999999999996]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [184.82999999999993,
#  203.83999999999995,
#  208.99999999999994,
#  197.21999999999997,
#  192.57999999999993,
#  206.27999999999992]

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [
#  50.55, 50.55, 50.55, 50.55, 50.55, 50.55
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('R ratio' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

# #-----------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453]
 


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [
#  0.6634078212290503,
#  0.6634078212290503,
#  0.6634078212290503,
#  0.6634078212290503,
#  0.6634078212290503,
#  0.6634078212290503]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [0.6662162162162162,
#  0.5385572139303483,
#  0.533816425120773,
#  0.5025773195876289,
#  0.45466321243523317,
#  0.46782178217821785]

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [
#  1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('R ratio' )
# plt.ylabel( 'Drank-mean for alpha 5')
# plt.legend() 
# plt.show()

# #---------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0,2,4,8,12,16]
# y_r = [
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992]
 


# x_dr = [0,2,4,8,12,16]
# y_dr = [
#  202.9099999999999,
#  180.95999999999998,
#  185.31999999999996,
#  178.49999999999997,
#  179.23999999999995,
#  176.26999999999995]


# x_d = [0,2,4,8,12,16]
# y_d = [
#  50.55, 50.55, 50.55, 50.55, 50.55, 50.55
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('DTF' )
# plt.ylabel( 'TR')
# plt.legend() 
# plt.show()

# #------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0,2,4,8,12,16]
# y_r = [
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453]
 


# x_dr = [0,2,4,8,12,16]
# y_dr = [
#  0.47029702970297027,
#  0.6284530386740331,
#  0.6461748633879781,
#  0.6791666666666667,
#  0.6896067415730337,
#  0.71]


# x_d = [0,2,4,8,12,16]
# y_d = [
#  1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('DTF' )
# plt.ylabel( 'Drank-mean')
# plt.legend() 
# plt.show()

#------------------------pure nr, pure diversity---------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [37.40999999999999,
#  52.32,
#  64.78,
#  80.04000000000002,
#  95.75000000000003,
#  101.89000000000001,
#  103.08000000000003]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [0.48,
#  2.3099999999999996,
#  9.259999999999998,
#  18.810000000000002,
#  23.029999999999998,
#  25.909999999999997,
#  25.86]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [75.83999999999999,
#  87.33999999999997,
#  110.2,
#  160.29999999999998,
#  180.03999999999996,
#  197.39999999999992,
#  198.9199999999999]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

# #---------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [
# 0.0078125,
#  0.005319148936170213,
#  0.008333333333333333,
#  0.006578947368421052,
#  0.008152173913043478,
#  0.010309278350515464,
#  0.005]
 


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [
# 0.5704225352112676,
#  0.5602409638554217,
#  0.6113636363636363,
#  0.6313291139240507,
#  0.6634078212290503,
#  0.6632653061224489,
#  0.6616161616161617]



# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [
# 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')

# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('Ts' )
# plt.ylabel( 'Drank-mean for alpha 5')
# plt.legend() 
# plt.show()

# #--------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [
# 95.75000000000003,
# 95.75000000000003,
# 95.75000000000003,
# 95.75000000000003,
# 95.75000000000003,
# 95.75000000000003]
 


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [
# 180.03999999999996,
# 180.03999999999996,
# 180.03999999999996,
# 180.03999999999996,
# 180.03999999999996,
# 180.03999999999996]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [181.28999999999994,
#  202.26999999999992,
#  203.4799999999999,
#  183.97999999999993,
#  163.63999999999996,
#  95.37000000000003]

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [
#  23.029999999999998,
#  23.029999999999998,
#  23.029999999999998,
#  23.029999999999998,
#  23.029999999999998,
#  23.029999999999998
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('R ratio' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

# #-----------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [
# 0.008152173913043478,
# 0.008152173913043478,
# 0.008152173913043478,
# 0.008152173913043478,
# 0.008152173913043478,
# 0.008152173913043478]
 


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [
#  0.6634078212290503,
#  0.6634078212290503,
#  0.6634078212290503,
#  0.6634078212290503,
#  0.6634078212290503,
#  0.6634078212290503]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [0.6569444444444444,
#  0.5640703517587939,
#  0.4696969696969697,
#  0.39285714285714285,
#  0.33125,
#  0.008333333333333333]

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [
#  1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('R ratio' )
# plt.ylabel( 'Drank-mean for alpha 5')
# plt.legend() 
# plt.show()

# #---------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0,2,4,8,12,16]
# y_r = [
# 95.75000000000003,
# 95.75000000000003,
# 95.75000000000003,
# 95.75000000000003,
# 95.75000000000003,
# 95.75000000000003]
 


# x_dr = [0,2,4,8,12,16]
# y_dr = [
#  202.9099999999999,
#  180.95999999999998,
#  185.31999999999996,
#  178.49999999999997,
#  179.23999999999995,
#  176.26999999999995]


# x_d = [0,2,4,8,12,16]
# y_d = [
#  23.029999999999998,
#  23.029999999999998,
#  23.029999999999998,
#  23.029999999999998,
#  23.029999999999998,
#  23.029999999999998
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('DTF' )
# plt.ylabel( 'TR')
# plt.legend() 
# plt.show()

# # #------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0,2,4,8,12,16]
# y_r = [
# 0.008152173913043478,
# 0.008152173913043478,
# 0.008152173913043478,
# 0.008152173913043478,
# 0.008152173913043478,
# 0.008152173913043478]
 


# x_dr = [0,2,4,8,12,16]
# y_dr = [
#  0.47029702970297027,
#  0.6284530386740331,
#  0.6461748633879781,
#  0.6791666666666667,
#  0.6896067415730337,
#  0.71]


# x_d = [0,2,4,8,12,16]
# y_d = [
#  1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('DTF' )
# plt.ylabel( 'Drank-mean')
# plt.legend() 
# plt.show()


##------------------- no premiumness-------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [82.66,
#  110.95,
#  142.48000000000005,
#  186.73999999999998,
#  221.1099999999999,
#  244.93999999999986,
#  244.93999999999986]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [2.69,
#  4.109999999999999,
#  22.930000000000003,
#  50.169999999999995,
#  57.679999999999986,
#  57.679999999999986,
#  57.679999999999986]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [78.58999999999999,
#  98.83999999999999,
#  129.93000000000006,
#  178.22999999999996,
#  198.7999999999999,
#  204.09999999999988,
#  208.4999999999999]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity based", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# #plt.plot(x_h, y_rh, label = "NR + H combination", marker="D")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

# #-----------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [
# 0.40384615384615385,
#  0.4649532710280374,
#  0.45598591549295775,
#  0.45652173913043476,
#  0.4792626728110599,
#  0.48333333333333334,
#  0.48333333333333334]
 


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [
# 0.5733333333333334,
#  0.5885416666666666,
#  0.622093023255814,
#  0.6511299435028248,
#  0.6704545454545454,
#  0.6650246305418719,
#  0.6614077669902912]



# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [
# 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')

# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('Ts' )
# plt.ylabel( 'Drank-mean for alpha 5')
# plt.legend() 
# plt.show()

# # #----------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [
# 221.1099999999999,
# 221.1099999999999,
# 221.1099999999999,
# 221.1099999999999,
# 221.1099999999999,
# 221.1099999999999]
 


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [
# 198.7999999999999,
# 198.7999999999999,
# 198.7999999999999,
# 198.7999999999999,
# 198.7999999999999,
# 198.7999999999999]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [198.7999999999999,
#  226.71999999999989,
#  229.15999999999988,
#  224.5899999999999,
#  221.1099999999999,
#  221.1099999999999]

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [
#  57.679999999999986,
#  57.679999999999986,
#  57.679999999999986,
#  57.679999999999986,
#  57.679999999999986,
#  57.679999999999986
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('R ratio' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

# # #-----------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [
# 0.4792626728110599,
# 0.4792626728110599,
# 0.4792626728110599,
# 0.4792626728110599,
# 0.4792626728110599,
# 0.4792626728110599]
 


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [
#  0.6704545454545454,
#  0.6704545454545454,
#  0.6704545454545454,
#  0.6704545454545454,
#  0.6704545454545454,
#  0.6704545454545454]

# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [0.6704545454545454,
#  0.5591517857142857,
#  0.5575221238938053,
#  0.502262443438914,
#  0.4792626728110599,
#  0.4792626728110599]

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [
#  1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('R ratio' )
# plt.ylabel( 'Drank-mean for alpha 5')
# plt.legend() 
# plt.show()

# #-------------------not completed--------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0,2,4,8,12,16]
# y_r = [
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992,
# 200.45999999999992]
 


# x_dr = [0,2,4,8,12,16]
# y_dr = [
#  202.9099999999999,
#  180.95999999999998,
#  185.31999999999996,
#  178.49999999999997,
#  179.23999999999995,
#  176.26999999999995]


# x_d = [0,2,4,8,12,16]
# y_d = [
#  50.55, 50.55, 50.55, 50.55, 50.55, 50.55
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('DTF' )
# plt.ylabel( 'TR')
# plt.legend() 
# plt.show()

# #------------------------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0,2,4,8,12,16]
# y_r = [
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453,
# 0.45454545454545453]
 


# x_dr = [0,2,4,8,12,16]
# y_dr = [
#  0.47029702970297027,
#  0.6284530386740331,
#  0.6461748633879781,
#  0.6791666666666667,
#  0.6896067415730337,
#  0.71]


# x_d = [0,2,4,8,12,16]
# y_d = [
#  1.0, 1.0, 1.0, 1.0, 1.0, 1.0
# ]



# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# #plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_d, y_d, label = "Diversity", marker="v")

# plt.xlabel('DTF' )
# plt.ylabel( 'Drank-mean')
# plt.legend() 
# plt.show()

#---------------number patterns vs TR-------------------

#import matplotlib.pyplot as plt
#
#from cycler import cycler


#x_r =[10,20,30,40,50,60,70,80,90,100]
#y_r = [24487,15507,12185,10995,10227,9615,9098,8635,8205,7595]
 


#monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                 cycler('linestyle', ['-', '-', '-', '-']))

#plt.rcParams['figure.figsize'] = (6, 4)
## plt.rcParams['text.usetex'] = True
#plt.rcParams['font.family'] = 'serif'
#plt.rcParams['axes.labelsize'] = 'xx-large'
#plt.rcParams['xtick.labelsize'] = 'large'
#plt.rcParams['ytick.labelsize'] = 'large'
#plt.rcParams['lines.markersize'] = 5

#plt.rcParams['axes.prop_cycle'] = monochrome
#plt.rcParams['figure.autolayout'] = True

#plt.rcParams['lines.linewidth'] = 0.7

#plt.rcParams['legend.frameon'] = False

#plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
#plt.plot(x_rdr, y_rdr, label = "NR-DR", marker="|")
#plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
#plt.plot(x_d, y_d, label = "Diversity", marker="v")

#plt.xlabel('Top Revenue Patterns' )
#plt.ylabel( 'Net Revenue')
#plt.legend() 
#plt.show()

#---------------------new----------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_r = [82.66,
#  110.95,
#  142.48000000000005,
#  186.73999999999998,
#  221.1099999999999,
#  244.93999999999986,
#  244.93999999999986]
 

# x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_d = [2.69,
#  4.109999999999999,
#  22.930000000000003,
#  50.169999999999995,
#  57.679999999999986,
#  57.679999999999986,
#  57.679999999999986]


# x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_dr = [41.75,
#  54.74,
#  76.87000000000003,
#  99.71000000000001,
#  117.02,
#  134.85999999999996,
#  149.4699999999999]

# x_rdr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
# y_rdr = [53.06,
#  83.56,
#  120.78999999999999,
#  162.80999999999986,
#  192.27999999999986,
#  222.89999999999992,
#  243.9599999999999]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "DIP", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "HIP", marker="|")

# plt.xlabel('Number of Slots' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

#---------------------correct one----------------------

import matplotlib.pyplot as plt

from cycler import cycler


x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_r = [82.66,
 110.95,
 142.48000000000005,
 186.73999999999998,
 221.1099999999999,
 255.03999999999985,
 274.4399999999998]
 

x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_d = [2.69,
 4.109999999999999,
 22.930000000000003,
 50.169999999999995,
 74.46999999999998,
 87.44,
 99.33]


x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_dr = [60.57999999999998,
 80.90999999999998,
 113.58000000000001,
 155.94,
 181.21999999999997,
 208.36999999999986,
 220.20999999999987]


x_rdr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_rdr = [81.42999999999999,
 105.84999999999998,
 132.95000000000005,
 177.75999999999996,
 217.07999999999984,
 243.9099999999998,
 268.5999999999998]

x_rdr1 = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_rdr1 = [81.42999999999999,
 105.84999999999998,
 132.14000000000004,
 175.6,
 211.35999999999984,
 230.65999999999983,
 256.4099999999998]

x_rdr2 = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_rdr2 = [81.42999999999999,
 106.82999999999998,
 138.22000000000003,
 182.3299999999999,
 218.71999999999989,
 252.47999999999985,
 271.8499999999998]


monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
                 cycler('linestyle', ['-', '-', '-', '-']))

plt.rcParams['figure.figsize'] = (6, 4)
# plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.labelsize'] = 'xx-large'
plt.rcParams['xtick.labelsize'] = 'large'
plt.rcParams['ytick.labelsize'] = 'large'
plt.rcParams['lines.markersize'] = 5

plt.rcParams['axes.prop_cycle'] = monochrome
plt.rcParams['figure.autolayout'] = True

plt.rcParams['lines.linewidth'] = 0.7

plt.rcParams['legend.frameon'] = False

plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
plt.plot(x_d, y_d, label = "DIP", marker="v")
plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
plt.plot(x_rdr, y_rdr, label = "HIP-0.3", marker="|")
plt.plot(x_rdr1, y_rdr1, label = "HIP-0.2", marker="s")
plt.plot(x_rdr2, y_rdr2, label = "HIP-0.4", marker=".")


plt.xlabel('Ts' )
plt.ylabel( 'TR')
plt.legend() 
plt.show()

#-----------------------------------

import matplotlib.pyplot as plt

from cycler import cycler


x_r =[1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_r = [0.40384615384615385,
 0.4649532710280374,
 0.45598591549295775,
 0.45652173913043476,
 0.4792626728110599,
 0.498,
 0.5073529411764706]
 

x_d = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_d = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


x_dr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_dr = [0.6779661016949152,
 0.6829268292682927,
 0.7280701754385965,
 0.759493670886076,
 0.7703804347826086,
 0.775,
 0.7748868778280543]


x_rdr = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_rdr = [0.6,
 0.6242718446601942,
 0.6515267175572519,
 0.6689189189189189,
 0.67,
 0.6753968253968254,
 0.6996376811594203]


x_rdr1 = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_rdr1 = [0.62,
 0.6442718446601942,
 0.671923076923077,
 0.697027027027027,
 0.6944444444444444,
 0.6956972111553785,
 0.72]

x_rdr2 = [1000, 2000, 4000, 8000, 12000, 16000, 20000]
y_rdr2 = [0.55,
 0.5740384615384616,
 0.5824427480916031,
 0.5770618556701031,
 0.6091517857142857,
 0.6219844357976653,
 0.6109318996415771]


monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
                 cycler('linestyle', ['-', '-', '-', '-']))

plt.rcParams['figure.figsize'] = (6, 4)
# plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.labelsize'] = 'xx-large'
plt.rcParams['xtick.labelsize'] = 'large'
plt.rcParams['ytick.labelsize'] = 'large'
plt.rcParams['lines.markersize'] = 5

plt.rcParams['axes.prop_cycle'] = monochrome
plt.rcParams['figure.autolayout'] = True

plt.rcParams['lines.linewidth'] = 0.7

plt.rcParams['legend.frameon'] = False

plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
plt.plot(x_d, y_d, label = "DIP", marker="v")
plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
plt.plot(x_rdr, y_rdr, label = "HIP-0.3", marker="|")
plt.plot(x_rdr1, y_rdr1, label = "HIP-0.2", marker="s")
plt.plot(x_rdr2, y_rdr2, label = "HIP-0.4", marker=".")

plt.xlabel('Ts' )
plt.ylabel( 'DRank')
plt.legend() 
plt.show()

# #-----------------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [221.1099999999999,
# 221.1099999999999,
# 221.1099999999999,
# 221.1099999999999,
# 221.1099999999999,
# 221.1099999999999]
 

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [74.46999999999998,
# 74.46999999999998,
# 74.46999999999998,
# 74.46999999999998,
# 74.46999999999998,
# 74.46999999999998]


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [181.21999999999997,
# 181.21999999999997,
# 181.21999999999997,
# 181.21999999999997,
# 181.21999999999997,
# 181.21999999999997]


# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [221.1099999999999,
#  221.1099999999999,
#  221.10,
#  216.71999999999989,
#  200.35999999999984,
#  181.21999999999997]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "DIP", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "HIP", marker="|")

# plt.xlabel('R-Ratio' )
# plt.ylabel( 'TR for alpha 5')
# plt.legend() 
# plt.show()

# # #-----------------------------------

# import matplotlib.pyplot as plt

# from cycler import cycler


# x_r =[0.0,0.2,0.4,0.6,0.8,1.0]
# y_r = [0.4792626728110599,
# 0.4792626728110599,
# 0.4792626728110599,
# 0.4792626728110599,
# 0.4792626728110599,
# 0.4792626728110599]
 

# x_d = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_d = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


# x_dr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_dr = [0.7703804347826086,
# 0.7703804347826086,
# 0.7703804347826086,
# 0.7703804347826086,
# 0.7703804347826086,
# 0.7703804347826086]



# x_rdr = [0.0,0.2,0.4,0.6,0.8,1.0]
# y_rdr = [0.4792626728110599,
#  0.4792626728110599,
#  0.5045045045045045,
#  0.5591517857142857,
#  0.6244444444444444,
#  0.7703804347826086]


# monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
#                  cycler('linestyle', ['-', '-', '-', '-']))

# plt.rcParams['figure.figsize'] = (6, 4)
# # plt.rcParams['text.usetex'] = True
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['axes.labelsize'] = 'xx-large'
# plt.rcParams['xtick.labelsize'] = 'large'
# plt.rcParams['ytick.labelsize'] = 'large'
# plt.rcParams['lines.markersize'] = 5

# plt.rcParams['axes.prop_cycle'] = monochrome
# plt.rcParams['figure.autolayout'] = True

# plt.rcParams['lines.linewidth'] = 0.7

# plt.rcParams['legend.frameon'] = False

# plt.plot(x_r, y_r, label = "PRIP", marker="o", fillstyle='none')
# plt.plot(x_d, y_d, label = "DIP", marker="v")
# plt.plot(x_dr, y_dr, label = "DRIP", marker="*", fillstyle='none')
# plt.plot(x_rdr, y_rdr, label = "HIP", marker="|")

# plt.xlabel('R-Ratio' )
# plt.ylabel( 'DRank for alpha 5')
# plt.legend() 
# plt.show()

#--------------------------------------
