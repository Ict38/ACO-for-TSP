# ACO-for-TSP
## Chuẩn bị
Cài đặt Python và pip cho máy <br>
Cài đặt thư viện Pyplot bằng cách sử dụng lệnh `pip install matplotlib`
## Chạy ứng dụng
### Cài đặt input (main.py)
Trong code có 2 cách để tạo dữ liệu đầu vào cho thuật toán: <br>
Cách 1: Sử dụng hàm random tạo để sinh ra tọa độ các thành phố dưới dạng tuple(x,y) với x,y là tung và hoành độ trên đồ thị <br>
```_nodes = [(random.uniform(-400, 400), random.uniform(-400, 400)) for _ in range(0, 15)]``` <br> (Đây là code áp dụng cho trường hợp 16 node)

Cách 2: Sử dụng dữ liệu được ghi sẵn từ trong file .txt ở ngoài : <br>
Dữ liệu từ file txt: <br>
![image](https://user-images.githubusercontent.com/88889991/169465385-4f4ddfb2-b5c6-4b55-b5c6-37a9ad3d8b34.png) <br>
Code để lấy dữ liệu từ trong file txt:
```  _nodes = []
    with open('E:/Ant_Colony/input.txt') as f:
        for line in f.readlines():
            print(line)
            city = line.split(' ')
            city[1].replace("\n","")
            print(city)
            a = (float(city[0]) , float(city[1]))
            _nodes.append(a)
 ```
 
 ### Thay đổi tham số thuật toán (aco.py)
  ```def __init__(self, mode='ACS', colony_size=20, elitist_weight=1.0, min_scaling_factor=0.001, alpha=1.0, beta=3.0,
                 rho=0.1, pheromone_deposit_weight=1.0, initial_pheromone=1.0, steps=30, nodes=None):
   ```
   Ngoài thay đổi số thành phố trong bài toán TSP ở trong code có thể điều chỉnh các tham số tham gia vào thuật toán và các biến thể trong file aco.py chi tiết các tham số em đã giải thích trong phần báo cáo
              
 ### Chạy thuật toán
 Run file main.py để chạy thuật toán <br>
 Hệ thống hiển thị danh sách các node trong input: <br>
![image](https://user-images.githubusercontent.com/88889991/169467586-c5933116-d0ee-4a10-bf3f-489053f70390.png) <br>
Lần lượt hệ thống hiển thị kết quả của 3 hệ thống kiến và hình ảnh trên đồ thị được vẽ bằng file plot.py sử dụng thư viện pyplot đã cài bên trên: <br>
![image](https://user-images.githubusercontent.com/88889991/169467785-6b819c2d-4619-4986-97d8-6ba8bd390b47.png)
<br> ![image](https://user-images.githubusercontent.com/88889991/169467830-47fcfda0-05f7-4739-8eba-33c087855706.png) <br>
Có thể tùy chọn lưu ảnh hoặc không và ấn tắt hình ảnh để hệ thống tiếp tục thực hiện các hệ thống sau: <br>
![image](https://user-images.githubusercontent.com/88889991/169467954-65135bab-7721-4fb6-9d75-9e17bd32246d.png) <br> 
![image](https://user-images.githubusercontent.com/88889991/169468047-29305b2f-751e-4362-a2a7-8e055bf1e8d1.png)
<br>
![image](https://user-images.githubusercontent.com/88889991/169468146-670a435b-3a27-4615-8b82-f2dc57a977a6.png)
<br>
![image](https://user-images.githubusercontent.com/88889991/169468166-3dcc6c6d-432f-4d09-a9cf-d35d2139d7bb.png)



 
