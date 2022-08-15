import 'package:flutter/material.dart';
import 'quote.dart';
import 'quote_card.dart';

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
    return Scaffold(
      backgroundColor: Colors.grey[200],
      appBar: AppBar(
        title: Text('Home Page'),
        centerTitle: true,
        backgroundColor: Colors.purple[600],
      ),
      body: Column(
        children: checkpoints.map((check) => StatusCard(check: check)).toList(),
      ),
    );
  }
}
