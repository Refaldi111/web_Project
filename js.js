var nilai = 89;

if (nilai > 90){
    grade = "A";
} else if (nilai > 80 && nilai <=90){
    grade = "B"
} else if (nilai >=75 && nilai < 81){
    grade = "C"
} else{
    grade = "D"
}

document.write("nilai: " + nilai + " termasuk grade: " + grade); 