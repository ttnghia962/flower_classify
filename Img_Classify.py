import scipy.io
import numpy as np

# Đường dẫn đến tệp imagelabels.mat
file_path = 'D:/Tai Lieu FPT/1_DBM301/imagelabels.mat'
# Đọc dữ liệu từ tệp mat
mat_data = scipy.io.loadmat(file_path)
print("Các biến có trong tệp MAT:", mat_data.keys())
header_variable_name = '__header__'
label_variable_name = 'labels'

# # Lấy dữ liệu nhãn từ biến tương ứng
labels = mat_data[header_variable_name]
print(labels)

# unique_values = np.unique(labels)


# # In dữ liệu nhãn
# print("Dữ liệu nhãn:", unique_values)

# # iterator = iter(mat_data.items())
# # first_element = next(iterator)
# # second_element = next(iterator)
# # print(first_element)
# # print(second_element)

# # # Lấy dữ liệu của các nhãn từ biến tương ứng trong tệp mat
# # # Chú ý rằng tên biến có thể khác nhau tùy thuộc vào cách tệp mat được tạo ra
# # labels = mat_data['labels']

# # print(type(labels))



# # Hiển thị nội dung của biến nhãn


# # Chuyển đổi từ điển thành iterator và lấy hai phần tử đầu tiên



