import React from 'react';
import ReactDOM from 'react-dom';
import './style.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import 'bootstrap/dist/css/bootstrap.css';
import 'font-awesome/css/font-awesome.css';
import { BrowserRouter } from 'react-router-dom';


ReactDOM.render((
	<BrowserRouter>
		<App />
	</BrowserRouter>
	), document.getElementById('root')
);
	
registerServiceWorker();
