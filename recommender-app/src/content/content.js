import React from 'react';

import Tabs from './tabs'

class Content extends React.Component {

    tabNames = ['Perguntas', 'Materiais recomendados'];

    constructor(props) {
        super(props);
        this.state = {activeTab: 0};
        this.changeActiveTab = this.changeActiveTab.bind(this);
    }

    changeActiveTab(index) {
        this.setState({activeTab: index})
    }

    render() {
        return (
            <div className="row">
                <Tabs
                    tabNames={this.tabNames}
                    activeTab={this.state.activeTab}
                    changeActiveTab={this.changeActiveTab}
                />
            </div>
        );
    }

}

export default Content;
