// import 'package:Huddle/models/profile.dart';
// import 'package:Huddle/server/getChats.dart';
// import 'package:Huddle/server/getLocation.dart';
// import 'package:Huddle/server/getNear.dart';
// import "package:graphql/client.dart";

// String token = "";
// MyProfile profile = new MyProfile();

// Future<bool> login(String username, String password) async {
//   HttpLink _httpLink = HttpLink(
//     'https://huddle-backend.herokuapp.com/graphql/',
//   );

//   AuthLink _authLink = AuthLink(
//     getToken: () async => 'JWT $token',
//   );

//   Link _link = _authLink.concat(_httpLink);
//   GraphQLClient client = GraphQLClient(
//     /// **NOTE** The default store is the InMemoryStore, which does NOT persist to disk
//     cache: GraphQLCache(),
//     link: _link,
//   );

//   String mutationString = """
//   mutation{
//   tokenAuth(username:"$username",password:"$password"){
//     token
   
//   }
// }
// """;

//   MutationOptions options = MutationOptions(
//     document: gql(mutationString),
//   );

//   QueryResult data = await client.mutate(options);
//   if (data.hasException) {
//     print(data.exception.toString());
//     return false;
//   }
//   token = data.data["tokenAuth"]["token"];
//   await getLocation();
//   await getProfile();
//   await getChats();
//   await getNearMe();
//   return true;
// }

// Future<bool> register(String username, String email, String password,
//     String name, String gender, String city, String state) async {
//   HttpLink _httpLink = HttpLink(
//     'https://huddle-backend.herokuapp.com/graphql/',
//   );

//   AuthLink _authLink = AuthLink(
//     getToken: () async => 'JWT $token',
//   );

//   Link _link = _authLink.concat(_httpLink);
//   GraphQLClient client = GraphQLClient(
//     /// **NOTE** The default store is the InMemoryStore, which does NOT persist to disk
//     cache: GraphQLCache(),
//     link: _link,
//   );

//   String mutationString = """
//    mutation{
//   createUser(username:"$username",password:"$password",email:"$email",name:"$name",city:"$city",state:"$state",gender:"$gender"){
//     __typename
//   }
// }
// """;

//   MutationOptions options = MutationOptions(
//     document: gql(mutationString),
//   );

//   QueryResult data = await client.mutate(options);
//   if (data.hasException) {
//     print(data.exception.toString());
//     return false;
//   }
//   if (await login(username, password)) {
//     return true;
//   }
//   return false;
// }

// Future<bool> getProfile() async {
//   HttpLink _httpLink = HttpLink(
//     'https://huddle-backend.herokuapp.com/graphql/',
//   );

//   AuthLink _authLink = AuthLink(
//     getToken: () async => 'JWT $token',
//   );

//   Link _link = _authLink.concat(_httpLink);
//   GraphQLClient client = GraphQLClient(
//     /// **NOTE** The default store is the InMemoryStore, which does NOT persist to disk
//     cache: GraphQLCache(),
//     link: _link,
//   );

//   String queryString = """
  
// {
//   me{
//     user{
//       email
//     }
//     city
//     name
//     gender
//     city
//     state
//     country
//     id
//     image
//   }
// }
// """;

//   QueryOptions options = QueryOptions(
//     document: gql(queryString),
//   );

//   QueryResult data = await client.query(options);
//   if (data.hasException) {
//     print(data.exception.toString());
//     return false;
//   }
//   var profiledata = data.data;
//   profile.name.value = profiledata["me"]["name"];
//   profile.email.value = profiledata["me"]["user"]["email"];
//   profile.city.value = profiledata["me"]["city"];
//   profile.isFemale.value = (profiledata["me"]["gender"] == "F") ? true : false;
//   profile.state.value = profiledata["me"]["state"];
//   profile.country.value = profiledata["me"]["country"];
//   profile.id.value = profiledata["me"]["id"];
//   profile.image.value = profiledata["me"]["image"];
//   return true;
// }