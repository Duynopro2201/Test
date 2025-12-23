tu_dien={
    'hello':'xin chào',
    'goodbye':'tạm biệt',
    'love':'yêu'
}
while True:
    print('='*6 + 'TỪ ĐIỂN ANH-VIỆT' + '='*6)
    print('  1-Tra cứu')
    print('  2-Thêm từ điển')
    print('  3-Xóa từ điển')
    print('  4-Thoát chương trình')
    lua_chon=int(input('Nhập yêu cầu của bạn:'))
    if lua_chon==1:
        while True:
            tra_cuu=input('Từ bạn cần tra:').lower()
            if tra_cuu in tu_dien:
                print('Nghĩa của từ',tra_cuu,'là',tu_dien[tra_cuu])
            else:
                print('Từ',tra_cuu,'không có trong từ điển')
                them=input('❓Bạn có muốn thêm từ này vào từ điển không?(y/n):')
                if them=='y':
                    nghia=input('Nghĩa của từ đó là:')
                    tu_dien[tra_cuu]=nghia
                    print('✅ Đã thêm thành công')
                else:
                    print('👌 Ok bạn')
            tiep_tuc=input('❓Bạn có muốn tiếp tục không?(y/n):')
            if tiep_tuc=='y':
                continue
            else:
                print('🤝 Cảm ơn bạn đã sử dụng tra cứu từ')
                break
    elif lua_chon==2:
        while True:
            them1=input('Nhập từ cần thêm:').lower()
            
            if them1 in tu_dien:
                print('Từ',them1,' đã có trong từ điển')
                sua=input('❓Bạn có muốn sửa nghĩa của từ này không?(y/n):')
                if sua=='y':
                    nghia1=input('Nhập nghĩa của từ bạn muốn sửa:')
                    tu_dien[them1]=nghia1
                    print('✅ Đã sửa thành công')
                else:
                    print('👌 Ok bạn')
            else:
                nghia2=input('Nhập nghĩa của từ bạn muốn thêm:')
                tu_dien[them1]=nghia2
                print('✅ Đã thêm thành công')
            tieptuc2=input('❓Bạn có muốn tiếp tục không?(y/n):')
            if tieptuc2=='y':
                continue
            else:
                print('🤝 Cảm ơn bạn đã sử dụng thêm từ')
                break
    elif lua_chon==3:
        while True:
            Xoa=input('Nhập từ muốn xóa:')
            if Xoa in tu_dien:
                del tu_dien[Xoa]
                print('✅ Đã xóa thành công')
            else :
                print('Từ cần xóa không có trong từ điển')
            tieptuc3=input('❓Bạn có muốn tiếp tục không?(y/n):')
            if tieptuc2=='y':
                continue
            else:
                print('🤝Cảm ơn bạn đã sử dụng xóa từ')
                break
    elif lua_chon==4:
        print('🤝Cảm ơn bạn đã sử dụng từ điển')
        break
    else:
        print('⚠️ Yêu cầu không hợp lệ')  