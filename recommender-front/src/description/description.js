import React from 'react'
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

import colors from '../colors'

const iStyle = {
    color: colors.orangeText
};

const textStyle = {
    color: colors.grayText
};

let Description  = React.forwardRef((props, ref) => {

        return (
            <Grid item xs={12} md={9}>
                <div ref={ref}>
                    <Typography style={textStyle}>
                        <i style={iStyle}><b>Não</b> sei o que <b>não</b> sei</i> é um <i>Sistema
                            de Recomendação
                            Educacional.</i>
                    </Typography>
                    <Typography style={textStyle}>
                        Inicialmente voltado para a disciplina de Introdução a Ciência da
                        Computação, ele pretente ajudar os estudantes a encontrar os melhores materiais de
                        estudo que se adequem às suas dúvidas e necesidades.
                    </Typography>
                </div>
            </Grid>
        );
})

export default Description;