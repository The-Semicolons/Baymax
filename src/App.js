import React, { Component } from 'react';
import {Row} from 'reactstrap';
import MiddleComponent from './Components/MiddleComponent';
import RightComponent from './Components/RightComponent';
import LeftComponent from './Components/LeftComponent';
import './App.css';

import FooterComponent from './Components/FooterComponent';
import HeaderComponent from './Components/HeaderComponent';


class App extends Component{
	render() {
		return(
			<div>
          <HeaderComponent/>
          <MiddleComponent/>
          <FooterComponent/>
        
				
			</div>
		);
	}
}

export default App;
