import 'package:flutter/material.dart';
import 'util.dart';
import 'model.dart';

void main() => runApp(MaterialApp(home: HomePage()));

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<certiCheck> checkpoints = [
    certiCheck(certi: 'Migration Certificate', status: 'Pending'),
    certiCheck(certi: 'Affidavit', status: 'Granted'),
    certiCheck(certi: 'Domicile Certificate', status: 'Pending'),
    certiCheck(certi: 'Migration Certificate', status: 'Pending'),
    certiCheck(certi: 'Affidavit', status: 'Granted'),
    certiCheck(certi: 'Domicile Certificate', status: 'Pending')
  ];

  @override
  Widget build(BuildContext context) {
    return Column(
      children: checkpoints.map((check) => StatusCard(check: check)).toList(),
    );
  }
}
