import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/Home/home_tab/model.dart';
import 'package:fridaynight/server_data.dart';
import 'package:graphql/client.dart';

Future<Map<String, List<dynamic>>> getInstituteEvents() async {
  List<InstituteEvent> list = [];
  List<StudentParticipation> list2 = [];

  Map<String, List<dynamic>> map = {
    "instituteEvent": list,
    "studentParticipation": list2,
  };
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

  String queryString = """ 
{
  getAllInstituteEvents{
    id
    eventName
    startDate
    endDate
    eventOverview
    eventDescription
    hostName
    hostContact
  }

  studentParticipation{
    id
    event{
      id
      eventName
    }
  }
}
""";

  QueryOptions options = QueryOptions(
    document: gql(queryString),
    fetchPolicy: FetchPolicy.cacheFirst,
  );

  QueryResult data = await client.query(options);
  if (data.hasException) {
    debugPrint(data.exception.toString());
    return map;
  }

  // Student Request Data
  List eventList = data.data!['getAllInstituteEvents'];
  for (var i = 0; i < eventList.length; i++) {
    var dataMap = eventList[i];
    var obj = InstituteEvent();
    obj.fromJson(dataMap);
    list.add(obj);
  }

  List partList = data.data!['studentParticipation'];
  for (var i = 0; i < partList.length; i++) {
    var dataMap = partList[i];
    var obj = StudentParticipation();
    obj.fromJson(dataMap);
    list2.add(obj);
  }

  map['studentParticipation'] = list2;
  map['instituteEvent'] = list;

  return map;
}

Future<bool> registerEvent(String eventId) async {
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
debugPrint(eventId);
  String mutationString = """ 
mutation{
  registerParticipant(id:"${eventId}"){
    __typename
  }
}
""";

  MutationOptions options = MutationOptions(
    document: gql(mutationString),
  );

  QueryResult data = await client.mutate(options);

  if (data.hasException) {
    debugPrint(data.exception.toString());
    await Fluttertoast.showToast(
      msg: "Failed to Register, Please try after sometime!", // message
      toastLength: Toast.LENGTH_SHORT, // length
      gravity: ToastGravity.BOTTOM, // placemnent
    );
    return false;
  }
  await Fluttertoast.showToast(
    msg: "Registeration Successful", // message
    toastLength: Toast.LENGTH_SHORT, // length
    gravity: ToastGravity.BOTTOM, // placemnent
  );

  return true;
}
