import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:fridaynight/utils.dart';
import 'package:google_speech/google_speech.dart';
import 'package:rxdart/rxdart.dart';
import 'package:sound_stream/sound_stream.dart';
import 'package:dialogflow_grpc/dialogflow_grpc.dart' as dialogflowLib;
import 'package:dialogflow_grpc/generated/google/cloud/dialogflow/v2beta1/session.pb.dart';

dialogflowLib.DialogflowGrpcV2Beta1? dialogflow;
SpeechToText? speechToText;
RecognitionConfig? config;

class Chat extends StatefulWidget {
  const Chat({Key? key}) : super(key: key);

  @override
  _ChatState createState() => _ChatState();
}

class _ChatState extends State<Chat> {
  final List<ChatMessage> _messages = <ChatMessage>[];
  final TextEditingController _textController = TextEditingController();

  final RecorderStream _recorder = RecorderStream();

  bool recognizing = false;
  bool recognizeFinished = false;
  String text = '';
  StreamSubscription<List<int>>? _audioStreamSubscription;
  BehaviorSubject<List<int>>? _audioStream;

  @override
  void initState() {
    super.initState();
    initPlugin();
    _recorder.initialize();
  }

  @override
  void dispose() {
    _audioStreamSubscription?.cancel();
    super.dispose();
  }

  Future<void> initPlugin() async {
    await Future.wait([_recorder.initialize()]);
    final serviceAccount = dialogflowLib.ServiceAccount.fromString(
        (await rootBundle.loadString('assets/key.json')));
    final serviceAccount2 = ServiceAccount.fromString(
        (await rootBundle.loadString('assets/key.json')));
    dialogflow =
        dialogflowLib.DialogflowGrpcV2Beta1.viaServiceAccount(serviceAccount);

    speechToText = SpeechToText.viaServiceAccount(serviceAccount2);
  }

  RecognitionConfig _getConfig() => RecognitionConfig(
      encoding: AudioEncoding.LINEAR16,
      model: RecognitionModel.basic,
      enableAutomaticPunctuation: true,
      sampleRateHertz: 16000,
      languageCode: 'pa-IN');

  void handleSubmitted(text) async {
    _textController.clear();

    ChatMessage message = ChatMessage(
      text: text,
      name: "You",
      type: true,
    );

    setState(() {
      _messages.insert(0, message);
    });

    DetectIntentResponse data = await dialogflow!.detectIntent(text, 'pa-IN');
    String fulfillmentText = data.queryResult.fulfillmentText;
    debugPrint("DialogFlow");
    debugPrint(fulfillmentText);
    if (fulfillmentText.isNotEmpty) {
      ChatMessage botMessage = ChatMessage(
        text: fulfillmentText,
        name: "Bot",
        type: false,
      );
      if (int.tryParse(fulfillmentText) != null) {
        int resp = int.parse(fulfillmentText);
        switch (resp) {
          case 1:
            {
              if (await requestCertificate("1", false)) {
                botMessage = const ChatMessage(
                  text: "ਮੈਂ ਤੁਹਾਡੀ ਬੇਨਤੀ ਅਧਿਕਾਰੀਆਂ ਨੂੰ ਭੇਜ ਦਿੱਤੀ ਹੈ",
                  name: "Bot",
                  type: false,
                );
              } else {
                botMessage = const ChatMessage(
                  text:
                      "ਅਫਸੋਸ ਹੈ ਕਿ ਮੈਂ ਤੁਹਾਡੀ ਬੇਨਤੀ ਨੂੰ ਅਧਿਕਾਰੀਆਂ ਨੂੰ ਅੱਗੇ ਭੇਜਣ ਵਿੱਚ ਅਸਮਰੱਥ ਸੀ",
                  name: "Bot",
                  type: false,
                );
              }
              return;
            }
          default:
        }
      }

      setState(() {
        _messages.insert(0, botMessage);
      });
    }
  }

