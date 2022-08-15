import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:get/get.dart';

class ButtonLogin extends GetxController {
  RxInt buttonState = 0.obs;
}

class LoginSreen extends StatefulWidget {
  const LoginSreen({Key? key}) : super(key: key);

  @override
  _LoginSreenState createState() => _LoginSreenState();
}

class _LoginSreenState extends State<LoginSreen> {
  final TextEditingController usernameController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  late String username, password;
  bool sError = false;
  bool nError = false;

  final btnState = Get.put(ButtonLogin());
  @override
  void initState() {
    usernameController.addListener(() {
      username = usernameController.text;
    });
    passwordController.addListener(() {
      password = passwordController.text;
    });
    super.initState();
  }

  @override
  void dispose() {
    usernameController.dispose();
    passwordController.dispose();
    super.dispose();
  }

  Widget logChild() {
    switch (btnState.buttonState.value) {
      case 0:
        {
          return const Text(
            "Continue",
            style: TextStyle(
                color: Colors.black, fontSize: 20, fontWeight: FontWeight.bold),
          );
        }
      case 1:
        {
          return SpinKitDoubleBounce(
            color: Colors.amber[100],
            size: 50.0,
          );
        }
      case 2:
        {
          return Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const [
              Icon(Icons.verified),
              SizedBox(
                width: 7,
              ),
              Text(
                "Success!",
                style: TextStyle(
                    color: Colors.black,
                    fontSize: 20,
                    fontWeight: FontWeight.normal),
              ),
            ],
          );
        }
      case 3:
        {
          return Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const [
              Icon(Icons.error),
              SizedBox(
                width: 7,
              ),
              Text(
                "Check Credentials",
                style: TextStyle(
                    color: Colors.black,
                    fontSize: 20,
                    fontWeight: FontWeight.normal),
              ),
            ],
          );
        }
      default:
        {
          return const Text(
            "Continue",
            style: TextStyle(
                color: Colors.black, fontSize: 20, fontWeight: FontWeight.w700),
          );
        }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
          child: SingleChildScrollView(
        child: Column(
          mainAxisSize: MainAxisSize.max,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Container(
              margin: const EdgeInsets.fromLTRB(20, 10, 20, 0),
              child: const Text(
                "FridayNight-SIH",
                style: TextStyle(
                    color: Colors.black,
                    fontSize: 35,
                    shadows: [
                      Shadow(
                        color: Colors.black,
                        blurRadius: 1,
                      )
                    ],
                    fontWeight: FontWeight.w700),
              ),
            ),
            Container(
              margin: const EdgeInsets.fromLTRB(20, 0, 20, 10),
              child: const Text(
                "Welcome Back",
                style: TextStyle(
                    color: Colors.black,
                    fontSize: 25,
                    fontWeight: FontWeight.w500),
              ),
            ),
            Container(
              margin: const EdgeInsets.fromLTRB(20, 60, 20, 0),
              child: TextField(
                controller: usernameController,
                keyboardType: TextInputType.text,
                decoration: InputDecoration(
                  errorText: (sError) ? "Can't be empty!" : null,
                  labelText: "Username",
                  prefixIcon: const Icon(Icons.account_circle),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(15),
                  ),
                ),
              ),
            ),
            Container(
              margin: const EdgeInsets.fromLTRB(20, 10, 20, 0),
              child: TextField(
                controller: passwordController,
                keyboardType: TextInputType.text,
                obscureText: true,
                obscuringCharacter: "*",
                decoration: InputDecoration(
                  errorText: (nError) ? "Can't be empty" : null,
                  labelText: "Password",
                  prefixIcon: const Icon(Icons.lock),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(15),
                  ),
                ),
              ),
            ),
            Container(
                height: 60,
                margin: const EdgeInsets.fromLTRB(20, 20, 20, 0),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(15),
                  child: Obx(() {
                    return MaterialButton(
                      color: Colors.amber,
                      splashColor: Colors.orange,
                      onPressed: () async {
                        if (username.isBlank! && password.isBlank!) {
                          setState(() {
                            nError = true;
                            sError = true;
                          });
                          Timer(const Duration(seconds: 2), () {
                            setState(() {
                              sError = false;
                              nError = false;
                            });
                          });
                        } else if (username.isBlank!) {
                          setState(() {
                            sError = true;
                          });

                          Timer(const Duration(seconds: 2), () {
                            setState(() {
                              sError = false;
                              nError = false;
                            });
                          });
                        } else if (password.isBlank!) {
                          setState(() {
                            nError = true;
                          });
                          Timer(const Duration(seconds: 2), () {
                            setState(() {
                              sError = false;
                              nError = false;
                            });
                          });
                        } else {
                          btnState.buttonState.value = 3;
                          // if (await login(name, city)) {
                          //   btnState.buttonState.value = 2;
                          //   Timer(Duration(seconds: 1), () {
                          //     Get.offAll(() => AllChats());
                          //   });
                          // } else {
                          //   btnState.buttonState.value = 3;
                          //   Timer(Duration(seconds: 1), () {
                          //     btnState.buttonState.value = 0;
                          //   });
                          // }
                        }
                      },
                      child: Container(
                        child: logChild(),
                      ),
                    );
                  }),
                )),
          ],
        ),
      )),
    );
  }
}
