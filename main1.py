import re

comments_text = """
Nguyễn Phước Sang
511 Đinh Bảo Trân
Phản hồi
1 ngày
Ngô Linh
389 Kieu Gia Thinh
Phản hồi
1 ngày
Lê Tấn Mạnh
512 Hoang Nguyen
Phản hồi
8 giờ
Quân Lê
824 Hà Huỳnh yes
Phản hồi
17 giờ
Trần Quốc Dũng
121Nguyễn Hưng
Phản hồi
1 ngày
Trần Binn
162 Thuy Phg
Phản hồi
1 ngày
Nguyễn Gia Huân
163 Hoàng Tuệ Phong
Phản hồi
18 giờ
Lương Quang Trường
036 Lâm Đoàn
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Lương Quang Trường ông ni thì năm sau trúng, ông bà ko độ
Phản hồi
1 ngày
Lương Quang Trường
P-TWO Barber House  🫣🫣🫣 v chưa bik về ông vua vé số giải 8 rồi
Phản hồi
1 ngày
Kin Dương
125 Huỳnh Công Minh
Phản hồi
1 ngày
Quăn Hà
Lụm lụm
Phản hồi
1 ngày
Đức Trọng
288 Tinh Gia
Phản hồi
1 ngày
Minh Hiếu
202 Nguyễn Quốc Triệu
Phản hồi
1 ngày
Cao Nhật Minh
897 Như Lập
Phản hồi
1 ngày
Minh Nguyễn
975 Thanh Lâm lụm lụm lụm
Phản hồi
1 ngày
Hà Hoang Thi
Đỉnh quá cháu Hoàng Tuệ Phong ơi 🥰😍💪
Phản hồi
22 giờ
Tùng Châu
610 Nguyễn Đức Nam Nguyễn Duy Thông
Phản hồi
1 ngày
Nguyễn Vũ Lê Huy
712 Thanh Nguyễn siuuu
Phản hồi
1 ngày
Tô Tấn Tài
209 Đăng Quang zô =))
Phản hồi
1 ngày
Viet Ngoc
211 Thiện Thần
Phản hồi
1 ngày
Cyet Đào
479 Quang Sang
Phản hồi
1 ngày
Tom My
337 Hồ Xuân Đức
Phản hồi
20 giờ
Minh Huy
145 Nhu Hoang
Phản hồi
1 ngày
Phạm Hoàng Quang Huy
  · 
621 Nguyễn Ngọc Thiện
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Phạm Hoàng Quang Huy ai cho mà chơi đó
Phản hồi
1 ngày
Phạm Hoàng Quang Huy
  · 
P-TWO Barber House Làng Gốm Bát Tràng cử em đi chơi đó sốp
Phản hồi
1 ngày
Hoàng Sao Mai
893 Mai Phương
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Hoàng Sao Mai đánh lô mà nhờ anh haiiii
Phản hồi
1 ngày
Ng Q Hoang
237 Hùngg Trần
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Ng Q Hoang năm sau đi mễ rồi chơi chi màyyy
Phản hồi
1 ngày
Ng Q Hoang
P-TWO Barber House hả j khó rứa anh
Phản hồi
1 ngày
Ng Q Hoang
P-TWO Barber House lỡ trúng em đem đi mĩ dùng
Phản hồi
1 ngày
Nguyễn QuangHuy
46 Phạm Chương
Phản hồi
1 ngày
Nguyễn Trường
10 Thạch Thắng
Phản hồi
1 ngày
Nam Duong
754 Vinh Trần
Phản hồi
1 ngày
Tịnh Phạm
579 Hải Namm
Phản hồi
1 ngày
Hải Namm
719 Tịnh Phạm
Phản hồi
1 ngày
Tùng Lê
704 Thanh Tiến
Phản hồi
1 ngày
Trần Huy
068 Duc Nam
Phản hồi
1 ngày
Nguyễn QuangHuy
18 Phan Thảo Nhi
Phản hồi
1 ngày
Phạm Chương
Nguyễn QuangHuy m cmt nhiều rứa m
Phản hồi
1 ngày
Phạm Chương
134 Nguyễn Huỳnh Tuyết Ngân
Phản hồi
1 ngày
Khang Lê
192 Tống Phước Minh Quang
Phản hồi
1 ngày
Duc Nam
12 Tùng Lê
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Duc Nam du học sinh chơi làm chi
Phản hồi
1 ngày
Trương Khánh Linh
259 Tuyết Ngân
Phản hồi
1 ngày
Nguyễn Hồ Tấn Minh
165 Tiến Hồ
Phản hồi
1 ngày
Trần Nhật
259 Khánh Đậu
Phản hồi
1 ngày
Khánh Đậu
Trần Nhật trúng về chia đôi
Phản hồi
1 ngày
Trần Nhật
Khánh Đậu cái máy sấy chia kiểu gì
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Trần Nhật người dùng 246 người dùng 357
Phản hồi
1 ngày
Trần Nhật
P-TWO Barber House còn cn nữa
Phản hồi
1 ngày
Tiếnn Nguyễnn
17Đức Việt
Phản hồi
1 ngày
Quăn Hà
278 Mai Thành Toại
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Quăn Hà sáu múi tặng lun hộp whey
Phản hồi
1 ngày
Quăn Hà
P-TWO Barber House sáu múi mỡ tặng gì ạ
Phản hồi
23 giờ
Hùng Khánh
157 Ngọc Vui
Phản hồi
1 ngày
Quang Thiện
6 Gia Hưng
Phản hồi
1 ngày
Trung Thành
555 Hoàng Tuệ Phong
Phản hồi
1 ngày
Lee Nguyễn
247 Văn Phúc
Phản hồi
1 ngày
Jolie Phan
993 Trần Huy
Phản hồi
1 ngày
Trần Bích
999 Nguyễn Sang
Phản hồi
1 ngày
Bao Tran Thai
297 w Thanh Thanh
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Bao Tran Thai mốt trúng nha em🫶🏼
Phản hồi
1 ngày
Tinh Gia
Quang Thiện tag th minh vô e
Phản hồi
1 ngày
Nguyễn Quang Huy
256 Truong Manh Cuong
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Nguyễn Quang Huy tóc dài không cắt, quýnh lô thì giỏi lắm
Phản hồi
1 ngày
Tieu Manh Hung
184 Le Minh Dat
Phản hồi
1 ngày
Văn Chung
86 Bình Minh Phan
Phản hồi
1 ngày
Thanh Nguyễn
222 Nguyễn Vũ Lê Huy
Phản hồi
1 ngày
Trung Lê
194 Khoa Anh
Phản hồi
1 ngày
Tinh Gia
Quang Đức Lê Trần Phước Hậu kiếm sáp vuốt hai fen
Phản hồi
1 ngày
Hà Từ
285 Huynh Huynh
Phản hồi
1 ngày
Tinh Gia
Lý Bảo Hồ Trịnh Thanh Dũng Huỳnh Ngọc Phước
Phản hồi
1 ngày
Đã chỉnh sửa
Nhienquynh Pham
581 Bảo Hân Thu Sang
Phản hồi
1 ngày
Noel Phạm
246 Nguyễn Văn Sang anh thích giải mấy nào 🤣
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Noel Phạm người chơi hệ số chẵn hả c😂
Phản hồi
1 ngày
Noel Phạm
P-TWO Barber House có ẩn ý đằng sau con số hết 🤣
Phản hồi
1 ngày
Hòa Trần
777 Nguễn Tùng
Phản hồi
1 ngày
Hoang Nguyen
932 Lê Tấn Mạnh
Phản hồi
3 giờ
Đinh Bảo Trân
1 Nguyễn Phước Sang
Phản hồi
22 giờ
Hưng Phúc
Đặng Văn Tâm 333
Phản hồi
1 ngày
Ris Đặng
Lấy cho mình cái giải nhất , tặng mỗi người ly nước mía
Phản hồi
16 giờ
Nguyễn Trần Phi Long
7Đỗ Minh Hưng zô zô
Phản hồi
1 ngày
Nguyên Bảo
Lê Triệu Công 168
Phản hồi
1 ngày
Đình Bi
Salim Kha 222
Phản hồi
1 ngày
Võ Tấn Phúc
017 Vũ Khánh
Phản hồi
1 ngày
Trần Trực
246 Bi Pham
Phản hồi
1 ngày
Tiến Lê
Huỳnh Quân 535 húp
Phản hồi
1 ngày
Ng Thành Hải
279 Phạm Hoàng Quang Huy
Phản hồi
1 ngày
Gia Hiếu
537 Trần Long Vũ zô sếp ơi 😙
Phản hồi
1 ngày
Nguyễn Nhậtt Trường
Ngô Quốc Hải 2019
Phản hồi
1 ngày
Le Minh Dat
289 Tieu Manh Hung
Phản hồi
1 ngày
Hiệp Võ
Trần Khắc Quốc 174
Phản hồi
1 ngày
Thiều Huy
Phan Nguyên Huân 627
Phản hồi
1 ngày
Tạ Ngọc Dân
710 Nguyễn QuangHuy
Phản hồi
1 ngày
Viet Anh
Bae Chul 152
Phản hồi
1 ngày
Nguyễn Hưng
102 Hà Từ
Phản hồi
1 ngày
Gia Bảo
271 Quỳnh Trang
Phản hồi
15 giờ
Nguyễn Hồng Sơn
619 Phan Khải ăn giải hè
Phản hồi
1 ngày
Pham Ngoc Loc
270 Nguyễn Trọng Đạt
Phản hồi
1 ngày
Hoàng Ka
Văn Hoàng 315
Phản hồi
1 ngày
Phạm Hiếu
398 Hoàng Sao Mai
Phản hồi
22 giờ
Tinh Gia
Đức Trọng 461
Phản hồi
1 ngày
Đăng Quang
246 Tô Tấn Tài
Phản hồi
1 ngày
Nam Trần
Lộc Nguyễn 462
Phản hồi
1 ngày
LÊ TUẤN
689 Quốc Lee
Phản hồi
1 ngày
Tinh Gia
Quốc võ Lê Bảo Hoàng Hoàng Minh
Phản hồi
1 ngày
Trương Nguyễn Minh Quang
315 Trương Hoài Thanh
Phản hồi
1 ngày
Đã chỉnh sửa
Gia Bao
368 Tuan Phan
Phản hồi
1 ngày
Long Hoàng Cao
13 Trần Thanh Trâm
Phản hồi
1 ngày
Trần Thanh Trâm
Long Hoàng Cao chúc trúng cái máy sấy về cho họ nghe :))))
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Trần Thanh Trâm làm một con lô luôn cho nóng chị ơiii
Phản hồi
1 ngày
Long Hoàng Cao
Trần Thanh Trâm Chờ sốp cơ cấu =)))
Phản hồi
1 ngày
Thinh Do
438 Vương Thanh Vinh
Phản hồi
1 ngày
Ngô Trần Tuấn Duy
212 Kim Quy
Phản hồi
1 ngày
Tinh Gia
Khang Lê Thanh Nguyễn Bùi Đức Hào Nguyễn Hoàng Sơn Lâm Quốc Trần Nguyễn Sơn Lê Tuấn
Phản hồi
1 ngày
Đã chỉnh sửa
Huy Thiện
169 Đăng Khoa chúa phù hộ con zai :))))
Phản hồi
1 ngày
Nguyễn Ngọc Tuân
Nguyễn QuangHuy 169 t xin vía m nhé =))
Phản hồi
1 ngày

Tác giả
P-TWO Barber House
Nguyễn Ngọc Tuân b tin tuiiiii
Phản hồi
1 ngày
Zen Tran
228 nha! Trần Nam e trai tui
Phản hồi
19 giờ
Anh Khoa
Đoàn Đức 606
Phản hồi
1 ngày
Đăng Khoa
312 Hà Văn Thuận tag m thì cơ hội trúng giải x100 :))
Phản hồi
1 ngày
Quăn Hà
Phản hồi
1 ngày
Hải Vũ
555 Nguyễn Gia Bảo
Phản hồi
6 giờ
Trương Gia Beo
583 Lê Duy Hiếu
Phản hồi
5 giờ
Lương Nhi
777 Hoàng Tuệ Phong tag thẳng ông chủ lấy hên 😚
Phản hồi
1 ngày
Hoàng Tuệ Phong
Lương Nhi Fan cứng lun
Phản hồi
1 ngày
Lương Nhi
Hoàng Tuệ Phong fan cứng lâu rồi mãi mãi yêu #PTWO nhaaaa🔥♥️
Phản hồi
1 ngày
Đoàn Đức
225 Anh Khoa
Phản hồi
1 ngày
Hưng Duy
789 Hồng Vy
Phản hồi
6 giờ
Thanh Lâm
Minh Nguyễn cl 25 :))))
Phản hồi
1 ngày
Đã chỉnh sửa
Như Hoàng
510 Dao Nguyen Anh Quoc vô kiếm ít quà e ơi
Phản hồi
8 giờ
Trí Quang
249 Trần Tâm con chó duy nó tag
Phản hồi
1 ngày
Thanh Thanh
Trần Trực tham gia đi
Phản hồi
1 ngày
Nguyễn Gia Bảo
666 Hải Vũ
Phản hồi
17 giờ
Lê Duy Hiếu
328 Trương Gia Beo
Phản hồi
5 giờ
Phuong Mai
312 Công Chức qua cắt tóc đi
Phản hồi
1 ngày
Nguyễn Hoàng Sơn Lâm
thế yêu thích bài viết có được không hay là phải đúng thích Hoàng Tuệ PhongTinh GiaNguyễn QuangHuy 459
Phản hồi
1 ngày
Thanh Thanh
Phuong Mia tham gia kìa
Phản hồi
1 ngày
Khánh
271 Lê Đại Hải mượn nhân phẩm =))
Phản hồi
1 ngày
Zen Tran
300 tag anh người iu lấy hên Duy Khanh
Phản hồi
19 giờ
Minh Tuấn
Văn Chung Hưng Phúc Ng Q Hoang Viet Ngoc 274
Phản hồi
1 ngày
Văn Lê
Quí Nguyễn xin cái máy sấy 🥸 113
Phản hồi
1 ngày
Trần Tâm
236 Duy Nguyen Trí Quang xin phép tag 2 người ạ
Phản hồi
1 ngày
Duy Nguyen
666 Trí Quang xin vía anh cụt ạ
Phản hồi
1 ngày
Trần Hiền
369 Trần Trực Trần Bích khuyến mãi thêm 1 người😂
Phản hồi
1 ngày
Hằng Nga
734 Ris Đặng em tag anh chủ tăng độ may mắn dc ko ạ"""

# Define a pattern to extract usernames and numbers
pattern = re.compile(r'(\w+\s*\w*)\s+(\d+)')

# Find all matches
matches = pattern.findall(comments_text)

# Display the results
for match in matches:
    full_name = match[0]
    username = match[1]

    # Remove "hồi: 1" from the output
    full_name = full_name.replace("Phản hồi", "").replace("hồi", "").replace(":", "").strip()

    print(f"{full_name}: {username}")
