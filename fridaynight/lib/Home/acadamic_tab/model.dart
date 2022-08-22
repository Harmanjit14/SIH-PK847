class Subjects {
  String? name, code;
  double? credits;

  fromJson(var data) {
    name = data['subject'];
    credits = data['credits'];
    code = data['subjectCode'];
  }
}
