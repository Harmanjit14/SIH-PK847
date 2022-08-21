import 'package:flutter/material.dart';
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


Future<bool> registerEvent() async {

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

  String mutationString = """ 
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

}
