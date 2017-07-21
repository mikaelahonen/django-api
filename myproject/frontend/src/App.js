//React
import React, { Component } from 'react';
//import logo from './logo.svg';
//import './App.css';
//Bootstrap
import { Button, Jumbotron, Grid, Row, Col } from 'react-bootstrap';
//React Router
import {Switch, Route} from 'react-router-dom'
//Components
import Menu from './Menu';
import Head from './Components';
import Home from './Home';
import Gym from './Gym';

class App extends Component {
	render() {
		return (
			<div>
				<Menu/>				
				<Grid>
					<Row>
						<Col md="12">
							<Switch>
								<Route exact path='/' component={Home}/>
								<Route path='/gym' component={Gym}/>
							</Switch>
						</Col>
					</Row>
				</Grid>
			</div>
    );
  }
}

export default App;
