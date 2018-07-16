import React from 'react';
import axios from 'axios';
import Grid from '@material-ui/core/Grid';
import stepsEnum from './steps'

import Stepper from './stepper'
import Questions from './questions/questions'
import Recommendation from './recommendation/recommendation'
import Topics from './topics/topics'

class Content extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            topics: {},
            superTopics: null,
            step: stepsEnum.TOPICS,
            wrongQuestions: []
        };
        this.changeActiveTab = this.changeActiveTab.bind(this);
        this.setCorrected = this.setCorrected.bind(this);
        this.clickStep = this.clickStep.bind(this);
    }

    componentWillMount() {
        let self = this;
        axios.get('http://35.211.99.4:8000/topics/').then(function (response) {
            let topics_reference = [];

            response.data.forEach((item) => {
               topics_reference = topics_reference.concat(item.topic_list);
                console.log(item.topic_list);
            });

            console.log(topics_reference);

            let topics = {};
            topics_reference.forEach((item) => {
                topics[item["code"]] = item["description"];
            });

            self.setState({
                topics: topics,
                superTopics: response.data
            });

            console.log(response.data);

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
        if (step === stepsEnum.TOPICS) {
            return (
                <Topics/>
            )
        }
        else if (step === stepsEnum.ANSWERS || step === stepsEnum.QUESTIONS) {
            return (
                <Questions topics={this.state.topics}
                           descriptionRef={this.props.descriptionRef}
                           setCorrected={this.setCorrected}/>
            )
        } else if (step === stepsEnum.RECOMMENDATION) {
            return (
                <Recommendation wrongQuestions={this.state.wrongQuestions} descriptionRef={this.props.descriptionRef}/>
            )
        }
    }

    render() {
        return (
            <Grid container justify='center' spacing={40} style={{width: "100%", marginLeft: 0, marginRight: 0}}>
                <Stepper step={this.state.step} clickStep={this.clickStep}/>
                {this.getContent()}
            </Grid>
        );
    }
}

export default Content;
