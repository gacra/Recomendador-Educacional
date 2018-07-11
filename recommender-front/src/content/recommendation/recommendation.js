import React from 'react'
import axios from 'axios';
import Grid from '@material-ui/core/Grid';

import Instructions from '../instructions'
import Material from './material'
import Pagination from './pagination'
import Loading from '../loading'

let state = {
    total: 0,
    materials: null,
    page: 0
};

class Recommendation extends React.Component {
    constructor(props) {
        super(props);
        this.state = state;
        this.changePage = this.changePage.bind(this);
    }

    getMaterials(page) {
        this.setState({
            materials: null,
            page: page
        });
        window.scroll({top: (this.props.descriptionRef.current.clientHeight + 30)});
        let url = 'http://localhost:8000/materials/?page=' + (page + 1);
        axios.post(url, {id_list: this.props.wrongQuestions})
            .then((response) => {
                this.setState({
                    materials: response.data.results,
                    total: response.data.count,
                })
            });
    }

    componentWillMount() {
        this.getMaterials(this.state.page);
    }

    changePage(page) {
        this.getMaterials(page);
    }

    getInstructions() {
        if (this.state.materials !== null && this.state.materials.length === 0) {
            return (
                <Instructions
                    text="Parabéns!!!"
                    subText="Você acertou todas as perguntas..."/>
            );
        } else {
            return (
                <Instructions
                    text="Materiais recomendados para você:"
                    subText={'Encontramos ' + this.state.total + ' resultados (página ' + (this.state.page + 1) +
                    ' de ' + Math.ceil(this.state.total / 10) + ')'}/>
            );
        }
    }

    render() {
        let material = this.state.materials; //null=loading   []=you're a genius
        let materialList = null;

        if (material !== null) {
            materialList = material.map((item) => {
                return (<Material key={item._id} material={item}/>);
            });
        }

        return (
            <Grid container justify='center' spacing={16} style={{width: "100%", marginLeft: 0, marginRight: 0}}>
                {this.getInstructions()}
                {material === null &&
                <Loading full={true}/>
                }
                {materialList}
                {(this.state.materials !== null && this.state.materials.length > 0) &&
                <Pagination page={this.state.page} total={this.state.total} changePage={this.changePage}/>
                }
            </Grid>
        )
    }

    componentWillUnmount() {
        state = this.state;
    }

}

export default Recommendation;