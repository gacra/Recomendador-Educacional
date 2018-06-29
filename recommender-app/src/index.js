import React from 'react';
import ReactDOM from 'react-dom';
import registerServiceWorker from './registerServiceWorker';

import Navbar from './navbar/navbar';

// ReactDOM.render(<App />, document.getElementById('root'));

let App = (
    <div>
        <Navbar/>
        <div className='re-container'>
        </div>
    </div>
);

ReactDOM.render(App, document.getElementById('root'))
registerServiceWorker();