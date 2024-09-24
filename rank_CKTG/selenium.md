# TÌM HIỂU VÀ ĐÁNH GIÁ VỀ SELENIUM 🌐

## I. Tổng quan

### 1. Selenium là gì? 🧪
- Selenium là một framework kiểm thử tự động mã nguồn mở, miễn phí, được sử dụng để đánh giá các ứng dụng web trên trình duyệt và nền tảng.
- Selenium có thể được sử dụng bằng nhiều ngôn ngữ lập trình khác nhau như Java, C#, Python...

### 2. WebDriver là gì? 🖥️
- WebDriver là một giao diện lập trình ứng dụng (API) cho phép thực hiện thao tác trên các trình duyệt web như mở trang web, nhập dữ liệu, nhấn nút, kéo thả, chụp ảnh màn hình...
- WebDriver được ra đời vào năm 2006 bởi Simon Stewart, một kỹ sư phần mềm. Năm 2008, WebDriver được kết hợp với Selenium RC để tạo ra Selenium 2.0, phiên bản hiện tại của Selenium.

### 3. Tại sao nên sử dụng Selenium WebDriver? 🚀
- WebDriver hoàn toàn miễn phí và dễ sử dụng.
- WebDriver hỗ trợ nhiều ngôn ngữ lập trình khác nhau để bạn có thể viết kịch bản kiểm thử theo ý muốn.

### 4. Ưu điểm và nhược điểm ⚖️

#### Ưu điểm:
- **Mã nguồn mở**: Selenium WebDriver là một dự án mã nguồn mở, có nghĩa là bất cứ ai cũng có thể sử dụng và đóng góp vào dự án.
- **Tương thích nhiều trình duyệt**: Selenium WebDriver hỗ trợ nhiều trình duyệt phổ biến, bao gồm Chrome, Firefox, Edge, Safari...

#### Nhược điểm:
- **Chỉ hỗ trợ ứng dụng web**: Selenium WebDriver chỉ hỗ trợ kiểm thử tự động các ứng dụng web.
- **Đòi hỏi kinh nghiệm lập trình**: Để sử dụng Selenium WebDriver, bạn cần có kiến thức về lập trình.

### 5. Một vài khái niệm cần biết trong Selenium WebDriver 📖

#### 5.1. Session
- Session là một kết nối giữa WebDriver và trình duyệt.

#### 5.2. Element
- Element là đối tượng đại diện cho một thành phần của giao diện người dùng trên trang web.

#### 5.3. Locator
- Locator là một cách để xác định vị trí của một Element trên trang web.

#### 5.4. Wait
- Wait là một kỹ thuật cho phép bạn đợi một khoảng thời gian nhất định hoặc cho đến khi một điều kiện nào đó được thỏa mãn.

#### 5.5. Alert
- Alert là hộp thoại xuất hiện trên trang web, yêu cầu người dùng nhập liệu hoặc xác nhận một hành động nào đó.

### 6. Các kỹ thuật phổ biến trong Selenium WebDriver 🛠️
- **Page Object Model (POM)**: Kỹ thuật thiết kế cho phép bạn tách biệt mã lập trình của WebDriver với cấu trúc của giao diện web.
- **Data Driven Testing (DDT)**: Kỹ thuật cho phép bạn thực hiện cùng một ca kiểm thử với nhiều bộ dữ liệu khác nhau.

## II. Sử dụng Selenium 🛠️

### 1. Cài đặt 📦
- Đầu tiên, tải Selenium về môi trường bằng lệnh: `pip install selenium`.

### 2. Khởi tạo 🚀
- Đầu tiên cần khai báo các công cụ như `webdriver`, `Keys`, `By`:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.common.by import By
  ```

- `webdriver` là công cụ chính để duyệt trên các trình duyệt:
  ```python
  driver = webdriver.Firefox()
  driver.get("http://www.python.org")
  ```

- `By` là công cụ để trỏ đến những phần tử HTML trong một website:
  ```python
  driver.find_element(By.XPATH, '//button[text()="Some text"]')
  ```

## III. Kết luận 📝
Selenium là một công cụ mạnh mẽ cho việc kiểm thử tự động các ứng dụng web. Với khả năng tương tác trực tiếp với trình duyệt, nó giúp nâng cao chất lượng ứng dụng và tiết kiệm thời gian cho lập trình viên. 🌟