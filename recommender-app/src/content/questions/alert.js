import React from 'react'

import colors from '../../utils'

class Alert extends React.Component {

    render() {
        return (
            <div className='col s12 m10 offset-m1'>
                <div className={'card ' + colors.warningAlert}>
                    <div className='card-content'>
                        <p className=''>
                            <i className='material-icons left'>error</i>
                            <b>É necessário responder todas as perguntas para concluir o questionário</b><br/>
                            Verifique qual pergunta não foi respondida e clique novamente em "CONCLUIR QUESTIONÁRIO"</p>
                    </div>
                </div>
            </div>
        );
    }

}

export default Alert;