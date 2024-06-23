### Odoo 17 README

![Odoo Logo](![image](https://github.com/hl2802/odoo/assets/93818052/b72de42b-f3b8-42b1-8524-76511d3fcf65)
)

---

### 🌟 Giới thiệu

Đây là tài liệu README hướng dẫn cài đặt, chạy và kết nối Odoo 17 với Docker.

### 🚀 Cách cài đặt và chạy Odoo 17 với Docker

#### 📋 Bước 1: Chuẩn bị môi trường

- Đảm bảo bạn đã cài đặt Docker và Docker Compose trên máy tính của bạn. 🐋

#### 📂 Bước 2: Tạo file `docker-compose.yml`

```yaml
version: '3'
services:
  odoo:
    image: odoo:17.0
    ports:
      - "8069:8069"
    depends_on:
      - db
    environment:
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_DB=postgres
    volumes:
      - ./addons:/mnt/extra-addons
  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_DB=postgres
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

volumes:
  odoo-db-data:
```

#### ▶️ Bước 3: Chạy Odoo 17

Mở terminal và di chuyển đến thư mục chứa file `docker-compose.yml`, sau đó chạy lệnh:

```bash
docker-compose up
```

Sau khi các container đã khởi động, Odoo sẽ có thể truy cập thông qua địa chỉ: `http://localhost:8069`. 🌐

#### 🔗 Bước 4: Kết nối và sử dụng Odoo

- Truy cập Odoo qua trình duyệt web tại `http://localhost:8069`.
- Đăng nhập vào Odoo sử dụng tài khoản mặc định (admin/admin) hoặc tạo một tài khoản mới.

### 🔧 Biểu tượng

Dưới đây là một số biểu tượng đơn giản để hỗ trợ việc hiển thị:

- Docker: ![Docker Logo](docker-logo.png) 🐳
- Odoo: ![Odoo Logo](odoo-logo.png) 🛠️
- PostgreSQL: ![PostgreSQL Logo](postgres-logo.png) 🐘

### 💬 Hỗ trợ

Nếu gặp bất kỳ vấn đề nào trong quá trình cài đặt hoặc sử dụng, vui lòng xem thêm tài liệu [Odoo Documentation](https://www.odoo.com/documentation/17.0) hoặc liên hệ với cộng đồng Odoo để được hỗ trợ.

---

© 2024 Your Company
