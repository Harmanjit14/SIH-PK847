import 'package:flutter/material.dart';
import 'package:flutter_native_splash/flutter_native_splash.dart';
import 'package:fridaynight/Auth/view.dart';
import 'package:get/get.dart';

void main() {
  WidgetsBinding widgetsBinding = WidgetsFlutterBinding.ensureInitialized();
  FlutterNativeSplash.preserve(widgetsBinding: widgetsBinding);
  runApp(const MyApp());
  FlutterNativeSplash.remove();
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      title: 'FridayNight-SIH',
      theme: ThemeData(
        // useMaterial3: true,
        splashColor: Colors.amber[700],
        progressIndicatorTheme: const ProgressIndicatorThemeData(color: Colors.amber),
        primarySwatch: Colors.amber,
      ),
      home: const LoginSreen(),
    );
  }
}
