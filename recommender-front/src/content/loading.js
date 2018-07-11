import React from 'react'
import Grid from '@material-ui/core/Grid';
import CircularProgress from '@material-ui/core/CircularProgress';
import {MuiThemeProvider, withStyles} from '@material-ui/core/styles';
import theme from "../theme";

const styles = {
    div: {
        marginTop: 30,
        marginBottom: 30
    },
    divFull: {
        marginTop: 30,
        marginBottom: 1000
    },
}

class Loading extends React.Component {

    render() {
        let {classes} = this.props;
        let gridClass = (this.props.full === true)? classes.divFull: classes.div;

        return (
            <MuiThemeProvider theme={theme}>
                <Grid item xs={10} md={8} className={gridClass}>
                    <Grid container justify='center' spacing={16} style={{width: "100%", marginLeft: 0, marginRight: 0}}>
                        <CircularProgress/>
                    </Grid>
                </Grid>
            </MuiThemeProvider>
        )
    }

}

export default withStyles(styles)(Loading);