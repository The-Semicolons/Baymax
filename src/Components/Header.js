import React, { Component } from 'react';
import { Navbar, NavbarBrand } from 'reactstrap';

class Header extends Component{
    render(){
        return(
            <React.Fragment>
                <Navbar className="bg-dark" dark>
                    <NavbarBrand>
                        <img src={process.env.PUBLIC_URL + "/Baymax.png"} className="navbarimg mr-2"/>
                        Baymax
                    </NavbarBrand>
                </Navbar>
            </React.Fragment>
        );
    }
}

export default Header;