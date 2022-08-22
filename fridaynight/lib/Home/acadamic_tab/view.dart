import 'package:flutter/material.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/Home/acadamic_tab/view_marks.dart';
import 'package:fridaynight/Home/acadamic_tab/view_subject.dart';
import 'package:fridaynight/utils.dart';
import 'package:get/get.dart';
import 'dart:convert';
import 'dart:io';

import 'package:fluttertoast/fluttertoast.dart';
import 'package:razorpay_flutter/razorpay_flutter.dart';

class AcadamicTab extends StatefulWidget {
  const AcadamicTab({Key? key}) : super(key: key);

  @override
  State<AcadamicTab> createState() => _AcadamicTabState();
}

class _AcadamicTabState extends State<AcadamicTab> {
  late Razorpay _razorpay;

  void _handlePaymentSuccess(PaymentSuccessResponse response) {
    return;
    // Do something when payment succeeds
  }

  void _handlePaymentError(PaymentFailureResponse response) {
    return;
    // Do something when payment fails
  }

  void _handleExternalWallet(ExternalWalletResponse response) {
    return;
    // Do something when an external wallet is selected
  }

  @override
  void initState() {
    _razorpay = Razorpay();
    _razorpay.on(Razorpay.EVENT_PAYMENT_SUCCESS, _handlePaymentSuccess);
    _razorpay.on(Razorpay.EVENT_PAYMENT_ERROR, _handlePaymentError);
    _razorpay.on(Razorpay.EVENT_EXTERNAL_WALLET, _handleExternalWallet);
    super.initState();
  }

  @override
  void dispose() {
    _razorpay.clear();
    super.dispose();
  }

  Future<void> generateODID(int amount) async {
    var orderOptions = {
      'amount': amount * 100, // amount in the smallest currency unit
      'currency': "INR",
      'receipt': "order_rcptid_11"
    };
    final client = HttpClient();
    final request =
        await client.postUrl(Uri.parse('https://api.razorpay.com/v1/orders'));
    request.headers
        .set(HttpHeaders.contentTypeHeader, "application/json; charset=UTF-8");
    String basicAuth =
        'Basic ${base64Encode(utf8.encode('$razorpayKey:$razorpaySecret'))}';
    request.headers.set(HttpHeaders.authorizationHeader, basicAuth);
    request.add(utf8.encode(json.encode(orderOptions)));
    final response = await request.close();
    response.transform(utf8.decoder).listen((contents) {
      debugPrint('ORDERID$contents');
      String orderId = contents.split(',')[0].split(":")[1];
      orderId = orderId.substring(1, orderId.length - 1);

      Fluttertoast.showToast(
          msg: "ORDERID: $orderId", toastLength: Toast.LENGTH_SHORT);

      Map<String, dynamic> checkoutOptions = {
        'key': razorpayKey,
        'amount': amount * 100,
        'name': 'Wallet Top-Up Demo',
        'description': '${institute.instituteName} Wallet recharge',
        'prefill': {'contact': student.mobile, 'email': student.email},
      };
      try {
        _razorpay.open(checkoutOptions);
      } catch (e) {
        debugPrint(e.toString());
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.max,
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        const Padding(
          padding: EdgeInsets.fromLTRB(20, 20, 20, 0),
          child: Text(
            "Academic Section",
            style: TextStyle(
                fontSize: 30,
                color: Colors.black,
                fontWeight: FontWeight.bold,
                shadows: [Shadow(color: Colors.black, blurRadius: 2)]),
          ),
        ),
        Padding(
          padding: const EdgeInsets.fromLTRB(20, 0, 20, 10),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Text(
                "My Wallet: ",
                style: TextStyle(
                  fontSize: 16,
                  color: Colors.black,
                ),
              ),
              const Icon(
                Icons.wallet,
                size: 23,
                color: Colors.black,
              ),
              const SizedBox(
                width: 5,
              ),
              Text(
                "Rs. ${student.wallet}",
                style: const TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: Colors.black,
                ),
              ),
            ],
          ),
        ),
        GridView(
          padding: const EdgeInsets.all(20),
          shrinkWrap: true,
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 3,
            crossAxisSpacing: 15,
            mainAxisSpacing: 10,
            childAspectRatio: (1),
          ),
          children: [
            itemContainer("My Subjects", Icons.menu_book, 0),
            itemContainer("My Grades", Icons.grade, 1),
            itemContainer("Add Money", Icons.account_balance_wallet, 2),
            itemContainer("Req Transcript", Icons.description, 3),
            itemContainer("Req Migration", Icons.transfer_within_a_station, 4),
            itemContainer("Req Character", Icons.person, 5),
            itemContainer("Grievances", Icons.mail, 6),
          ],
        ),
      ],
    );
  }

  navigator(int index) async {
    switch (index) {
      case 0:
        {
          int sem = await showSemesterSectionPopup(context);
          if (sem != -1) Get.to(() => ViewSubjects(sem));
          return;
        }
        case 1:
        {
          int sem = await showSemesterSectionPopup(context);
          if (sem != -1) Get.to(() => MarksView(sem));
          return;
        }
      default:
    }
    return;
  }

  Widget itemContainer(String title, IconData icon, int index,
      {String? certificateIndex}) {
    return MaterialButton(
      padding: const EdgeInsets.all(0),
      onPressed: () => navigator(index),
      child: Container(
        padding: const EdgeInsets.all(10),
        decoration: BoxDecoration(boxShadow: [
          BoxShadow(blurRadius: 2, color: light.shadow),
        ], color: light.primary, borderRadius: BorderRadius.circular(20)),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          mainAxisSize: MainAxisSize.max,
          children: [
            Icon(
              icon,
              size: 30,
              color: light.background,
            ),
            const SizedBox(
              height: 8,
            ),
            Text(
              title,
              textAlign: TextAlign.center,
              style: TextStyle(
                  color: light.background,
                  fontSize: 12,
                  shadows: const [Shadow(blurRadius: 2, color: Colors.black)]),
            )
          ],
        ),
      ),
    );
  }
}
