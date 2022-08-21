import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
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
    return FutureBuilder<List<CertificateRequest>?>(
      future: getStudentRequest(),
      builder: ((context, snapshot) {
        switch (snapshot.connectionState) {
          case ConnectionState.waiting:
            return Center(
                child: SpinKitWave(
              color: light.primary.withOpacity(0.4),
            ));
          default:
            if (snapshot.hasError) {
              return Center(
                  child: Center(child: Text('Error: ${snapshot.error}')));
            } else {
              List<CertificateRequest>? requestList = snapshot.data;
              if (requestList!.isEmpty) {
                return const Center(
                  child: Text("No Requests so far.."),
                );
              }
              return ListView(
                shrinkWrap: true,
                children: [
                  const Padding(
                    padding: EdgeInsets.fromLTRB(20, 20, 20, 10),
                    child: Text(
                      "My Requests",
                      style: TextStyle(
                          fontSize: 30,
                          color: Colors.black,
                          fontWeight: FontWeight.bold,
                          shadows: [
                            Shadow(color: Colors.black, blurRadius: 2)
                          ]),
                    ),
                  ),
                  GridView.builder(
                    padding: const EdgeInsets.all(20),
                    shrinkWrap: true,
                    itemCount: requestList.length,
                    gridDelegate:
                        const SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisCount: 2,
                      crossAxisSpacing: 15,
                      mainAxisSpacing: 10,
                      childAspectRatio: (1),
                    ),
                    itemBuilder: (
                      context,
                      index,
                    ) {
                      return requestContainer(requestList[index]);
                    },
                  ),
                ],
              );
              ;
            }
        }
      }),
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
        mainAxisSize: MainAxisSize.max,
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
                  fontSize: 14,
                  shadows: const [Shadow()]),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(10),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              mainAxisSize: MainAxisSize.max,
              children: [
                if (!request.accepted!)
                  const Text(
                    "Your Certificate request is currently not accepted by Institute, sit back and relax we have informed them.",
                    textAlign: TextAlign.justify,
                    style: TextStyle(fontSize: 11),
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
                      fontWeight: FontWeight.bold, fontSize: 13),
                )
              ],
            ),
          )
        ],
      ),
    );
  }
}
