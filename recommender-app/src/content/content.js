import React from 'react';
import axios from 'axios';

import Tabs from './tabs'
import Questions from './questions/questions'

class Content extends React.Component {

    tabNames = ['Perguntas', 'Materiais recomendados'];

    constructor(props) {
        super(props);
        this.state = {
            activeTab: 0,
            topics: {},
            corrected: false
        };
        this.changeActiveTab = this.changeActiveTab.bind(this);
        this.setCorrected = this.setCorrected.bind(this);
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

    setCorrected() {
        this.setState({
            corrected: true
        });
    }

    render() {
        return (
            <div className="row">
                <Tabs
                    tabNames={this.tabNames}
                    activeTab={this.state.activeTab}
                    changeActiveTab={this.changeActiveTab}
                    corrected={this.state.corrected}
                />
                <Questions topics={this.state.topics}
                           descriptionRef={this.props.descriptionRef}
                           setCorrected={this.setCorrected}/>
            </div>
        );
    }

}

export default Content;
