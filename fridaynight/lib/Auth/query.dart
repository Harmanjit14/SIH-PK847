import 'package:flutter/material.dart';
import 'package:fridaynight/Auth/model.dart';
import 'package:fridaynight/degree_data.dart';
import 'package:fridaynight/server_data.dart';
import "package:graphql/client.dart";

String token = "";
Student student = Student();
Institute institute = Institute();

Future<bool> login(String username, String password) async {
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
  mutation{
  tokenAuth(username:"$username",password:"$password"){
    token
   
  }
}
""";

  MutationOptions options = MutationOptions(
    document: gql(mutationString),
  );

  QueryResult data = await client.mutate(options);

  if (data.hasException) {
    debugPrint(data.exception.toString());
    return false;
  }
  token = data.data!["tokenAuth"]["token"];

  bool studentStatus = await getStudent();

  return studentStatus;
}

Future<bool> getStudent() async {
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
  studentLogin{
    id
    firstName
    lastName
    email
    roll
    institute{
      name
      logo
      mail
      contact
    }
    mobile
    dob
    degree
    address
    batch
    fatherName
    motherName
    graduatingYear
    wallet
  }
}
""";

  QueryOptions options = QueryOptions(
    document: gql(queryString),
  );

  QueryResult data = await client.query(options);
  if (data.hasException) {
    debugPrint(data.exception.toString());
    return false;
  }

  // Student Profile
  var studentData = data.data!['studentLogin'];
  debugPrint(studentData.toString());
  student.uid = studentData['id'];
  student.firstName = studentData['firstName'];
  student.lastName = studentData['lastName'];
  student.address = studentData['address'];
  student.email = studentData['email'];
  student.mobile = studentData['mobile'];
  student.dob = studentData['dob'];
  String deg = studentData['degree'].toString();
  int degIndex = int.parse(deg[deg.length - 1]);
  student.degree = degreeList[degIndex];
  student.batch = studentData['batch'];
  student.fatherName = studentData['fatherName'];
  student.motherName = studentData['motherName'];
  student.graduatingYear = studentData['graduatingYear'];
  student.wallet = studentData['wallet'];
  student.roll = studentData['roll'];
  student.currentSem = studentData['currentSem'];

  // Institute Data
  var instituteData = data.data!['studentLogin']['institute'];
  debugPrint(instituteData.toString());
  institute.instituteContact = instituteData['contact'];
  institute.instituteLogo = instituteData['logo'];
  institute.instituteName = instituteData['name'];
  institute.instituteMail = instituteData['mail'];
  return true;
}
