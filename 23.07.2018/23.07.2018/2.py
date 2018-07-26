## pep8 standart arşatırr


students = {
        '120101003': {'vize': 80, "final": 90},
        '120101004': {'vize': 60, "final": 100}
    }

try:
    file=open('ogrenciler.txt','w')

except Exception:
    file=open('ogrenciler.txt','x')

    for std_no, grades in students.items():
        file.write("{} number of students vise:{} final:{}",format(std_no,grades.get('vise'),grades.get('final')))







#ogernci kayit islemi
#ogrenci silme
#ogencileri goruntuleme
#ogrencileri temizleme









