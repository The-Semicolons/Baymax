import React, {Component} from 'react';
import {Row, Container, Col, Button, Input, Form} from 'reactstrap'; 

class RightComponent extends Component{
    render(){
        return(
            <React.Fragment>
                <Container>
                    <Row className="align-items-center">
                        <Col xl="2">
                            
                        </Col>
    
                        <Col xl="4"> 
                        </Col>
    
                        <Col xl="3">
                                
                        </Col>
    
                        <Col xl="3">
                            <Button className="btn"> Right message </Button>
                                
                        </Col>

                    </Row>
                </Container>
            </React.Fragment>
        )
    }
}
export default RightComponent;