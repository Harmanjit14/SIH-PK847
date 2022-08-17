import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:fridaynight/Auth/query.dart';

class ProfileTab extends StatefulWidget {
  const ProfileTab({Key? key}) : super(key: key);

  @override
  State<ProfileTab> createState() => _ProfileTabState();
}

class _ProfileTabState extends State<ProfileTab> {
  @override
  Widget build(BuildContext context) {
    return ListView(
      shrinkWrap: true,
      children: [
        Column(
          mainAxisAlignment: MainAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            SizedBox(
                height: MediaQuery.of(context).size.height / 10,
                child: Image.network(institute.instituteLogo!)),
            const SizedBox(
              height: 10,
            ),
            Text(
              institute.instituteName!,
              style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
          ],
        ),
        Table(
          border: TableBorder.all(),
          children: [
            TableRow(children: [
              const Padding(
                padding: EdgeInsets.only(left: 15),
                child: Text(
                  "Student Name ",
                  style: TextStyle(
                    fontSize: 20,
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsets.only(left: 15),
                child: Text(
                  "${student.firstName} ${student.lastName}",
                  style: TextStyle(fontSize: 20),
                ),
              )
            ]),
            TableRow(children: [
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: const Text(
                  "Student Email ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: Text(
                  "${student.email}",
                  style: const TextStyle(fontSize: 20),
                ),
              ),
            ]),
            TableRow(children: [
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: const Text(
                  "Registeration No. ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: Text(
                  "${student.roll}",
                  style: const TextStyle(fontSize: 20),
                ),
              ),
            ]),
            TableRow(children: [
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: const Text(
                  "Student Degree ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: Text(
                  "${student.degree}",
                  style: const TextStyle(fontSize: 20),
                ),
              ),
            ]),
            TableRow(children: [
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: const Text(
                  "Current Semester ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: Text(
                  "${student.currentSem}",
                  style: const TextStyle(fontSize: 20),
                ),
              ),
            ]),
            TableRow(children: [
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: const Text(
                  "Batch ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: Text(
                  "${student.batch}",
                  style: const TextStyle(fontSize: 20),
                ),
              ),
            ]),
            TableRow(children: [
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: const Text(
                  "Graduation Year ",
                  style: TextStyle(fontSize: 20),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(left: 15),
                child: Text(
                  "${student.graduatingYear}",
                  style: const TextStyle(fontSize: 20),
                ),
              ),
            ]),
          ],
        )
      ],
    );
  }
}
