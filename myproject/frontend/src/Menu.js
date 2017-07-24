import React, { Component } from 'react';
import { Navbar, MenuItem, Nav, NavDropdown, NavItem } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import FontAwesome from  'react-fontawesome';

class Menu extends Component {
	
	render() {
		return (
			<Navbar inverse collapseOnSelect>
				<Navbar.Header>
					<Navbar.Brand>
						<Link to="/"><FontAwesome name="home"/></Link>
					</Navbar.Brand>
					<Navbar.Toggle />
				</Navbar.Header>
				<Navbar.Collapse>
					<Nav>
						{/*<NavItem eventKey={2}>Link</NavItem>*/}
						<NavDropdown eventKey={3} title={<span><FontAwesome name="bolt"/> Gym</span>} id="basic-nav-dropdown">
							<MenuItem header>Home</MenuItem>
							<MenuItem eventKey={3.1}><Link to='/gym'>Gym</Link></MenuItem>
							<MenuItem divider />
							<MenuItem header>Templates</MenuItem>
							<MenuItem eventKey={3.2}><Link to='/gym/workouts'>Workouts</Link></MenuItem>
							<MenuItem divider />
							<MenuItem header>Training</MenuItem>
							<MenuItem eventKey={3.3}>Separated link</MenuItem>
						</NavDropdown>
					</Nav>
					<Nav pullRight>
						<NavItem eventKey={1} href="/"><FontAwesome name="user"/> User</NavItem>
						{/*<NavItem eventKey={2} href="/">Link Right</NavItem>*/}
					</Nav>
				</Navbar.Collapse>
			</Navbar>
		);
		}
	}

export default Menu;
