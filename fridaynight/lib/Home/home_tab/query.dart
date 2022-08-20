import 'package:flutter/material.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/Home/home_tab/model.dart';
import 'package:fridaynight/server_data.dart';
import 'package:graphql/client.dart';

Future<List<InstituteEvent>> getInstituteEvents() async {
  List<InstituteEvent> list = [];
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
}
""";

  QueryOptions options = QueryOptions(
    document: gql(queryString),
    fetchPolicy: FetchPolicy.cacheFirst,
  );

  QueryResult data = await client.query(options);
  if (data.hasException) {
    debugPrint(data.exception.toString());
    return [];
  }

  // Student Request Data
  List eventList = data.data!['getAllInstituteEvents'];
  for (var i = 0; i < eventList.length; i++) {
    var dataMap = eventList[i];
    var obj = InstituteEvent();
    obj.fromJson(dataMap);
    list.add(obj);
  }

  return list;
}
