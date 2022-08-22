import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/server_data.dart';
import 'package:graphql/client.dart';

ColorScheme light = const ColorScheme.light();

const razorpaySecret = "eg4DJ2rVwUw7VQNP4D1u2JcZ";
const razorpayKey = "rzp_test_cJu9VokepiK9cp";

Future<bool> requestCertificate(String certificateId, bool hardcopy,
    {int? semesterNo, String? eventId}) async {
  HttpLink httpLink = HttpLink(
    url,
  );

  AuthLink authLink = AuthLink(
    getToken: () async => 'JWT $token',
  );

  Link link = authLink.concat(httpLink);
  GraphQLClient client = GraphQLClient(
    cache: GraphQLCache(),
    link: link,
  );
  String mutationString = "";
  if (certificateId == "0" && semesterNo != null) {
    mutationString = """
  mutation{
  certificateRequest(certificate:"0",hardcopy =$hardcopy ,semester:$semesterNo){
    __typename
  }
}
""";
  } else if (certificateId == "1") {
    mutationString = """
  mutation{
  certificateRequest(certificate:"1",hardcopy: $hardcopy){
    __typename
  }
}
""";
  } else if (certificateId == "4") {
    mutationString = """
  mutation{
  certificateRequest(certificate:"4",hardcopy: $hardcopy){
    __typename
  }
}
""";
  } else if (certificateId == "5") {
    mutationString = """
  mutation{
  certificateRequest(certificate:"5",hardcopy: $hardcopy,eventId:"${eventId}" ){
    __typename
  }
}
""";
  } else {
    await Fluttertoast.showToast(
      msg: "Unable to create new Certificate Request",
      toastLength: Toast.LENGTH_SHORT,
      gravity: ToastGravity.BOTTOM,
    );
    return false;
  }

  MutationOptions options = MutationOptions(
    document: gql(mutationString),
  );

  QueryResult data = await client.mutate(options);

  if (data.hasException) {
    debugPrint(data.exception.toString());
    await Fluttertoast.showToast(
      msg: "Unable to create new Certificate Request",
      toastLength: Toast.LENGTH_SHORT,
      gravity: ToastGravity.BOTTOM,
    );
    return false;
  }

  await Fluttertoast.showToast(
    msg: "Certificate Request Sent Successfully",
    toastLength: Toast.LENGTH_SHORT,
    gravity: ToastGravity.BOTTOM,
  );
  return true;
}

Future<int> showSemesterSectionPopup(BuildContext context) async {
  List<int> list = List.generate(student.currentSem!, ((index) => index));
  int selectedIndex = -1;
  await showDialog<void>(
    context: context,
    barrierDismissible: true, // user must tap button!
    builder: (BuildContext context) {
      return AlertDialog(
        title: const Text("Select your Semester"),
        content: SingleChildScrollView(
          child: ListBody(
            children: <Widget>[
              DropdownButton<int>(
                borderRadius: BorderRadius.circular(20),
                value: 0,
                icon: Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    Icon(
                      Icons.arrow_downward,
                      color: light.primary,
                      size: 15,
                    ),
                  ],
                ),
                elevation: 16,
                style: TextStyle(color: light.primary),
                underline: Container(
                  height: 2,
                  color: light.primary,
                ),
                onChanged: (int? newValue) {
                  selectedIndex = newValue ?? 0 + 1;
                  Navigator.pop(context);
                },
                items: list.map<DropdownMenuItem<int>>((int value) {
                  return DropdownMenuItem<int>(
                    value: value,
                    child: Text("Semester ${value + 1}"),
                  );
                }).toList(),
              ),
            ],
          ),
        ),
      );
    },
  );
  return selectedIndex;
}
