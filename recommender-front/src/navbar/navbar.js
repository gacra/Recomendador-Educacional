import React from 'react';
import {MuiThemeProvider, withStyles} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Icon from '@material-ui/core/Icon'
import Button from '@material-ui/core/Button';
import theme from '../theme'
import '../index.css'

const styles = {
    root: {
        flexGrow: 1,
        paddingTop: 90
    },
    appBar: {
        position: 'fixed',
        top: 0
    },
    typography: {
        flex: 1,
        fontSize: '180%'
    },
    mainIcon: {
        fontSize: "35px"
    },
    icon: {
        marginRight: 8
    }
};

class NavBar extends React.Component {

    render() {
        const { classes } = this.props;

        return (
            <MuiThemeProvider theme={theme}>
                <div className={classes.root}>
                    <AppBar className={classes.appBar} color="primary">
                        <Toolbar>
                            <Icon className={classes.mainIcon}>not_listed_location</Icon>
                            <Typography variant="headline" color="inherit" className={classes.typography}>
                                <a href=""><b>ñ</b> sei o que <b>ñ</b> sei</a>
                            </Typography>
                            <a href="https://github.com/gacra/Recomendador-Educacional"
                               target="_blank"
                               rel="noopener noreferrer">
                                <Button color="inherit">
                                    <Icon className={classes.icon}>code</Icon>Código fonte
                                </Button>
                            </a>
                            <a href="https://www.linkedin.com/in/guilherme-jos%C3%A9-acra-6a5b7a11a/"
                               target="_blank" rel="noopener noreferrer">
                                <Button color="inherit">
                                    <Icon className={classes.icon}>person</Icon>Contato
                                </Button>
                            </a>
                        </Toolbar>
                    </AppBar>
                </div>
            </MuiThemeProvider>
        )
    }

}

export default withStyles(styles)(NavBar);