import React from 'react';
import ReactDOM from 'react-dom';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import registerServiceWorker from './registerServiceWorker';

import NavBar from './navbar/navbar'
import Description from './description/description'
import Content from './content/content'

let descriptionRef = React.createRef();

let App = (
    <React.Fragment>
        <CssBaseline />
        <NavBar/>
        <Grid container justify='center' spacing={40} style={{width: "100%", marginLeft: 0 , marginRight:0}}>
            <Description ref={descriptionRef}/>
            <Content descriptionRef={descriptionRef}/>
        </Grid>
    </React.Fragment>
)

ReactDOM.render(App, document.getElementById('root'));
registerServiceWorker();
