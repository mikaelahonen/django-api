import React, { Component } from 'react';
import { Button, Jumbotron, Grid, Row, Col } from 'react-bootstrap';
import Head from './Components';

class Home extends Component {
  render() {
    return (
		<div>
			<Head head="Home"/>
			<Jumbotron>
				<h2>Quantiefied Self App</h2>
				<p><i>Welcome!</i></p>
			</Jumbotron>
			<Button bsStyle='primary' bsSize='large'>Home button</Button>
		</div>
	);
  }
}

export default Home;