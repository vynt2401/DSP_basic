import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import firwin, lfilter


'''
1/ Tạo tín hiệu sin số  x1 có tần số 2khz và x2 có tần số 10khz, tần số lấy mẫu là 40khz
Thời gian lấy mẫu 10s
'''
fs = 40000 #tần số lấy mẫu
duration = 10# thời gian lấy mẫu
t = np.arange(0, duration, 1/fs)#khởi tạo vector thời gian bắt đầu từ 0 -> 10, với một steps = 1/fs

x1 = np.sin(2*np.pi*2000*t) 
x2 = np.sin(2*np.pi*10000*t)

'''2/ Tạo tín hiệu tổng x = x1 + x2'''

x = x1 + x2

'''3/ Sử dụng lọc FIR để loại x1 ra khỏi x
Cho biết các hệ số lọc và tần số cắt.

==> vì để loại x1 có tần số 2kHz ra khỏi x, cần lọc tần số thấp, giữ lại tần số cao. Nên ta sẽ sử dụng bộ lọc thông cao (high-pass filter)
'''

numtaps = 101 #số hệ số lọc
cutoff_highPass = 5000# f cắt
coeffs_highPass = firwin(numtaps, cutoff_highPass, fs=fs, pass_zero=False)

x_loc_highPass = lfilter(coeffs_highPass, 1.0, x)
#x_loc là tín hiệu x đã được lọc

'''4/ Sử dụng lọc FIR để loại x2 ra khỏi x
Cho biết các hệ số lọc và tần số cắt.'''


#==> vì để loại x2 có tần số 10kHz ra khỏi x, cần lọc tần số cao, giữ lại tần số thấp. Nên ta sẽ sử dụng bộ lọc thông thấp (low-pass filter)

cutoff_lowPass = 5000# f cắt
coeffs_lowPass = firwin(numtaps, cutoff_lowPass, fs=fs, pass_zero=True)

x_loc_lowPass = lfilter(coeffs_lowPass, 1.0, x)


#display

print("đợi tầm 5s để hiển thị trên màn hình khác")
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t[:1000], x[:1000])
plt.title("Tín hiệu tổng x = x1 + x2")

plt.subplot(3, 1, 2)
plt.plot(t[:1000], x_loc_highPass[:1000])
plt.title("Tín hiệu sau lọc High-pass (loại x1)")

plt.subplot(3, 1, 3)
plt.plot(t[:1000], x_loc_lowPass[:1000])
plt.title("Tín hiệu sau lọc Low-pass (loại x2)")

plt.tight_layout()
plt.show()
