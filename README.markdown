# Xử Lý Tín Hiệu với Bộ Lọc FIR

Dự án này thể hiện việc sử dụng bộ lọc FIR (Finite Impulse Response) để xử lý tín hiệu số. Dự án tạo ra hai tín hiệu sin với tần số khác nhau, tổng hợp chúng, và áp dụng bộ lọc thông cao (high-pass) và thông thấp (low-pass) để tách các tín hiệu gốc. Kết quả được hiển thị bằng Matplotlib.

## Yêu Cầu

Để chạy dự án này, bạn cần cài đặt Python và các thư viện cần thiết. Dự án đã được kiểm tra với Python 3.8 trở lên.

### Thư viện cần thiết
Các thư viện Python sau đây là bắt buộc:
- `numpy`
- `scipy`
- `matplotlib`

## Cài Đặt

1. **Sao chép kho lưu trữ** (nếu có):
   ```bash
   git clone https://github.com/vynt2401/DSP_basic
   ```

2. **Tạo môi trường ảo** (khuyến nghị):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Trên Windows: venv\Scripts\activate
   ```

3. **Cài đặt các thư viện**:
   Tạo tệp `requirements.txt` với nội dung sau:
   ```
   numpy==1.24.3
   scipy==1.10.1
   matplotlib==3.7.1
   ```
   Sau đó chạy:
   ```bash
   pip install -r requirements.txt
   ```

## Cách Sử Dụng

1. **Chạy mã nguồn**:
   Đảm bảo bạn đang ở trong thư mục dự án và môi trường ảo đã được kích hoạt (nếu sử dụng). Sau đó thực thi:
   ```bash
   python main.py
   ```

2. **Kết quả mong đợi**:
   Mã nguồn sẽ tạo ra một biểu đồ với ba đồ thị con:
   - Tín hiệu tổng (`x = x1 + x2`).
   - Tín hiệu sau khi áp dụng bộ lọc thông cao để loại bỏ `x1` (2 kHz).
   - Tín hiệu sau khi áp dụng bộ lọc thông thấp để loại bỏ `x2` (10 kHz).

## Cấu Trúc Dự Án

- `main.py`: Tệp mã nguồn chính tạo tín hiệu sin, áp dụng bộ lọc FIR và hiển thị kết quả.
- `requirements.txt`: Liệt kê các thư viện Python cần thiết và phiên bản của chúng.
- `README.md`: Tệp này, cung cấp tổng quan và hướng dẫn cho dự án.

## Giải Thích Mã Nguồn

1. **Tạo Tín Hiệu**:
   - Tạo hai tín hiệu sin:
     - `x1`: Tần số 2 kHz.
     - `x2`: Tần số 10 kHz.
   - Tần số lấy mẫu: 40 kHz.
   - Thời gian lấy mẫu: 10 giây.
   - Tín hiệu tổng `x` là tổng của `x1` và `x2`.

2. **Lọc FIR**:
   - **Bộ lọc thông cao** (tần số cắt 5 kHz) được sử dụng để loại bỏ `x1` (2 kHz) và giữ lại `x2` (10 kHz).
   - **Bộ lọc thông thấp** (tần số cắt 5 kHz) được sử dụng để loại bỏ `x2` (10 kHz) và giữ lại `x1` (2 kHz).
   - Hàm `firwin` từ `scipy.signal` thiết kế các hệ số lọc, và `lfilter` áp dụng các bộ lọc.

3. **Hiển Thị**:
   - Matplotlib được sử dụng để vẽ biểu đồ của 1000 mẫu đầu tiên của:
     - Tín hiệu tổng.
     - Tín hiệu sau khi lọc thông cao.
     - Tín hiệu sau khi lọc thông thấp.

## Lưu Ý

- Số hệ số lọc (`numtaps = 101`) và tần số cắt (5 kHz) có thể được điều chỉnh trong `main.py` để thử nghiệm hiệu suất bộ lọc.
- Đảm bảo tần số lấy mẫu (40 kHz) đủ cao để tránh hiện tượng aliasing đối với các tần số tín hiệu đã cho.
- Các biểu đồ chỉ hiển thị 1000 mẫu đầu tiên để rõ ràng, nhưng có thể sửa đổi trong mã nguồn.

## Khắc Phục Sự Cố

- **Thiếu thư viện**: Nếu gặp lỗi như `ModuleNotFoundError`, hãy đảm bảo đã cài đặt tất cả các thư viện bằng lệnh `pip install -r requirements.txt`.
- **Biểu đồ không hiển thị**: Đảm bảo `matplotlib` được cài đặt đúng và môi trường của bạn hỗ trợ đầu ra đồ họa (ví dụ: trên một số hệ thống Linux, bạn có thể cần máy chủ hiển thị hoặc lưu biểu đồ vào tệp).

## Giấy Phép

Dự án này được cấp phép theo Giấy phép MIT.
