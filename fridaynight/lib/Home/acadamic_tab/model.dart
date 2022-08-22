class Subjects {
  String? name, code, grade;
  double? credits, marks;

  fromJson(var data) {
    name = data['subject'];
    credits = data['credits'];
    code = data['subjectCode'];
    grade = data['grade'];
    marks = data['marks'];
  }
}
