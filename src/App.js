import React, { Component } from 'react';
import './App.css';
import ChattingInterface from './Components/ChatingInterface';

class App extends Component{
	render() {
		return(
			<div className="background">
				<br />
				<ChattingInterface />
				<br />
			</div>
		);
	}
}

export default App;
