import React, { Component } from 'react';
import { Container } from 'reactstrap';
import Header from './Header';
import Footer from './Footer';
import ChatArea from './ChatArea';

class ChattingInterface extends Component{
    render(){
        return(
            <React.Fragment>
                <Container>
                    <Header />
                    <ChatArea />
                    <Footer />
                </Container>
            </React.Fragment>
        );
    }
}

export default ChattingInterface;