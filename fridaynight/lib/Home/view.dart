import 'package:flutter/material.dart';
import 'package:fridaynight/Auth/query.dart';
import 'package:fridaynight/Home/home_tab/view.dart';
import 'package:fridaynight/Home/profile_tab/view.dart';
import 'package:fridaynight/Home/request_tab/view.dart';
import 'package:fridaynight/chat/view.dart';
import 'package:fridaynight/utils.dart';
import 'package:get/get.dart';
import 'package:salomon_bottom_bar/salomon_bottom_bar.dart';

class BottomNavbarState extends GetxController {
  RxInt currentPage = 0.obs;
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final _controller = PageController(initialPage: 0);

  final state = Get.put(BottomNavbarState());
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: (() {
          Get.to(() => const Chat());
        }),
        child: Icon(
          Icons.mic,
          color: light.background,
        ),
      ),
      body: SafeArea(
        child: PageView(
          physics: const NeverScrollableScrollPhysics(),
          controller: _controller,
          children: [
            HomePage(),
            const RequestsTab(),
            Text("Acadamic"),
            const ProfileTab(),
          ],
        ),
      ),
      extendBody: true,
      bottomNavigationBar: Obx(
        () => SalomonBottomBar(
          currentIndex: state.currentPage.value,
          onTap: (tap) {
            state.currentPage.value = tap;
            _controller.animateToPage(tap,
                duration: const Duration(milliseconds: 300),
                curve: Curves.easeIn);
          },
          items: [
            SalomonBottomBarItem(
                icon: const Icon(Icons.home),
                title: const Text("Home"),
                selectedColor: light.primary),
            SalomonBottomBarItem(
                icon: const Icon(Icons.list_alt),
                title: const Text("My Orders"),
                selectedColor: light.primary),
            SalomonBottomBarItem(
                icon: const Icon(Icons.school),
                title: const Text("Acadamic"),
                selectedColor: light.primary),
            SalomonBottomBarItem(
                icon: const Icon(Icons.person),
                title: const Text("Profile"),
                selectedColor: light.primary),
          ],
        ),
      ),
    );
  }
}
