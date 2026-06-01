raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    user_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if user_choice == "1":
        print("--- CHUỖI DỮ LIỆU GỐC ---")
        print(raw_data)

    elif user_choice == "2":
        print("--- BÁO CÁO NHÂN SỰ ĐÃ CHUẨN HÓA ---")
        print("Mã NV | Họ và Tên | Số Điện Thoại | Phòng Ban")
        print("-" * 50)

        raw_employees = raw_data.split("|")

        for item in raw_employees:
            fields = item.split(";")

            count = 0
            for f in fields:
                count += 1
            if count < 4:
                continue

            emp_id = fields[0].strip().upper()
            emp_name = fields[1].strip().title()
            department = fields[3].strip().upper()

            raw_phone = fields[2].strip().replace("-", "")

            if raw_phone.isdigit():
                hidden_phone = "******" + raw_phone[6:]
            else:
                hidden_phone = "Invalid Format"

            print(emp_id, "|", emp_name, "|", hidden_phone, "|", department)

    elif user_choice == "3":
        print("--- TÌM KIẾM NHÂN VIÊN ---")
        search_input = input("Nhập mã nhân viên cần tìm: ")

        clean_search_key = search_input.strip().upper()
        is_found = False

        raw_employees = raw_data.split("|")

        for item in raw_employees:
            fields = item.split(";")

            count = 0
            for f in fields:
                count += 1
            if count < 4:
                continue

            current_id = fields[0].strip().upper()

            if current_id == clean_search_key:
                emp_name = fields[1].strip().title()
                department = fields[3].strip().upper()

                raw_phone = fields[2].strip().replace("-", "")
                if raw_phone.isdigit():
                    hidden_phone = "******" + raw_phone[6:]
                else:
                    hidden_phone = "Invalid Format"

                print("KẾT QUẢ TÌM THẤY")
                print("Mã nhân viên:", current_id)
                print("Họ và tên:", emp_name)
                print("Số điện thoại:", hidden_phone)
                print("Phòng ban:", department)

                is_found = True
                break

        if not is_found:
            print("Không tìm thấy nhân viên")

    elif user_choice == "4":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")