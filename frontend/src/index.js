import React from 'react';
import ReactDOM from 'react-dom';
import './css/index.css';
import Menu from './components/menu';
import Cabecera from './components/cabecera';
import App from './components/App';
import MenuLeft from './components/menu_left';
import Pie from './components/footer';


import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Menu />, document.getElementById('menu'));
ReactDOM.render(<Cabecera />, document.getElementById('cabecera'));
ReactDOM.render(<MenuLeft /> , document.getElementById('menu_left'));
ReactDOM.render(<App /> , document.getElementById('root'));
ReactDOM.render(<Pie /> , document.getElementById('footer'));
registerServiceWorker();
