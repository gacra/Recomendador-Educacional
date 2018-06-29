import React from 'react';
import colors from '../utils'

class Description extends React.Component {

    iconStyle = {
        color: "#5f5f5f"
    };

    render() {
        return (
            <div className="row">
                <div className="col s10 offset-s1">
                    <div className="card white">
                        <div className="card-content" style={this.iconStyle}>
                            <p><i className={colors.orangeText}><b>Não</b> sei o que <b>não</b> sei</i> é um <i>Sistema
                                de Recomendação
                                Educacional.</i></p>
                            <p>Inicialmente voltado para a disciplina de Introdução a Ciência da
                                Computação, ele pretente ajudar os estudantes a encontrar os melhores materiais de
                                estudo que se adequem às suas dúvidas e necesidades.</p>
                            <p>Para usá-lo, basta você responder as perguntas propostas. Ao concluir o questionário,
                                você poderá ver quais foram os seus erros e, baseado neles, será indicada uma lista
                                exclusiva de materiais da web para que você possa tirar suas dúvidas e avançar nos
                                estudos.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

}

export default Description;