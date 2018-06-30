import React from 'react';
import ReactDOM from 'react-dom';
import registerServiceWorker from './registerServiceWorker';

import Navbar from './navbar/navbar';
import Description from './description/description'
import Content from './content/content'

// ReactDOM.render(<App />, document.getElementById('root'));

let descriptionRef = React.createRef();

let App = (
    <div>
        <Navbar/>
        <div className='re-container'>
            <Description ref={descriptionRef}/>
            <Content descriptionRef={descriptionRef}/>
        </div>
    </div>
);

ReactDOM.render(App, document.getElementById('root'))
registerServiceWorker();