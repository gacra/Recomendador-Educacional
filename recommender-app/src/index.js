import React from 'react';
import ReactDOM from 'react-dom';
import registerServiceWorker from './registerServiceWorker';

// ReactDOM.render(<App />, document.getElementById('root'));

let App = (
    <div>
        Olá Mundo do React
    </div>
)

ReactDOM.render(App, document.getElementById('root'))
registerServiceWorker();