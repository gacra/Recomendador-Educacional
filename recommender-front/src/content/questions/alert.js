import React from 'react';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import Typography from '@material-ui/core/Typography';
import Icon from '@material-ui/core/Icon'
import {withStyles} from "@material-ui/core/styles/index";

import colors from '../../colors'

const styles = {
    card: {
        backgroundColor: colors.warningAlert,
        padding: 16,
    },
    icon: {
        display: 'inline',
        paddingTop: '8%',
        height: "108%"
    }
}

class Alert extends React.Component {

    render() {
        const {classes} = this.props;

        return (
            <Grid item xs={10} md={8}>
                <Card className={classes.card}>
                    <Grid container spacing={0} justify='center'>
                        <Grid item xs={1}>
                            <Grid container spacing={0} justify='center' style={{height: 'inherit'}}>
                                <Icon className={classes.icon}>error</Icon>
                            </Grid>
                        </Grid>

                        <Grid item xs={11}>
                            <Typography component="p" className={classes.text}>
                                <b>É necessário responder todas as perguntas para concluir o questionário</b><br/>
                                Verifique qual pergunta não foi respondida e clique novamente em "CONCLUIR QUESTIONÁRIO"
                            </Typography>
                        </Grid>
                    </Grid>
                </Card>
            </Grid>
        )
    };

}

export default withStyles(styles)(Alert);