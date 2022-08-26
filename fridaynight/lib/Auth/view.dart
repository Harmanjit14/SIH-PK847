import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/Home/view.dart';
import 'package:fridaynight/utils.dart';
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
          return Text(
            "Continue",
            style: TextStyle(
                color: light.background,
                fontSize: 20,
                fontWeight: FontWeight.bold),
          );
        }
      case 1:
        {
          return SpinKitDoubleBounce(
            color: light.background,
            size: 50.0,
          );
        }
      case 2:
        {
          return Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                Icons.verified,
                color: light.background,
              ),
              const SizedBox(
                width: 7,
              ),
              Text(
                "Success!",
                style: TextStyle(
                    color: light.background,
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
            children: [
              Icon(
                Icons.error,
                color: light.background,
              ),
              const SizedBox(
                width: 7,
              ),
              Text(
                "Check Credentials",
                style: TextStyle(
                    color: light.background,
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

  final ScrollController controller = ScrollController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      
      bottomSheet: Container(
        color: light.background,
        width: double.maxFinite,
        height: 60,
        margin: const EdgeInsets.fromLTRB(20, 20, 20, 10),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(15),
          child: Obx(() {
            return MaterialButton(
              color: light.primary,
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
                  btnState.buttonState.value = 1;
                  if (await login(username, password)) {
                    btnState.buttonState.value = 2;
                    Timer(const Duration(seconds: 1), () {
                      Get.offAll(() => const HomeScreen());
                    });
                  } else {
                    btnState.buttonState.value = 3;
                    Timer(const Duration(seconds: 1), () {
                      btnState.buttonState.value = 0;
                    });
                  }
                }
              },
              child: Container(
                child: logChild(),
              ),
            );
          }),
        ),
      ),
      backgroundColor: light.background,
      body: SafeArea(
          child: ListView(
        controller: controller,
        shrinkWrap: true,
        children: [
          SizedBox(
            width: MediaQuery.of(context).size.width,
            height: MediaQuery.of(context).size.height * 0.3,
            child: Image.asset("assets/login.gif"),
          ),
          Container(
            margin: const EdgeInsets.fromLTRB(20, 10, 20, 0),
            child: const Text(
              "FridayNight-SIH",
              textAlign: TextAlign.center,
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
            padding: const EdgeInsets.fromLTRB(20, 0, 20, 0),
            margin: const EdgeInsets.fromLTRB(20, 0, 20, 10),
            child: const Text(
              "Welcome Back, Please Login with your Institute credentials to proceed!",
              textAlign: TextAlign.center,
              style: TextStyle(
                  color: Colors.black,
                  fontSize: 20,
                  fontWeight: FontWeight.w500),
            ),
          ),
          Container(
            margin: const EdgeInsets.fromLTRB(20, 30, 20, 0),
            child: TextField(
              onTap: () {
                controller.animateTo(controller.position.maxScrollExtent,
                    duration: const Duration(milliseconds: 300),
                    curve: Curves.easeIn);
              },
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
          SizedBox(
            height: MediaQuery.of(context).size.height / 7,
          )
        ],
      )),
    );
  }
}
