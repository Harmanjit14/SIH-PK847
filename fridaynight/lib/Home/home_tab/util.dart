import 'package:flutter/material.dart';
import 'package:fridaynight/Home/home_tab/model.dart';

class StatusCard extends StatelessWidget {
  final certiCheck check;
  const StatusCard({Key? key, required this.check}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
        margin: const EdgeInsets.fromLTRB(16.0, 16.0, 16.0, 0),
        child: Padding(
          padding: const EdgeInsets.all(12.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              Text(
                check.certi,
                style: TextStyle(
                  fontSize: 18.0,
                  color: Colors.grey[800],
                ),
              ),
              const SizedBox(height: 6.0),
              Text(
                check.status,
                style: TextStyle(
                  fontSize: 14.0,
                  color: Colors.grey[600],
                ),
              ),
            ],
          ),
        ));
  }
}
