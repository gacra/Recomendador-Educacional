import React from 'react';
import {MuiThemeProvider, withStyles} from '@material-ui/core/styles';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepButton from '@material-ui/core/StepButton';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import theme from '../theme';
import stepsEnum from './steps'

const styles = theme => ({
    root: {
        width: '100%',
        marginBottom: 0,
    },
});


class StepperComponent extends React.Component {
    constructor(props) {
        super(props);
        this.clickStep = this.clickStep.bind(this);
    }

    getStepsProps() {
        let stepNumber = this.props.step;
        switch (stepNumber) {
            case stepsEnum.TOPICS:
                return [{}, {}, {disabled: true}, {disabled: true}];
            case stepsEnum.QUESTIONS:
                return [{disabled: true, completed: true}, {}, {disabled: true}, {disabled: true}];
            case stepsEnum.ANSWERS:
                return [{disabled: true, completed: true}, {disabled: true, completed: true}, {}, {}];
            case stepsEnum.RECOMMENDATION:
                return [{disabled: true, completed: true}, {disabled: true, completed: true}, {completed: true}, {}];
            default:
                return null;
        }
    }

    clickStep(step) {
        this.props.clickStep(step);
    }

    render() {
        const { classes } = this.props;

        let stepsProps = this.getStepsProps();

        return(
            <Grid item xs={12} md={10}>
                <MuiThemeProvider theme={theme}>
                    <div className={classes.root}>
                        <Card className={classes.card}>
                            <Stepper alternativeLabel nonLinear activeStep={this.props.step}>
                                <Step {...stepsProps[0]}>
                                    <StepButton>
                                        Escolha os temas
                                    </StepButton>
                                </Step>
                                <Step {...stepsProps[1]}>
                                    <StepButton onClick={this.clickStep.bind(null, 1)}>
                                        Responda as perguntas
                                    </StepButton>
                                </Step>
                                <Step {...stepsProps[2]}>
                                    <StepButton onClick={this.clickStep.bind(null, 2)}>
                                        Vejas seus acertos e erros
                                    </StepButton>
                                </Step>
                                <Step {...stepsProps[3]}>
                                    <StepButton onClick={this.clickStep.bind(null, 3)}>
                                        Estude com os materiais recomendados
                                    </StepButton>
                                </Step>
                            </Stepper>
                        </Card>
                    </div>
                </MuiThemeProvider>
            </Grid>
        );
    }

}

export default withStyles(styles)(StepperComponent);