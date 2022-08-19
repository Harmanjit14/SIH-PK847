import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:fridaynight/Home/request_tab/model.dart';
import 'package:fridaynight/Home/request_tab/query.dart';
import 'package:fridaynight/utils.dart';

class RequestsTab extends StatefulWidget {
  const RequestsTab({Key? key}) : super(key: key);

  @override
  State<RequestsTab> createState() => _RequestsTabState();
}

class _RequestsTabState extends State<RequestsTab> {
  @override
  Widget build(BuildContext context) {
    return ListView(
      shrinkWrap: true,
      children: [
        const Padding(
          padding: EdgeInsets.fromLTRB(20, 20, 20, 10),
          child: Text(
            "My Requests",
            style: TextStyle(
                fontSize: 35,
                color: Colors.black,
                fontWeight: FontWeight.bold,
                shadows: [Shadow(color: Colors.black, blurRadius: 2)]),
          ),
        ),
        GridView.builder(
          padding: const EdgeInsets.all(20),
          shrinkWrap: true,
          itemCount: requestList!.length,
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
            crossAxisSpacing: 15,
            mainAxisSpacing: 10,
            childAspectRatio: (1),
          ),
          itemBuilder: (
            context,
            index,
          ) {
            return requestContainer(requestList![index]);
          },
        ),
      ],
    );
  }

  Widget requestContainer(CertificateRequest request) {
    return Container(
      decoration: BoxDecoration(boxShadow: [
        BoxShadow(blurRadius: 2, color: light.shadow),
      ], color: light.background, borderRadius: BorderRadius.circular(20)),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: light.primary,
              borderRadius: const BorderRadius.only(
                  topLeft: Radius.circular(20), topRight: Radius.circular(20)),
            ),
            child: Text(
              request.certificate ?? "",
              textAlign: TextAlign.center,
              style: TextStyle(
                  fontWeight: FontWeight.bold,
                  color: light.background,
                  fontSize: 16,
                  shadows: const [Shadow()]),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(15),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              mainAxisSize: MainAxisSize.max,
              children: [
                if (!request.accepted!)
                  const Text(
                    "Your Certificate request is currently not accepted by Institute, sit back and relax we have informed them.",
                    textAlign: TextAlign.justify,
                  ),
                // Text(
                //   "Payment Rs.${request.paymentAmount!}",
                //   textAlign: TextAlign.justify,
                //   style: const TextStyle(
                //       fontWeight: FontWeight.bold, fontSize: 16),
                // ),
                Text(
                  "Status: ${request.status!}",
                  textAlign: TextAlign.justify,
                  style: const TextStyle(
                      fontWeight: FontWeight.bold, fontSize: 16),
                )
              ],
            ),
          )
        ],
      ),
    );
  }
}
