import React from 'react';
import ReactDOM from 'react-dom';
import './home.css';

function renderDOM() {
  const root = document.createElement('div');
  root.id = 'root';
  document.body.appendChild(root);
  ReactDOM.render(<Home />, document.getElementById('root'));
}

function Home() {
    return(
      <div className='Home'>
        <h1>Welcome to AgingHub</h1>
      </div>
    );
}

renderDOM();

export default Home;