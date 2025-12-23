# Khởi tạo từ điển Anh - Việt ban đầu
dictionary = {
    "hello": "xin chào",
    "world": "thế giới",
    "computer": "máy tính",
    "program": "chương trình",
    "python": "ngôn ngữ lập trình Python"
}

# Vòng lặp chính của chương trình
running = True
while running:
    # 1. HIỂN THỊ MENU
    print("\n" + "=" * 25 + " TỪ ĐIỂN ANH VIỆT " + "=" * 25)
    print("1 - Tra từ điển")
    print("2 - Thêm từ điển")
    print("3 - Xóa từ điển")
    print("4 - Thoát chương trình")
    print("=" * 73)

    # 2. CHỌN CHỨC NĂNG
    choice = input("Mời bạn chọn chức năng (1-4): ").strip()

    # XỬ LÝ LỰA CHỌN CỦA NGƯỜI DÙNG

    # CHỨC NĂNG 1: TRA TỪ ĐIỂN
    if choice == '1':
        while True:
            print("\n--- Chức năng Tra từ điển ---")
            word_to_lookup = input("Nhập từ tiếng Anh cần tra (hoặc nhập 0 để quay lại menu): ").lower().strip()

            if word_to_lookup == '0':
                break

            if word_to_lookup in dictionary:
                print(f"✅ Nghĩa tiếng Việt của '{word_to_lookup}': **{dictionary[word_to_lookup]}**")
            else:
                print(f"❌ Không tìm thấy từ '{word_to_lookup}' này trong từ điển.")

            # Hỏi có muốn tra tiếp không
            while True:
                continue_lookup = input("Bạn có muốn tra tiếp không? (y/n): ").lower().strip()
                if continue_lookup == 'y':
                    break  # Tiếp tục tra
                elif continue_lookup == 'n':
                    # Dùng cờ để thoát vòng lặp tra từ và quay lại menu chính
                    word_to_lookup = '0' 
                    break 
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")
            
            if word_to_lookup == '0':
                break # Quay lại menu chính

    # CHỨC NĂNG 2: THÊM TỪ ĐIỂN
    elif choice == '2':
        while True:
            print("\n--- Chức năng Thêm từ điển ---")
            english_word = input("Nhập từ tiếng Anh (hoặc nhập 0 để quay lại menu): ").lower().strip()

            if english_word == '0':
                break
            
            if not english_word:
                 print("❌ Từ tiếng Anh không được để trống.")
                 continue

            if english_word in dictionary:
                print(f"⚠️ Từ '{english_word}' này đã có trong từ điển! Nghĩa hiện tại: {dictionary[english_word]}")
            else:
                vietnamese_meaning = input(f"Nhập nghĩa tiếng Việt cho từ '{english_word}': ").strip()
                if vietnamese_meaning:
                    dictionary[english_word] = vietnamese_meaning
                    print(f"✅ Đã thêm thành công từ '{english_word}' với nghĩa '{vietnamese_meaning}'!")
                else:
                    print("❌ Nghĩa tiếng Việt không được để trống. Thao tác thêm bị hủy.")

            # Hỏi có muốn thêm tiếp không
            while True:
                continue_add = input("Bạn có muốn thêm tiếp không? (y/n): ").lower().strip()
                if continue_add == 'y':
                    break # Tiếp tục thêm
                elif continue_add == 'n':
                    # Dùng cờ để thoát vòng lặp thêm từ và quay lại menu chính
                    english_word = '0' 
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")
            
            if english_word == '0':
                break # Quay lại menu chính

    # CHỨC NĂNG 3: XÓA TỪ ĐIỂN
    elif choice == '3':
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

            # Hỏi có muốn xóa tiếp không
            while True:
                continue_delete = input("Bạn có muốn xóa thêm không? (y/n): ").lower().strip()
                if continue_delete == 'y':
                    break # Tiếp tục xóa
                elif continue_delete == 'n':
                    # Dùng cờ để thoát vòng lặp xóa từ và quay lại menu chính
                    word_to_delete = '0'
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập 'y' hoặc 'n'.")

            if word_to_delete == '0':
                break # Quay lại menu chính

    # CHỨC NĂNG 4: THOÁT CHƯƠNG TRÌNH
    elif choice == '4':
        print("\nCảm ơn bạn đã sử dụng TỪ ĐIỂN ANH VIỆT! Hẹn gặp lại 👋")
        running = False # Dừng vòng lặp chính
        
    # XỬ LÝ LỰA CHỌN KHÔNG HỢP LỆ
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")