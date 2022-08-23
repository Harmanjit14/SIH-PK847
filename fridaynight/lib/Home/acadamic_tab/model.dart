class Subjects {
  String? name, code, grade;
  int? marks;
  double? credits;

  fromJson(var data) {
    name = data['subject'];
    credits = data['credits'];
    code = data['subjectCode'];
    grade = data['grade'];
    marks = data['marks'];
  }
}
