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
      padding: const EdgeInsets.fromLTRB(20, 20, 20, 20),
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
        const SizedBox(
              height: 40,
            ),
        Text(
          "Student Name: ${student.firstName} ${student.lastName}",
          style: const TextStyle(fontSize: 20),
        ),
        Text(
          "Student Email: ${student.email}",
          style: const TextStyle(fontSize: 20),
        ),
        Text(
          "Registeration Number: ${student.roll}",
          style: const TextStyle(fontSize: 20),
        ),
        Text(
          "Student Degree: ${student.degree}",
          style: const TextStyle(fontSize: 20),
        ),
        Text(
          "Current Semester: ${student.currentSem}",
          style: const TextStyle(fontSize: 20),
        ),
        Text(
          "Alloted Batch: ${student.batch}",
          style: const TextStyle(fontSize: 20),
        ),
        Text(
          "Graduating Year: ${student.graduatingYear}",
          style: const TextStyle(fontSize: 20),
        ),
      ],
    );
  }
}
