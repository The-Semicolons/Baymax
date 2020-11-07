import React, { Component } from 'react';
import { Navbar, Form, Input, Button, FormGroup, InputGroup, InputGroupAddon } from 'reactstrap';

class Footer extends Component{
    render(){
        return(
            <React.Fragment>
                 <Navbar className="bg-dark" dark>
                    <Form className="form-inline">
                        <FormGroup>
                            <InputGroup>
                                <Input type="text" placeholder="Type your message here..." size="121" aria-label="Message"/>
                                <InputGroupAddon addonType="append">
                                    <Button type="button">
                                        Send
                                    </Button>
                                </InputGroupAddon>
                            </InputGroup>
                            <Button className="btn ml-3 btn-danger" type="button">
                                Speak
                            </Button>
                        </FormGroup>
                    </Form>
                </Navbar>
            </React.Fragment>
        );
    }
}

export default Footer;