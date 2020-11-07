import React, { Component } from 'react';
import { Card, CardBody, CardText, Row, Col } from 'reactstrap';

class RightMessageBox extends Component{
    
    constructor(props){
        super(props);
        this.state = {
            text : this.props.text
        };
    }
    
    render(){
        return(
            <div>
                <Row className="justify-content-end">
                    <Col xl={5}>
                        <Card className="mx-3 my-1">
                            <CardBody>
                                <CardText>
                                    {this.state.text}
                                </CardText>
                            </CardBody>
                        </Card>
                    </Col>
                </Row>
            </div>
        );
    }
}

export default RightMessageBox;