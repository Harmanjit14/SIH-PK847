import 'package:fridaynight/choices_data.dart';

class CertificateRequest {
  String? uid, status;
  bool? accepted;
  bool? paymentStatus;
  bool? delivered;
  int? paymentAmount;

  fromJson(var data) {
    uid = data['id'];
    paymentAmount = data['paymentAmount'];
    paymentStatus = data['paymentStatus'];
    accepted = data['verified'];
    String deg = data['deliveryStatus'].toString();
    int statIndex = int.parse(deg[deg.length - 1]);
    status = delivery_choices[statIndex];
    delivered = data['deliveryDone'];
  }
}
