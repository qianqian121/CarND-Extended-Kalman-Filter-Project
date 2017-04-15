import matplotlib.pyplot as plt
import pandas as pd

my_cols=['px_est','py_est','vx_est','vy_est','px_meas','py_meas','px_gt','py_gt','vx_gt','vy_gt']
#with open('/root/sharefolder/udacity/CarND-Extended-Kalman-Filter-Project/build/output2.txt') as f:
with open('./output2.txt') as f:
    table_ekf_output = pd.read_table(f, sep='\t', header=None, names=my_cols, lineterminator='\n')
    
#table_ekf_output

x1=table_ekf_output['px_est']
y1=table_ekf_output['py_est']
x2=table_ekf_output['px_meas']
y2=table_ekf_output['py_meas']
x3=table_ekf_output['px_gt']
y3=table_ekf_output['py_gt']
plt.plot(x1, y1, x2, y2, x3, y3, linewidth=2.0)
plt.show()
