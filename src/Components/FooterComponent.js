import React, {Component} from 'react';
import {Row, Container, Col, Button, Input, Form} from 'reactstrap';

class FooterComponent extends Component{
    render(){
        return(
            <div className ="p-3 footer mb-0 bg-dark text-white ">
                <Container>
                    <Row>

                        {/*1st column*/}
                        <Col xl="10">
                            <Input className="form-control"  placeholder="Enter your message here"/>
                           
                            

                        </Col>

                        {/*2nd column */}
                        <Col xl="2">
                            <Button className="btn1 right-align"> Speak </Button>
                        </Col>

                       
                    </Row>
                    
                </Container>
            </div>
        )
    }
}

export default FooterComponent;