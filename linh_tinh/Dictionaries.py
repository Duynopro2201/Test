# Khởi tạo từ điển Anh - Việt ban đầu
# Key là từ tiếng Anh, Value là nghĩa tiếng Việt
dictionary = {
    "hello": "xin chào",
    "world": "thế giới",
    "computer": "máy tính",
    "program": "chương trình",
    "python": "ngôn ngữ lập trình Python"
}

def display_menu():
    """Hiển thị menu chức năng."""
    print("\n" + "=" * 25 + " TỪ ĐIỂN ANH VIỆT " + "=" * 25)
    print("1 - Tra từ điển")
    print("2 - Thêm từ điển")
    print("3 - Xóa từ điển")
    print("4 - Thoát chương trình")
    print("=" * 73)

def lookup_word():
    """Chức năng 1: Tra từ điển."""
    while True:
        print("\n--- Chức năng Tra từ điển ---")
        word_to_lookup = input("Nhập từ tiếng Anh cần tra (hoặc nhập 0 để quay lại menu): ").lower().strip() # Chuyển sang chữ thường để tìm kiếm không phân biệt hoa thường

        if word_to_lookup == '0':
            break

        if word_to_lookup in dictionary:
            print(f"✅ Nghĩa tiếng Việt của '{word_to_lookup}': **{dictionary[word_to_lookup]}**")
        else:
            print(f"❌ Không tìm thấy từ '{word_to_lookup}' này trong từ điển.")

        # Hỏi người dùng có muốn tra tiếp không
        while True:
            choice = input("Bạn có muốn tra tiếp không? (y/n): ").lower().strip()
            if choice == 'y':
                break  # Thoát khỏi vòng lặp hỏi và tiếp tục tra
            elif choice == 'n':
                return # Quay lại menu chính
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")

def add_word():
    """Chức năng 2: Thêm từ điển."""
    while True:
        print("\n--- Chức năng Thêm từ điển ---")
        english_word = input("Nhập từ tiếng Anh (hoặc nhập 0 để quay lại menu): ").lower().strip()

        if english_word == '0':
            break

        if english_word in dictionary:
            print(f"⚠️ Từ '{english_word}' này đã có trong từ điển! Nghĩa hiện tại: {dictionary[english_word]}")
        else:
            vietnamese_meaning = input(f"Nhập nghĩa tiếng Việt cho từ '{english_word}': ").strip()
            if vietnamese_meaning: # Đảm bảo người dùng nhập nghĩa
                dictionary[english_word] = vietnamese_meaning
                print(f"✅ Đã thêm thành công từ '{english_word}' với nghĩa '{vietnamese_meaning}'!")
            else:
                print("❌ Nghĩa tiếng Việt không được để trống. Thao tác thêm bị hủy.")

        # Hỏi người dùng có muốn thêm tiếp không
        while True:
            choice = input("Bạn có muốn thêm tiếp không? (y/n): ").lower().strip()
            if choice == 'y':
                break  # Thoát khỏi vòng lặp hỏi và tiếp tục thêm
            elif choice == 'n':
                return # Quay lại menu chính
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")

def delete_word():
    """Chức năng 3: Xóa từ điển."""
    while True:
        print("\n--- Chức năng Xóa từ điển ---")
        word_to_delete = input("Nhập từ tiếng Anh muốn xóa (hoặc nhập 0 để quay lại menu): ").lower().strip()

        if word_to_delete == '0':
            break

        if word_to_delete in dictionary:
            del dictionary[word_to_delete]
            print(f"✅ Đã xóa thành công từ '{word_to_delete}'!")
        else:
            print(f"❌ Không tìm thấy từ '{word_to_delete}' cần xóa.")

        # Hỏi người dùng có muốn xóa thêm không
        while True:
            choice = input("Bạn có muốn xóa thêm không? (y/n): ").lower().strip()
            if choice == 'y':
                break # Thoát khỏi vòng lặp hỏi và tiếp tục xóa
            elif choice == 'n':
                return # Quay lại menu chính
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")

def main():
    """Hàm chính điều khiển chương trình."""
    while True:
        display_menu()
        choice = input("Mời bạn chọn chức năng (1-4): ").strip()

        if choice == '1':
            lookup_word()
        elif choice == '2':
            add_word()
        elif choice == '3':
            delete_word()
        elif choice == '4':
            print("\nCảm ơn bạn đã sử dụng TỪ ĐIỂN ẢNH VIỆT! Hẹn gặp lại 👋")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

# Chạy chương trình
if __name__ == "__main__":
    main()