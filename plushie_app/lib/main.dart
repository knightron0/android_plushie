import 'dart:io';


import 'package:flutter/material.dart';
import 'package:tflite/tflite.dart';
import 'package:image_picker/image_picker.dart';
import 'package:image/image.dart' as img;
import 'package:flutter/services.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: TfliteHome(),
    );
  }
}

//const String finalmodel = ""

class TfliteHome extends StatefulWidget {
  @override
  TfliteHomeState createState() => TfliteHomeState();
}

class TfliteHomeState extends State<TfliteHome> {
  String model = "Android PlushieNet";
  File image;

  double imgheight;
  double imgwidth;
  bool busy = false;

  List _recognitions;

  @override
  void InitState(){
    super.initState();
    busy = true;
    loadModel().then((val){
      setState(() {
        busy = false;
      });
    });
  }
  loadModel() async {
    Tflite.close();
    try {
      String res;
      res = await Tflite.loadModel(
        model: "assets/model.tflite",
        labels: "assets/labels.txt",
      );
    } on PlatformException {
      print("Failed to load the model");
    }
  }
  selectfromImagePicker() async {
    var image = await ImagePicker.pickImage(source: ImageSource.gallery);
    if(image == null) return;
    setState(() {
      busy = true;
    });
    predictImage(image);
    print(_recognitions);
  }
  predictImage(File image2) async {
    if(image2 == null) return;
    androidPlushie(image2);
    FileImage(image)
        .resolve(ImageConfiguration())
        .addListener((ImageStreamListener((ImageInfo info, bool _) {
          setState(() {
            imgheight = info.image.height.toDouble();
            imgwidth = info.image.width.toDouble();
          });
    })));
    setState(() {
      image = image2;
      busy = false;
    });
  }

  androidPlushie(File img) async {
    var recognitions = await Tflite.runModelOnImage(
        path: "assets/model.tflite",
        imageMean: 0.0,
        imageStd: 255.0,
        numResults: 2,
        threshold: 0.2,
    );
    setState(() {
      _recognitions = recognitions;
    });
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;

    List<Widget> stackChildren = [];

    stackChildren.add(Positioned(
      top: 0.0,
      left: 0.0,
      width: size.width,
      child: image == null ? Text("No Image Selected") : Image.file(image),
    ));


    if (busy) {
      stackChildren.add(Center(
        child: CircularProgressIndicator(),
      ));
    }

    return Scaffold(
      appBar: AppBar(
        title: Text("TFLite Demo"),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.image),
        tooltip: "Pick Image from gallery",
        onPressed: selectfromImagePicker,
      ),
      body: Stack(
        children: stackChildren,
      ),
    );
  }
}