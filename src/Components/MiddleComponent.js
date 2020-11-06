import React, {Component} from 'react';
import LeftComponent from './LeftComponent';
import RightComponent from './RightComponent';
import {Row, Container} from 'reactstrap';

class MiddleComponent extends Component{
    render(){
        return(
            <div className="background">
                <Container>
                    <Row>
                        <LeftComponent/>
                    </Row>
                    <Row>
                        <RightComponent/>
                    </Row>
                </Container>
            </div>
        )
    }
}

export default MiddleComponent;