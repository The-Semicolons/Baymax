import React from 'react';

export default function SpeechToText() {
    var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
    var recognition = new SpeechRecognition();
    var text = "";
    // This runs when the speech recognition service returns result
    recognition.onresult = function(event) {
        text = event.results[0][0].transcript;
        newtext = text;
        var confidence = event.results[0][0].confidence;
        //console.log(text);
    };
    // start recognition
    recognition.start();
};