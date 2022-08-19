import 'package:fridaynight/choices_data.dart';

class CertificateRequest {
  String? uid, status;
  bool? accepted;
  bool? paymentStatus;
  bool? delivered;
  int? paymentAmount;
  String? certificate;

  fromJson(var data) {
    uid = data['id'];
    paymentAmount = data['paymentAmount'];
    paymentStatus = data['paymentStatus'];
    accepted = data['verified'];
    String deg = data['deliveryStatus'].toString();
    String cer = data['certificateStatus'].toString();
    int certindex = int.parse(cer[cer.length - 1]);
    int statIndex = int.parse(deg[deg.length - 1]);
    status = delivery_choices[statIndex];
    certificate = certificate_choices[certindex];
    delivered = data['deliveryDone'];
  }
}
