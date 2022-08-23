import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/Home/acadamic_tab/model.dart';
import 'package:fridaynight/server_data.dart';
import 'package:graphql/client.dart';

Future<List<Subjects>> getSubjects(int semester) async {
  semester += 1;
  List<Subjects> list = [];
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
  getAllSemSubjects(sem:$semester,graduatingYear:${student.graduatingYear},degree:"${student.degreeIndex}"){
    subject
    subjectCode
    credits
  }
}
""";
  debugPrint(queryString);
  QueryOptions options = QueryOptions(
    document: gql(queryString),
    fetchPolicy: FetchPolicy.cacheFirst,
  );

  QueryResult data = await client.query(options);
  if (data.hasException) {
    debugPrint(data.exception.toString());
    return list;
  }

  // Student Request Data
  List dataList = data.data!['getAllSemSubjects'];
  debugPrint(dataList.toString());
  for (var i = 0; i < dataList.length; i++) {
    var dataMap = dataList[i];
    var obj = Subjects();
    obj.fromJson(dataMap);
    list.add(obj);
  }

  return list;
}


Future<List<Subjects>> getMarks(int semester) async {
  semester += 1;
  List<Subjects> list = [];
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
  getAllSemGradesForStudents(sem:$semester){
    subject
    subjectCode
    credits
    marks
    grade
    id
  }
}
""";
  debugPrint(queryString);
  QueryOptions options = QueryOptions(
    document: gql(queryString),
    fetchPolicy: FetchPolicy.cacheFirst,
  );

  QueryResult data = await client.query(options);
  if (data.hasException) {
    debugPrint(data.exception.toString());
    return list;
  }

  // Student Request Data
  List dataList = data.data!['getAllSemGradesForStudents'];
  debugPrint(dataList.toString());
  for (var i = 0; i < dataList.length; i++) {
    var dataMap = dataList[i];
    var obj = Subjects();
    obj.fromJson(dataMap);
    list.add(obj);
  }

  return list;
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
