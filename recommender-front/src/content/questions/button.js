import React from 'react';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import {MuiThemeProvider, withStyles} from '@material-ui/core/styles';

import theme from '../../theme'

const styles = {
    button: {
        width: '100%'
    }
}

class SendButton extends React.Component {
    constructor(props) {
        super(props);
        this.clickButton = this.clickButton.bind(this);
    }

    clickButton() {
        this.props.clickButton();
    }

    render() {
        const { classes } = this.props;

        return (
            <Grid item xs={10} md={8}>
                <MuiThemeProvider theme={theme}>
                    <Button variant="contained" color="primary" className={classes.button} onClick={this.clickButton}>
                        Concluir Questionário
                    </Button>
                </MuiThemeProvider>
            </Grid>
        )
    };

}

export default withStyles(styles)(SendButton);