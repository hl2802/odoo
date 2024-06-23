# Sử dụng image base từ Odoo 17
FROM odoo:17


# Copy file cấu hình odoo.conf vào container
COPY ./odoo.conf /etc/odoo/odoo.conf

# Thêm entrypoint để chạy Odoo với cấu hình từ odoo.conf
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]
