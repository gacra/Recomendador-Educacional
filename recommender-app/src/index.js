import React from 'react';
import ReactDOM from 'react-dom';
import registerServiceWorker from './registerServiceWorker';

import Navbar from './navbar/navbar';
import Description from './description/description'
import Content from './content/content'

// ReactDOM.render(<App />, document.getElementById('root'));

let App = (
    <div>
        <Navbar/>
        <div className='re-container'>
            <Description/>
            <Content/>
        </div>
    </div>
);

ReactDOM.render(App, document.getElementById('root'))
registerServiceWorker();