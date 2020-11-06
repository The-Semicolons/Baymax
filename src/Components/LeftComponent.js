import React, {Component} from 'react';
import {Row, Container, Col, Button, Input, Form} from 'reactstrap'; 
import HeaderComponent from './HeaderComponent';

class LeftComponent extends Component{
    render(){
        return(
            <React.Fragment>
                <Container>
                    <Row className="align-items-center left">
                        <Col xl="2">
                            <Button className="btn"> Left message </Button> 
                        </Col>
                        <Col xl="4">
                            
                        </Col>
                        <Col xl="4">
                        </Col>
                        <Col xl="2">

                        </Col>
                    </Row>
                </Container>
            </React.Fragment>
        )
    }
}
export default LeftComponent;