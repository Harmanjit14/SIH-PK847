import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
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
          itemCount: 6,
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
            return GestureDetector(
              onTap: () {},
              child: Container(
                decoration: BoxDecoration(
                    boxShadow: const [
                      BoxShadow(blurRadius: 2, color: Colors.black),
                    ],
                    color: light.primaryContainer,
                    borderRadius: BorderRadius.circular(20)),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    Align(
                      alignment: Alignment.topLeft,
                      child: MaterialButton(
                        elevation: 2,
                        color: light.background,
                        // shape: const CircleBorder(),
                        onPressed: () {},
                        child: Icon(
                          Icons.close,
                          color: light.primary,
                        ),
                      ),
                    ),
                    Text("Certificate Type: ")
                  ],
                ),
              ),
            );
          },
        ),
      ],
    );
  }
}
