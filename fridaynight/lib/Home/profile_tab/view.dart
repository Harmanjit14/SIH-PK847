import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
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
        const SizedBox(
          height: 30,
        ),
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
        Padding(
          padding: const EdgeInsets.all(20.0),
          child: Table(
            border: TableBorder.all(width: 1.5),
            children: [
              TableRow(children: [
                const Padding(
                  padding: EdgeInsets.all(10),
                  child: Text(
                    "Student Name ",
                    style: TextStyle(
                      fontSize: 20,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(10),
                  child: Text(
                    "${student.firstName} ${student.lastName}",
                    style: const TextStyle(fontSize: 20),
                  ),
                )
              ]),
              TableRow(children: [
                const Padding(
                  padding: EdgeInsets.all(10),
                  child: Text(
                    "Student Email ",
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(10),
                  child: Text(
                    "${student.email}",
                    style: const TextStyle(fontSize: 20),
                  ),
                ),
              ]),
              TableRow(children: [
                const Padding(
                  padding: EdgeInsets.all(10),
                  child: Text(
                    "Registeration No. ",
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(10),
                  child: Text(
                    "${student.roll}",
                    style: const TextStyle(fontSize: 20),
                  ),
                ),
              ]),
              TableRow(children: [
                const Padding(
                  padding: EdgeInsets.all(10),
                  child: Text(
                    "Student Degree ",
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(10),
                  child: Text(
                    "${student.degree}",
                    style: const TextStyle(fontSize: 20),
                  ),
                ),
              ]),
              TableRow(children: [
                const Padding(
                  padding: EdgeInsets.all(10),
                  child: Text(
                    "Current Semester ",
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(10),
                  child: Text(
                    "${student.currentSem}",
                    style: const TextStyle(fontSize: 20),
                  ),
                ),
              ]),
              TableRow(children: [
                const Padding(
                  padding: EdgeInsets.all(10),
                  child: Text(
                    "Batch ",
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Padding(
                  padding:const  EdgeInsets.all( 10),
                  child: Text(
                    "${student.batch}",
                    style: const TextStyle(fontSize: 20),
                  ),
                ),
              ]),
              TableRow(children: [
                const Padding(
                  padding: EdgeInsets.all(10),
                  child: Text(
                    "Graduation Year ",
                    style: TextStyle(fontSize: 20),
                  ),
                ),
                Padding(
                  padding: const  EdgeInsets.all( 10),
                  child: Text(
                    "${student.graduatingYear}",
                    style: const TextStyle(fontSize: 20),
                  ),
                ),
              ]),
            ],
          ),
        )
      ],
    );
  }
}
