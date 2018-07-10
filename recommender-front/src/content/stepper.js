import React from 'react';
import {MuiThemeProvider, withStyles} from '@material-ui/core/styles';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepButton from '@material-ui/core/StepButton';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
// import colors from '../utilsMatUI'
import theme from '../theme'

const styles = theme => ({
    root: {
        width: '100%',
        marginBottom: 0,
    },
});


class StepperComponent extends React.Component {

    getStepsProps() {
        let stepNumber = this.props.step;
        switch (stepNumber) {
            case 0:
                return [{}, {disabled: true}, {disabled: true}]
            case 1:
                return [{disabled: true, completed: true}, {}, {}]
            case 2:
                return [{disabled: true, completed: true}, {completed: true}, {}]
        }
    }

    render() {
        const { classes } = this.props;

        let stepsProps = this.getStepsProps()

        return(
            <Grid item xs={12} md={10}>
                <MuiThemeProvider theme={theme}>
                    <div className={classes.root}>
                        <Card className={classes.card}>
                            <Stepper alternativeLabel nonLinear activeStep={this.props.step}>
                                <Step {...stepsProps[0]}>
                                    <StepButton>
                                        Responda as perguntas
                                    </StepButton>
                                </Step>
                                <Step {...stepsProps[1]}>
                                    <StepButton>
                                        Vejas seus acertos e erros
                                    </StepButton>
                                </Step>
                                <Step {...stepsProps[2]}>
                                    <StepButton>
                                        Estude com os materiais recomendados
                                    </StepButton>
                                </Step>
                            </Stepper>
                        </Card>
                    </div>
                </MuiThemeProvider>
            </Grid>
        )
    }

}

export default withStyles(styles)(StepperComponent);