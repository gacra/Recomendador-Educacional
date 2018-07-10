import React from 'react'
import axios from 'axios';
import Grid from '@material-ui/core/Grid';

import Instructions from '../instructions'
import QuestionCard from './card'
import SendButton from './button'
import Alert from './alert'

class QuestionCardList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            questionsData: [],
            total: 0,
            questionsAnswers: {},
            unansweredQuestions: [],
            answered: false,
            questionsCorrectAlternatives: null
        };
        this.changeSelectedAlternative = this.changeSelectedAlternative.bind(this);
        this.clickButton = this.clickButton.bind(this);
    }

    componentWillMount() {
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
        console.log(this.props.descriptionRef.current.clientHeight);
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
                this.props.setCorrected();
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
                                  subText={<span>Depois, clique na aba <b>MATERIAIS RECOMENDADOS</b> acima para
                                      conferir uma lista de materiais recomendados para você que preparamos baseado em
                                      suas dificuldades!!</span>}/>);
        }
    }

    render() {
        let questions = this.state.questionsData;

        let cardList = questions.map((item, index) => {
            let unanswered = this.state.unansweredQuestions.includes(item._id);
            let questionsCorrectAlternatives = this.state.questionsCorrectAlternatives;
            let correctAlternative = questionsCorrectAlternatives !== null && (questionsCorrectAlternatives[item._id] || false);
            return <QuestionCard key={index}
                                 index={index}
                                 total={this.state.total}
                                 question={item}
                                 topics={this.props.topics}
                                 changeSelectedAlternative={this.changeSelectedAlternative}
                                 unanswered={unanswered}
                                 correctAlternative={correctAlternative}/>
        });

        return (
            <Grid container justify='center' spacing={16} style={{width: "100%", marginLeft: 0 , marginRight:0}}>
            {this.state.unansweredQuestions.length > 0 &&
                <Alert/>
                }
                {this.renderInstructions()}
                {cardList}
                {!this.state.answered &&
                <SendButton clickButton={this.clickButton}/>
                }
            </Grid>
        );
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

export default QuestionCardList