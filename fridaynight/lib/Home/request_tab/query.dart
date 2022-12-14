import 'package:flutter/material.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/Home/request_tab/model.dart';
import 'package:fridaynight/server_data.dart';
import 'package:graphql/client.dart';

Future<List<CertificateRequest>> getStudentRequest() async {
  List<CertificateRequest>? requestList = [];

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
  studentRequests{
    id
    paymentAmount
    paymentStatus
    deliveryStatus
    verified
    deliveryDone
    certificateStatus
  }
}
""";

  QueryOptions options = QueryOptions(
    document: gql(queryString),
    fetchPolicy: FetchPolicy.cacheFirst
  );

  QueryResult data = await client.query(options);
  if (data.hasException) {
    debugPrint(data.exception.toString());
    return [];
  }

  // Student Request Data
  List requestDataList = data.data!['studentRequests'];
  debugPrint(requestDataList.toString());
  debugPrint(requestDataList.length.toString());
  for (var i = 0; i < requestDataList.length; i++) {
    var dataMap = requestDataList[i];
    var obj = CertificateRequest();
    obj.fromJson(dataMap);
    requestList.add(obj);
  }

  return requestList;
}
