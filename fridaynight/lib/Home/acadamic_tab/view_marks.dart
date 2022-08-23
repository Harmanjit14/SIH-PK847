import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:fridaynight/Home/acadamic_tab/model.dart';
import 'package:fridaynight/Home/acadamic_tab/query.dart';
import 'package:fridaynight/utils.dart';

class MarksView extends StatefulWidget {
  final int sem;
  const MarksView(this.sem, {Key? key}) : super(key: key);

  @override
  State<MarksView> createState() => _MarksViewState();
}

class _MarksViewState extends State<MarksView> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: FutureBuilder<List<Subjects>?>(
          future: getMarks(widget.sem),
          builder: ((context, snapshot) {
            switch (snapshot.connectionState) {
              case ConnectionState.waiting:
                return Center(
                  child: SpinKitWave(
                    color: light.primary.withOpacity(0.4),
                  ),
                );
              default:
                if (snapshot.hasError) {
                  return Center(
                      child: Center(child: Text('Error: ${snapshot.error}')));
                } else {
                  List<Subjects>? requestList = snapshot.data;
                  if (requestList!.isEmpty) {
                    return const Center(
                      child: Text("No subjects added by your Institute."),
                    );
                  }

                  return ListView(
                    shrinkWrap: true,
                    children: [
                      Padding(
                        padding: const EdgeInsets.fromLTRB(20, 20, 20, 10),
                        child: Text(
                          "Subjects for Semester ${widget.sem + 1}",
                          textAlign: TextAlign.left,
                          style: const TextStyle(
                              fontSize: 20,
                              color: Colors.black,
                              fontWeight: FontWeight.bold,
                              shadows: [
                                Shadow(color: Colors.black, blurRadius: 2)
                              ]),
                        ),
                      ),
                      Padding(
                        padding: const EdgeInsets.all(20.0),
                        child: Table(
                          border: TableBorder.all(width: 1.5),
                          children: [
                            const TableRow(children: [
                              Padding(
                                padding: EdgeInsets.all(10),
                                child: Text(
                                  "Subject",
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                              Padding(
                                padding: EdgeInsets.all(10),
                                child: Text(
                                  "Subject Code",
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                              Padding(
                                padding: EdgeInsets.all(10),
                                child: Text(
                                  "Credits",
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                              Padding(
                                padding: EdgeInsets.all(10),
                                child: Text(
                                  "Marks Secured /100",
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                              Padding(
                                padding: EdgeInsets.all(10),
                                child: Text(
                                  "Grade Secured",
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                            ]),
                            ...List.generate(requestList.length, (index) {
                              return TableRow(children: [
                                Padding(
                                  padding: const EdgeInsets.all(10),
                                  child: Text(requestList[index].name ?? ""),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(10),
                                  child: Text(requestList[index].code ?? ""),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(10),
                                  child: Text(
                                      requestList[index].credits.toString()),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(10),
                                  child: Text(
                                      requestList[index].marks.toString()),
                                ),
                                Padding(
                                  padding: const EdgeInsets.all(10),
                                  child: Text(
                                      requestList[index].grade.toString()),
                                ),
                              ]);
                            }),
                          ],
                        ),
                      ),
                    ],
                  );
                }
            }
          }),
        ),
      ),
    );
  }
}
