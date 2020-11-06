import React, {Component} from 'react';
import {Row, Container, Col, Button, Input, Form} from 'reactstrap';

class HeaderComponent extends Component{
    render(){
        return(
            <div className ="p-3 header mb-0 bg-dark text-white ">
                <Container>
                    <Row>
                        <Col xl="1" className="right-align">
                            <img alt="baymax" class="embed-responsive-item image " src= {process.env.PUBLIC_URL + "/bay1.jpg"}> 
                           </img>
                        </Col>
                        <Col xl="3" className="text-center">
                            <h2> Baymax </h2> 
                        </Col>

                        <Col xl="6">
                        </Col>

                       
                    </Row>
                    
                </Container>
            </div>
        )
    }
}

export default HeaderComponent;