  void streamingRecognize() async {
    config = _getConfig();
    _audioStream = BehaviorSubject<List<int>>();
    _audioStreamSubscription = _recorder.audioStream.listen((event) {
      _audioStream!.add(event);
    });

    await _recorder.start();

    setState(() {
      recognizing = true;
    });

    final responseStream = speechToText!.streamingRecognize(
        StreamingRecognitionConfig(config: config!, interimResults: true),
        _audioStream!);

    var responseText = '';

    responseStream.listen((data) {
      final currentText =
          data.results.map((e) => e.alternatives.first.transcript).join('\n');

      if (data.results.first.isFinal) {
        responseText += '\n' + currentText;
        setState(() {
          text = responseText;
          recognizeFinished = true;
        });
      } else {
        setState(() {
          text = responseText + '\n' + currentText;
          recognizeFinished = true;
        });
      }
    }, onDone: () {
      setState(() async {
        handleSubmitted(responseText);
        recognizing = false;
      });
    });
  }

  void stopRecording() async {
    await _recorder.stop();
    await _audioStreamSubscription?.cancel();
    await _audioStream?.close();
    setState(() {
      recognizing = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(children: <Widget>[
        Flexible(
            child: ListView.builder(
          padding: const EdgeInsets.all(8.0),
          reverse: true,
          itemBuilder: (_, int index) => _messages[index],
          itemCount: _messages.length,
        )),
        const Divider(height: 1.0),
        Container(
            decoration: BoxDecoration(color: Theme.of(context).cardColor),
            child: IconTheme(
              data: IconThemeData(color: Theme.of(context).colorScheme.primary),
              child: Container(
                margin: const EdgeInsets.symmetric(horizontal: 10.0),
                child: Row(
                  children: <Widget>[
                    Flexible(
                      child: TextField(
                        style: const TextStyle(
                          fontSize: 18,
                        ),
                        controller: _textController,
                        onSubmitted: handleSubmitted,
                        decoration: const InputDecoration.collapsed(
                            hintText: "Send a message"),
                      ),
                    ),
                    Container(
                      margin: const EdgeInsets.symmetric(horizontal: 4.0),
                      child: IconButton(
                        icon: const Icon(Icons.send),
                        onPressed: () => handleSubmitted(_textController.text),
                      ),
                    ),
                    IconButton(
                      iconSize: 30.0,
                      icon: Icon(recognizing ? Icons.mic_off : Icons.mic),
                      onPressed:
                          recognizing ? stopRecording : streamingRecognize,
                    ),
                  ],
                ),
              ),
            )),
      ]),
    );
  }
}

class ChatMessage extends StatelessWidget {
  const ChatMessage({Key? key, this.text, this.name, this.type})
      : super(key: key);

  final String? text;
  final String? name;
  final bool? type;

  List<Widget> otherMessage(context) {
    return <Widget>[
      Container(
        margin: const EdgeInsets.only(right: 16.0),
        child: CircleAvatar(
            backgroundColor: light.primary,
            child: Text(
              name!,
              style: TextStyle(
                  fontWeight: FontWeight.bold, color: light.background),
            )),
      ),
      Expanded(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Text(name!, style: const TextStyle(fontWeight: FontWeight.bold)),
            Container(
              margin: const EdgeInsets.only(top: 5.0),
              child: Text(text!, style: const TextStyle(fontSize: 20)),
            ),
          ],
        ),
      ),
    ];
  }

  List<Widget> myMessage(context) {
    return <Widget>[
      Expanded(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.end,
          children: <Widget>[
            Text(name!, style: const TextStyle(fontWeight: FontWeight.bold)),
            Container(
              margin: const EdgeInsets.only(top: 5.0),
              child: Text(text!, style: const TextStyle(fontSize: 20)),
            ),
          ],
        ),
      ),
      Container(
        margin: const EdgeInsets.only(left: 16.0),
        child: CircleAvatar(
            backgroundColor: light.primary,
            child: Text(
              name!,
              style: TextStyle(
                  fontWeight: FontWeight.bold, color: light.background),
            )),
      ),
    ];
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 10.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: type! ? myMessage(context) : otherMessage(context),
      ),
    );
  }
}
