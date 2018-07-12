import React from 'react'
import axios from 'axios';
import Grid from '@material-ui/core/Grid';

import Instructions from '../instructions';
import QuestionCard from './card';
import SendButton from './button';
import Alert from './alert';
import Loading from '../loading';

let state = {
    questionsData: [],
    total: 0,
    questionsAnswers: {},
    unansweredQuestions: [],
    answered: false,
    questionsCorrectAlternatives: null
};

let unmounted = false;

class QuestionCardList extends React.Component {
    constructor(props) {
        super(props);
        this.state = state;
        this.changeSelectedAlternative = this.changeSelectedAlternative.bind(this);
        this.clickButton = this.clickButton.bind(this);
    }

    componentWillMount() {
        if (unmounted === true) {
            return;
        }
        let self = this;
        axios.get('http://localhost:8000/questions/topics=/').then(function (response) {
            let questions = response.data;
            let questionsAnswers = {};

            questions.forEach((item) => {
                questionsAnswers[item._id] = -1;
            });

            self.setState({
                questionsData: questions,
                total: questions.length,
                questionsAnswers: questionsAnswers
            });
        });
    }

    changeSelectedAlternative(questionId, alternative) {
        this.setState((prevState) => {
            let questionsAnswers = prevState.questionsAnswers;
            questionsAnswers[questionId] = alternative;
            return {questionsAnswers: questionsAnswers};
        });
    }

    clickButton() {
        let unanswered = checkUnanswered(this.state.questionsAnswers);
        if (unanswered.length === 0) {
            this.setState({
                answered: true
            });
            this.getQuestionsCorrectAlternatives();
        }
        this.setState({unansweredQuestions: unanswered});
        window.scroll({top: this.props.descriptionRef.current.clientHeight + 30, behavior: 'smooth'});
    }

    getQuestionsCorrectAlternatives() {
        let questionsIdList = this.state.questionsData.map((item) => {
            return item._id;
        });
        axios.post('http://localhost:8000/answers/', {id_list: questionsIdList})
            .then((response) => {
                let questionsCorrectAlternatives = {};
                response.data.forEach((item) => {
                    questionsCorrectAlternatives[item.id] = item.correct_alt;
                });
                this.setState({
                    questionsCorrectAlternatives: questionsCorrectAlternatives
                });
                this.props.setCorrected(getWrongQuestions(this.state.questionsAnswers, questionsCorrectAlternatives));
            });
    }

    renderInstructions() {
        if (!this.state.answered) {
            return (<Instructions text="Responda as seguintes perguntas:"
                                  subText="Ao concluir o questionário, você poderá ver quais foram os seus erros e,
                                  baseado neles, será indicada uma lista exclusiva de materiais da web para que você
                                  possa tirar suas dúvidas e avançar nos estudos."/>);
        } else {
            return (<Instructions text="Veja seus acertos e erros:"
                                  subText={<span>Depois, clique no <b>passo 3</b> acima para
                                      conferir uma lista de materiais recomendados para você que preparamos baseado em
                                      suas dificuldades!!</span>}/>);
        }
    }

    getCorrectAlternative(_id) {
        let questionsCorrectAlternatives = this.state.questionsCorrectAlternatives;
        if (questionsCorrectAlternatives !== null) {
            let correctAlternative = questionsCorrectAlternatives[_id];
            if (correctAlternative !== undefined) {
                return correctAlternative;
            }
        }
        return false;
    }

    render() {
        let questions = this.state.questionsData;

        let cardList = questions.map((item, index) => {
            let unanswered = this.state.unansweredQuestions.includes(item._id);
            let correctAlternative = this.getCorrectAlternative(item._id);
            let selectedAlternative = this.state.questionsAnswers[item._id];
            return <QuestionCard key={index}
                                 index={index}
                                 total={this.state.total}
                                 question={item}
                                 topics={this.props.topics}
                                 changeSelectedAlternative={this.changeSelectedAlternative}
                                 unanswered={unanswered}
                                 correctAlternative={correctAlternative}
                                 selectedAlternative={selectedAlternative}/>
        });

        return (
            <Grid container justify='center' spacing={16} style={{width: "100%", marginLeft: 0, marginRight: 0}}>
                {this.state.unansweredQuestions.length > 0 &&
                <Alert/>
                }
                {this.renderInstructions()}
                {((questions.length === 0) || (this.state.answered === true && this.state.questionsCorrectAlternatives === null)) &&
                <Loading/>
                }
                {cardList}
                {questions.length > 0 && !this.state.answered &&
                <SendButton clickButton={this.clickButton}/>
                }
            </Grid>
        );
    }

    componentWillUnmount() {
        state = this.state;
        unmounted = true;
    }

}

function checkUnanswered(questionsAnswers) {
    let unanswered = [];
    for (let key in questionsAnswers) {
        if (questionsAnswers[key] === -1) {
            unanswered.push(key);
        }
    }
    return unanswered;
}

function getWrongQuestions(questionsAnswers, questionsCorrectAlternatives) {
    let wrongQuestions = [];
    for (let key in questionsAnswers) {
        if (questionsAnswers[key] !== questionsCorrectAlternatives[key]) {
            wrongQuestions.push(key);
        }
    }
    return wrongQuestions;
}

export default QuestionCardList