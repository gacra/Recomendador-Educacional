import React from 'react';
import colors from '../utils';

import '../index.css'

var recommendationTab = 1;

class Tabs extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            visited: false
        };
        this.changeActiveTab = this.changeActiveTab.bind(this);
    }


    changeActiveTab(index) {
        this.props.changeActiveTab(index);
        if (this.props.corrected && index === recommendationTab) {
            this.setState({
                visited: true
            });
        }
    }

    render() {
        let activeTab = this.props.activeTab;
        let self = this;
        let tabs = this.props.tabNames.map((value, index) => {
            let color = activeTab === index ? colors.orangeTertiary : "";

            console.log(this.props.corrected);

            let valueHTML = (index === recommendationTab && self.props.corrected && !self.state.visited) ? (
                <span><b>{value}</b></span>) : (<span>{value}</span>);

            let className = "tab col s3 " + color;

            return (
                <li key={index} className={className} onClick={self.changeActiveTab.bind(null, index)}>
                    <a style={{cursor: 'pointer'}} className={colors.orangeText}>
                        {valueHTML}
                    </a>
                </li>
            )
        });

        let offsetIndicator = "offset-s" + (activeTab * 6) + " offset-l" + (activeTab * 3);

        return (
            <div className="col s12">
                <div className="card white">
                    <ul className="tabs" id={"tabs"}>
                        {tabs}
                        <li className={"indicator col s6 l3 " + offsetIndicator + " " + colors.deepOrange}></li>
                    </ul>
                </div>
            </div>
        );
    }

}

export default Tabs;