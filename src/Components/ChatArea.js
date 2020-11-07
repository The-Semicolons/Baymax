import React, { Component } from 'react';
import LeftMessageBox from './LeftMessageBox';
import RightMessageBox from './RightMessageBox';

class ChatArea extends Component{
    render(){
        return(
            <div className="chatarea">
                <RightMessageBox text="OUCH!!!"/>
                <LeftMessageBox text="HI! I am Baymax. Your personel healthcare companion."/>
                <LeftMessageBox text="On a scale of one to ten, How would you rate youe pain?"/>
                <RightMessageBox text="I don't know."/>
                <LeftMessageBox text="..."/>
            </div>
        );
    }
}

export default ChatArea;