import React from 'react';
import axios from 'axios';
import Grid from '@material-ui/core/Grid';

import Stepper from './stepper'
import Questions from './questions/questions'
import Recommendation from './recommendation/recommendation'

class Content extends React.Component {

    tabNames = ['Perguntas', 'Materiais recomendados'];

    constructor(props) {
        super(props);
        this.state = {
            activeTab: 0,
            topics: {},
            step: stepsEnum.QUESTIONS,
            wrongQuestions: []
        };
        this.changeActiveTab = this.changeActiveTab.bind(this);
        this.setCorrected = this.setCorrected.bind(this);
        this.clickStep = this.clickStep.bind(this);
    }

    componentWillMount() {
        let self = this;
        axios.get('http://localhost:8000/topics/').then(function (response) {
            let topics = {};

            response.data.forEach((item) => {
                topics[item["code"]] = item["description"];
            });

            self.setState({
                topics: topics
            });

        });
    }

    changeActiveTab(index) {
        this.setState({activeTab: index});
    }

    setCorrected(wrongQuestions) {
        this.setState({
            step: stepsEnum.ANSWERS
        });
        this.setState({
            wrongQuestions: wrongQuestions
        });
    }

    clickStep(step) {
        this.setState({
            step: step
        });
    }

    getContent() {
        let step = this.state.step;
        if(step === stepsEnum.ANSWERS || step === stepsEnum.QUESTIONS) {
            return (
                <Questions topics={this.state.topics}
                           descriptionRef={this.props.descriptionRef}
                           setCorrected={this.setCorrected}/>
            )
        } else if(step === stepsEnum.RECOMMENDATION) {
            return (
                <Recommendation wrongQuestions={this.state.wrongQuestions} descriptionRef={this.props.descriptionRef}/>
            )
        }
    }

    render() {
        return (
            <Grid container justify='center' spacing={40} style={{width: "100%", marginLeft: 0 , marginRight:0}}>
                <Stepper step={this.state.step} clickStep={this.clickStep}/>
                {this.getContent()}
            </Grid>
        );
    }

}

var stepsEnum = {
    QUESTIONS: 0,
    ANSWERS: 1,
    RECOMMENDATION: 2
}

export default Content;
