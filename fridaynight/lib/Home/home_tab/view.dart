import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/Home/home_tab/model.dart';
import 'package:fridaynight/Home/home_tab/query.dart';
import 'package:fridaynight/utils.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return FutureBuilder<Map<String, List<dynamic>>>(
      future: getInstituteEvents(),
      builder: ((context, snapshot) {
        switch (snapshot.connectionState) {
          case ConnectionState.waiting:
            return Center(
                child: SpinKitWave(
              color: light.primary.withOpacity(0.4),
            ));
          default:
            if (snapshot.hasError) {
              return Center(child: Text('Error: ${snapshot.error}'));
            } else {
              List<InstituteEvent>? list =
                  snapshot.data!['instituteEvent']!.cast<InstituteEvent>();
              List<StudentParticipation>? list2 = snapshot
                  .data!['studentParticipation']!
                  .cast<StudentParticipation>();
              if (list.isEmpty && list2.isEmpty) {
                return const Center(
                  child: Text("Error getting data"),
                );
              }

              return Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                mainAxisSize: MainAxisSize.max,
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  if (list.isNotEmpty)
                    const Padding(
                      padding: EdgeInsets.all(20),
                      child: Text(
                        "Exciting Events",
                        style: TextStyle(
                            fontSize: 30,
                            color: Colors.black,
                            fontWeight: FontWeight.bold,
                            shadows: [
                              Shadow(color: Colors.black, blurRadius: 2)
                            ]),
                      ),
                    ),
                  if (list.isNotEmpty)
                    SizedBox(
                      height: MediaQuery.of(context).size.height / 5,
                      width: MediaQuery.of(context).size.width,
                      child: ListView.builder(
                        padding: const EdgeInsets.all(10),
                        shrinkWrap: true,
                        scrollDirection: Axis.horizontal,
                        itemCount: list.length,
                        itemBuilder: ((context, index) {
                          return eventCard(list[index]);
                        }),
                      ),
                    ),
                  if (list2.isNotEmpty)
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const SizedBox(
                            height: 20,
                          ),
                          const Padding(
                            padding: EdgeInsets.all(20),
                            child: Text(
                              "My Participations",
                              textAlign: TextAlign.left,
                              style: TextStyle(
                                  fontSize: 30,
                                  color: Colors.black,
                                  fontWeight: FontWeight.bold,
                                  shadows: [
                                    Shadow(color: Colors.black, blurRadius: 2)
                                  ]),
                            ),
                          ),
                          Expanded(
                            child: ListView.builder(
                              padding: const EdgeInsets.all(10),
                              shrinkWrap: true,
                              itemCount: list2.length,
                              itemBuilder: ((context, index) {
                                return participationContainer(list2[index]);
                              }),
                            ),
                          ),
                        ],
                      ),
                    ),
                ],
              );
            }
        }
      }),
    );
  }

  Widget participationContainer(StudentParticipation obj) {
    Future<void> _showCertificateRequestDialog() async {
      return showDialog<void>(
        context: context,
        barrierDismissible: true, // user must tap button!
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text(obj.eventName ?? ""),
            content: SingleChildScrollView(
              child: ListBody(
                children: const <Widget>[
                  Text(
                      'Do you want to request certificate for your participation? Please select from below options, If hardcopy selected you will be charged Rs. 30 for safe delivery from your student wallet.'),
                ],
              ),
            ),
            actions: <Widget>[
              MaterialButton(
                shape: const StadiumBorder(),
                elevation: 0,
                color: light.primary,
                onPressed: () {
                  requestCertificate("5", false, eventId: obj.eventId);
                  Navigator.pop(context);
                },
                child: Text(
                  'E-Certificate',
                  style: TextStyle(color: light.background),
                ),
              ),
              MaterialButton(
                shape: const StadiumBorder(),
                elevation: 0,
                color: light.primary,
                onPressed: () async {
                  if (student.wallet! < 30) {
                    await Fluttertoast.showToast(
                        toastLength: Toast.LENGTH_SHORT,
                        gravity: ToastGravity.BOTTOM,
                        msg:
                            "Maintain minimum balance of Rs. 30 in your studdent wallet to proceed.");
                    return;
                  }

                  requestCertificate("5", false, eventId: obj.eventId);
                  Navigator.pop(context);
                },
                child: Text(
                  'Hardcopy',
                  style: TextStyle(color: light.background),
                ),
              ),
            ],
          );
        },
      );
    }

    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        color: light.background,
        boxShadow: [
          BoxShadow(blurRadius: 3, spreadRadius: -1, color: light.shadow)
        ],
      ),
      height: 70,
      width: MediaQuery.of(context).size.width,
      child: Row(
        mainAxisSize: MainAxisSize.max,
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(
              child: Row(
            children: [
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.all(15.0),
                  child: Text(
                    obj.eventName ?? "Event Name",
                    style: const TextStyle(
                        shadows: [Shadow()],
                        fontSize: 18,
                        fontWeight: FontWeight.bold),
                    maxLines: 3,
                  ),
                ),
              ),
            ],
          )),
          MaterialButton(
            padding: const EdgeInsets.all(0),
            minWidth: 70,
            height: double.maxFinite,
            onPressed: () {
              _showCertificateRequestDialog();
            },
            child: Container(
              height: double.maxFinite,
              width: 70,
              decoration: BoxDecoration(
                color: light.primary,
                borderRadius: const BorderRadius.only(
                  topRight: Radius.circular(20),
                  bottomRight: Radius.circular(20),
                ),
              ),
              child: Icon(
                Icons.description,
                color: light.background,
                size: 30,
              ),
            ),
          ),
        ],
      ),
    );
  }

  String getMonth(int month) {
    switch (month) {
      case 1:
        return "JAN";
      case 2:
        return "FEB";
      case 3:
        return "MAR";
      case 4:
        return "APR";
      case 5:
        return "MAY";
      case 6:
        return "JUN";
      case 7:
        return "JUL";
      case 8:
        return "AUG";
      case 9:
        return "SEP";
      case 10:
        return "OCT";
      case 11:
        return "NOV";
      case 12:
        return "DEC";
      default:
        return "JAN";
    }
  }

  Widget eventCard(InstituteEvent event) {
    String day = event.startDate!.split("/")[0];
    String month = getMonth(int.parse(event.startDate!.split("/")[1]));
    String year = event.startDate!.split("/")[2];

    Future<void> _showEventParticipationDialog() async {
      return showDialog<void>(
        context: context,
        barrierDismissible: true, // user must tap button!
        builder: (BuildContext context) {
          return AlertDialog(
            title: Text(event.eventName ?? ""),
            content: SingleChildScrollView(
              child: ListBody(
                children: <Widget>[
                  Text('Overview- ${event.overview}'),
                  Text('Decription- ${event.description}'),
                  Text('Dates- ${event.startDate}-${event.startDate}'),
                ],
              ),
            ),
            actions: <Widget>[
              MaterialButton(
                shape: const StadiumBorder(),
                elevation: 0,
                color: Colors.green,
                onPressed: () {
                  registerEvent(event.id ?? "");
                  Navigator.pop(context);
                },
                child: Text(
                  'Register',
                  style: TextStyle(color: light.background),
                ),
              ),
              MaterialButton(
                shape: const StadiumBorder(),
                elevation: 0,
                color: Colors.red,
                onPressed: () {
                  Navigator.pop(context);
                },
                child: Text(
                  'No',
                  style: TextStyle(color: light.background),
                ),
              ),
            ],
          );
        },
      );
    }

    return Container(
      margin: const EdgeInsets.only(right: 15),
      width: MediaQuery.of(context).size.width * 0.8,
      decoration: BoxDecoration(boxShadow: [
        BoxShadow(blurRadius: 3, spreadRadius: -1, color: light.shadow),
      ], color: light.background, borderRadius: BorderRadius.circular(20)),
      child: MaterialButton(
        onPressed: _showEventParticipationDialog,
        padding: const EdgeInsets.all(0),
        child: Row(
          mainAxisSize: MainAxisSize.max,
          children: [
            Container(
              width: MediaQuery.of(context).size.width * 0.3,
              decoration: BoxDecoration(
                color: light.primary,
                borderRadius: const BorderRadius.only(
                  topLeft: Radius.circular(20),
                  bottomLeft: Radius.circular(20),
                ),
              ),
              child: Center(
                  child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  SizedBox(
                    height: 65,
                    child: Text(
                      day,
                      style: TextStyle(
                        fontWeight: FontWeight.w900,
                        letterSpacing: 0,
                        shadows: const [
                          Shadow(
                            color: Colors.black,
                            blurRadius: 2,
                          )
                        ],
                        fontSize: 60,
                        color: light.background,
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 33,
                    child: Text(
                      month,
                      style: TextStyle(
                          shadows: const [
                            Shadow(
                              color: Colors.black,
                              blurRadius: 2,
                            )
                          ],
                          fontSize: 30,
                          letterSpacing: 3,
                          fontWeight: FontWeight.w900,
                          color: light.background),
                    ),
                  ),
                  Text(
                    year,
                    style: TextStyle(
                        fontSize: 17,
                        letterSpacing: 8,
                        color: light.background),
                  ),
                ],
              )),
            ),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.all(10.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.max,
                  children: [
                    Text(
                      event.eventName ?? "",
                      style: const TextStyle(
                          shadows: [Shadow()],
                          fontSize: 18,
                          fontWeight: FontWeight.bold),
                      maxLines: 3,
                    ),
                    Text(
                      "Hosted By- ${event.hostName}",
                      style: TextStyle(
                          color: Colors.grey[600],
                          fontSize: 10,
                          fontWeight: FontWeight.normal),
                      maxLines: 3,
                    ),
                    const SizedBox(
                      height: 10,
                    ),
                    Text(
                      "About- ${event.overview}",
                      style: TextStyle(
                          color: Colors.grey[800],
                          fontSize: 12,
                          fontWeight: FontWeight.normal),
                      maxLines: 3,
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
