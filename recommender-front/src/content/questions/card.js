import React from 'react';
import Card from '@material-ui/core/Card';
import Grid from '@material-ui/core/Grid';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import Chip from '@material-ui/core/Chip';
import FormControl from '@material-ui/core/FormControl';
import RadioGroup from '@material-ui/core/RadioGroup';
import Radio from '@material-ui/core/Radio';
import FormControlLabel from '@material-ui/core/FormControlLabel';

import {createMuiTheme, MuiThemeProvider} from '@material-ui/core/styles';
import colors from '../../colors'
import {withStyles} from "@material-ui/core/styles/index";

const stepTheme = createMuiTheme({
    overrides:{
        MuiIconButton:{
            root: {
                width: 40,
                height: 35,
                marginLeft: 8
            },
        },
        MuiRadio: {
            colorSecondary: {
                '&$checked': {
                    color: colors.radio
                }
            },

        }
    }
})

const styles = {
    cardTitle: {
        color: colors.orangeText
    },
    chip: {
        marginBottom: 10,
        marginTop: 10
    },
    rightAlternative: {
        color: colors.rightAlternativeText
    },
    alternative: {
        color: colors.grayText
    },
    warningCard:{
        backgroundColor: colors.warningCard
    },
    rightCard: {
        backgroundColor: colors.rightCard
    },
    wrongCard: {
        backgroundColor: colors.wrongCard
    },
    normalCard: {
        backgroundColor: colors.normalCard
    }
};

class QuestionCardList extends React.Component {

    constructor(props) {
        super(props);
        this.changeSelectedAlternative = this.changeSelectedAlternative.bind(this)
    }

    changeSelectedAlternative(event) {
        let questionId = event.target['name'];
        let alternative = parseInt(event.target['value'], 10);
        this.props.changeSelectedAlternative(questionId, alternative);
    }

    getCardColor() {
        const { classes } = this.props;

        let correctAlternative = this.props.correctAlternative;
        let selectedAlternative = this.props.selectedAlternative;
        let unanswered = this.props.unanswered;

        if (unanswered === true) {
            return classes.warningCard;
        } else if (correctAlternative !== false) {
            let rightAnswers = correctAlternative === selectedAlternative;
            if (rightAnswers) {
                return classes.rightCard;
            } else {
                return classes.wrongCard;
            }
        }
        return classes.normalCard;
    }

    render() {
        const { classes } = this.props;
        let questionIndex = this.props.index;
        let title = "Pergunta " + (questionIndex + 1) + " (de " + this.props.total + ")";
        let {stem, alternatives, topic, _id} = this.props.question;
        let correctAlternative = this.props.correctAlternative;

        let disabled = correctAlternative? true: false;

        let alternativesRadio = alternatives.map((item, index) => {
            let alternativeText;
            if (correctAlternative === index) {
                alternativeText = (<span className={classes.rightAlternative}><b>{item}</b></span>)
            } else {
                alternativeText = (<span className={classes.alternative}>{item}</span>);
            }

            return (
                <FormControlLabel value={index.toString()} control={<Radio />} label={alternativeText} key={index}/>
            );
        });

        return (
            <Grid item xs={10} md={8}>
                <Card className={this.getCardColor()}>
                    <CardContent>
                        <Typography variant="headline" component="h3" className={classes.cardTitle}>
                            {title}
                        </Typography>
                        <Chip label={this.props.topics[topic]} className={classes.chip} />
                        <Typography component="p">
                            {stem}
                        </Typography>
                        <MuiThemeProvider theme={stepTheme}>
                        <FormControl component="fieldset" required disabled={disabled}>
                            <RadioGroup
                                name={_id}
                                value={this.props.selectedAlternative.toString()}
                                onChange={this.changeSelectedAlternative}
                            >
                                {alternativesRadio}
                            </RadioGroup>
                        </FormControl>
                        </MuiThemeProvider>
                    </CardContent>
                </Card>
            </Grid>
        )
    };

}

export default withStyles(styles)(QuestionCardList);