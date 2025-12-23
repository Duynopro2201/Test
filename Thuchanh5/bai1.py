class Student():
    def __init__(self, id, name, scores):
        self.id = id
        self.name = name
        self.scores = scores
    def average(self):
        if not self.scores:
            return 0
        else:
            return sum(self.scores)/len(self.scores)
    def rank(self):
        avg = self.average()
        if avg >= 8:
            return "gioi"
        elif avg >= 6.5:
            return "kha"
        elif avg >= 5:
            return "dat"
        elif avg < 5:
            return "truot"
    def __str__(self):
        avg = self.average()
        return f"| {self.id:>6} | {self.name:>15} | {avg:>5.2f} | {self.rank():>6} |"
    
students = [
    Student("SV001", "Hieu", [8.5, 9.0, 7.5, 8.0]),
    Student("SV002", "Tu", [9.5, 9.0, 8.5, 9.2]),
    Student("SV003", "Duy", [6.5, 7.0, 6.0, 6.8]),
    Student("SV004", "Long", [4.5, 5.0, 4.2, 4.8]),
    Student("SV005", "Dung", [7.5, 8.0, 7.2, 7.8]),
    Student("SV006", "Loc", [8.8, 9.2, 8.5, 9.0])
]

sorted_students = sorted(students, key=lambda x: x.average(), reverse=True)

print("=" * 50)
print("BẢNG XẾP HẠNG SINH VIÊN THEO ĐIỂM TRUNG BÌNH")
print("=" * 50)
print(f"{'STT':>4} | {'Mã SV':>6} | {'Họ tên':>15} | {'Điểm TB':>8} | {'Xếp loại':>8}")
print("-" * 50)
for i, student in enumerate(sorted_students, 1):
    print(f"{i:>4} {student}")
print("=" * 50)