import 'package:flutter/material.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/utils.dart';
import 'package:get/get.dart';

class AcadamicTab extends StatefulWidget {
  const AcadamicTab({Key? key}) : super(key: key);

  @override
  State<AcadamicTab> createState() => _AcadamicTabState();
}

class _AcadamicTabState extends State<AcadamicTab> {
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
            itemContainer("My Subjects", Icons.menu_book, navigator(0)),
            itemContainer("My Grades", Icons.grade, navigator(1)),
            itemContainer(
                "Add Money", Icons.account_balance_wallet, navigator(2)),
            itemContainer("Req Transcript", Icons.description, navigator(3)),
            itemContainer("Req Migration", Icons.transfer_within_a_station, navigator(4)),
            itemContainer("Req Character", Icons.person, navigator(5)),
            itemContainer("Grievances", Icons.mail, navigator(6)),
          ],
        ),
      ],
    );
  }

  navigator(int index) {
    switch (index) {
      case 0:{Get.to(()=>);}
        
        break;
      default:
    }
    return;
  }

  Widget itemContainer(String title, IconData icon, ontap,
      {String? certificateIndex}) {
    return MaterialButton(
      padding: const EdgeInsets.all(0),
      onPressed: ontap,
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
